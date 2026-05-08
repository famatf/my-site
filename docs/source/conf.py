# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Archivum Famae'
copyright = '2026, famatf'
author = 'famatf'
release = ''
html_title = 'Archivum Famae'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
]

myst_enable_extensions = [
    "colon_fence",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

html_baseurl = 'https://famatf.com/'
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.ico"
html_js_files = [
    "custom-footer.js",
]

html_last_updated_fmt = "%Y-%m-%d %H:%M"
