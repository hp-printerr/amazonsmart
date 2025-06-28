# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('../src'))  # Adjust as needed

# -- Project information -----------------------------------------------------

# -- Project information -----------------------------------------------------

project = 'Amazon Smart'
copyright = '2025'
author = 'Your Name'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "show_sidebar": False,
    "show_relbar_top": False,
    "show_relbar_bottom": False,
    "content_max_width": "100%",
}

html_static_path = ['_static']
html_css_files = ['style.css']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# Use the Read the Docs theme for better compatibility with Read the Docs.
# html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. These files are copied after the built-in
# static files, so a file named "default.css" will overwrite the built-in one.
# html_static_path = ['_static']



