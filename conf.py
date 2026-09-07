# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Quloud Ver.7.0 Manual'
copyright = '2026, Quemix Inc'
author = 'Quemix inc'
version = '2026.4.20'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.mathjax', 'sphinx.ext.githubpages', 'sphinx_last_updated_by_git']
# extensions = ['sphinx.ext.mathjax', 'sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = [
    '_build', 'docs', 'Thumbs.db', '.DS_Store', '.venv',
    'source/_generated', 'meta', 'tools', 'README.md',
]

language = 'ja'

numfig = True
numfig_secnum_depth = 1
#math_number_all = True 
#math_numfig = True
#math_eqref_format = "Eq.{number}"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_extra_path = ['CNAME']
html_style = 'css/my_theme.css'
#html_logo = '_static/Quloud_A_color.png'
html_title = ''
html_short_title = 'aa'
html_theme_options = {
    # 'logo_only': True,
    # 'sticky_navigation': True,
    # 'titles_only': True,
    # 'display_version': True,
    # 'flyout_display': 'attached',
    # 'version_selector': True,
    # 'language_selector': True,
    # 'collapse_navigation': True,
}
html_last_updated_fmt = '%b %d, %Y'
html_favicon = 'source/images/favicon/Quloud_B.png'
html_show_sphinx = False
