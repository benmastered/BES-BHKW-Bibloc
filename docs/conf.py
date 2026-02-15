# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "BES BHKW BIBLOC BV"
copyright = "2026, Handbuch"
author = "Team BES"


# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    'sphinx_rtd_theme',
    "myst_parser",
]
myst_heading_anchors = 7

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
# Optional: Configure linkify behavior
myst_linkify_fuzzy_links = True  # Allow fuzzy matching for URLs without scheme
myst_linkify_anchors = True      # Enable anchor links for headings

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
#html_theme = "blue"
#html_theme = "classic"
#html_theme = "haiku"
#html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

html_logo = "_static/images/logo_header.png"
#html_show_sourcelink = True
#html_favicon = "_static/images/favicon.ico"

# html_sidebars = {
   # '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   # 'using/windows': ['windows-sidebar.html', 'searchbox.html'],
# }

html_theme_options = {
    'logo_only': True,
    'prev_next_buttons_location': 'bottom',
    #'style_external_links': True,
    'sidebarbgcolor':'grey',
    'rightsidebar': 'true',
    #'relbarbgcolor': 'black',
    #'vcs_pageview_mode': 'blob',
    'style_nav_header_background': 'white',
    'flyout_display': 'attached',
    #'version_selector': False,
    #'language_selector': False,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    #'includehidden': False,
    'titles_only': True
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Source - https://stackoverflow.com/a/57840173
# Posted by Jose Cherian, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-13, License - CC BY-SA 4.0

latex_logo = "_static/images/logo_header.png"
latex_use_latex_multicolumn = "true"
latex_table_style = ['booktabs','colorrows']

rinoh_documents = [dict(doc='index',        # top-level file (index.rst)
                        target='manual')]   # output file (manual.pdf)
                        
html_css_files = ['custom.css']
