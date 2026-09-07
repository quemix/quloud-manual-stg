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
  engines: SimulationEngine.order(:code).map { |e|
    { code: e.code, name: e.name, description: e.description, active: e.active? }
  },
  capabilities: Capability.order(:sort_order).map { |c|
    { code: c.code, name_ja: c.name_ja, name_en: c.name_en,
      description_ja: c.description_ja, description_en: c.description_en }
  },
  workflow_templates: WorkflowTemplate.order(:sort_order).map { |t|
    { key: t.key, capability: t.capability&.code, name_ja: t.name_ja,
      name_en: t.name_en, enabled: t.enabled }
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

File.write('/app/tmp_master_dump.json', JSON.pretty_generate(data))
warn "wrote /app/tmp_master_dump.json  ec=#{data[:engine_capabilities].size}"
