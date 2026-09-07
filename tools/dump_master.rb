# frozen_string_literal: true
#
# マスタデータを Quloud の API と同じ解決ロジックで JSON へ落とす。
# ホストからは tools/dump_master.sh 経由で呼ぶ。単体で実行しない。
#
# 重要: パラメータの解決は API::CapabilitiesController の payload builder を
# そのまま呼ぶ。ここで独自に再実装すると canonical フォールバックの扱いが
# API とずれる。キーは必ず mapping.key（capability_parameter.key ではない）。
require 'json'

ActiveRecord::Base.logger = nil
ctrl = API::CapabilitiesController.new

engine_capabilities = EngineCapability
                      .includes(:simulation_engine, :capability)
                      .sort_by { |ec| [ec.simulation_engine.code, ec.sort_order] }

data = {
  generated_at: Time.now.utc.iso8601,
  # DB 側の鮮度シグナル: ここに挙げたマスタテーブルの updated_at の最大値。
  # dump はコンテナの DB を読むだけなので、マスタ YAML を編集しても
  # rake quloud:sync_master_data を流さない限りここは更新されない。
  # source_commit と乖離していれば、マスタが未同期であることに気づける。
  master_synced_at: [
    SimulationEngine, Capability, EngineCapability, CapabilityParameter,
    EngineCapabilityParameterMapping, EngineCapabilityPhysicalParameterMapping,
    EngineCapabilityArtifactSpec, EngineCapabilityPropertyMapping, WorkflowTemplate
  ].filter_map { |model| model.maximum(:updated_at) }.max&.utc&.iso8601,
  engines: SimulationEngine.order(:code).map { |e|
    { code: e.code, name: e.name, description: e.description, active: e.active? }
  },
  capabilities: Capability.order(:sort_order).map { |c|
    { code: c.code, name_ja: c.name_ja, name_en: c.name_en,
      description_ja: c.description_ja, description_en: c.description_en }
  },
  # ステップも落とす。「ジョブ作成」の選択ダイアログに出るのはテンプレート名
  # （name_ja）ではなく、代表 capability の名称と、ステップが使うエンジンの名称。
  # ステップが無いとダイアログの表示を再現できない。
  workflow_templates: WorkflowTemplate.order(:sort_order).map { |t|
    { key: t.key, capability: t.capability&.code, name_ja: t.name_ja,
      name_en: t.name_en, enabled: t.enabled,
      # role が付いているステップは計算ではなく入力の選択（既存 Job や構造を
      # 選ばせるタブ）。create2.vue の computeSteps がこれを除いてから
      # 「計算ソフト」の見出しを組み立てるので、同じ判定ができるように落とす。
      steps: t.workflow_steps.map { |s|
        ib = s.input_binding_json
        { step_no: s.step_no,
          engine: s.engine_capability.simulation_engine.code,
          capability: s.engine_capability.capability.code,
          role: ib.is_a?(Hash) ? (ib['role'] || ib[:role]) : nil }
      } }
  },
  engine_capabilities: engine_capabilities.map { |ec|
    {
      engine: ec.simulation_engine.code,
      capability: ec.capability.code,
      visible: ec.visible,
      recommended: ec.recommended,
      sort_order: ec.sort_order,
      ui_group_key: ec.ui_group_key,
      ui_group_label_ja: ec.ui_group_label_ja,
      legacy_rsdft_job_type: ec.legacy_rsdft_job_type,
      legacy_software_code: ec.legacy_software_code,
      parameters: ec.engine_capability_parameter_mappings
                    .visible.includes(:capability_parameter)
                    .map { |m| ctrl.send(:engine_capability_parameter_mapping_payload, m) },
      physical_model_parameters: ec.engine_capability_physical_parameter_mappings
                                   .visible.includes(:physical_model_parameter)
                                   .map { |m| ctrl.send(:engine_capability_physical_parameter_mapping_payload, m) },
      artifact_specs: ec.engine_capability_artifact_specs.map { |a|
        a.as_json(except: %w[id engine_capability_id created_at updated_at])
      },
      property_mappings: ec.engine_capability_property_mappings.map { |p|
        p.as_json(except: %w[id engine_capability_id created_at updated_at])
      }
    }
  }
}

raise 'engine_capabilities が空。マスタが DB に入っていない可能性がある（rake quloud:sync_master_data 未実行？）' if data[:engine_capabilities].empty?

param_total = data[:engine_capabilities].sum { |ec| ec[:parameters].size + ec[:physical_model_parameters].size }
raise "パラメータが0件。mapping の取得が壊れている可能性がある（ec=#{data[:engine_capabilities].size}）" if param_total.zero?

File.write('/app/tmp_master_dump.json', JSON.pretty_generate(data))
warn "wrote /app/tmp_master_dump.json  ec=#{data[:engine_capabilities].size}"
