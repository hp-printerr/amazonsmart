
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

project = 'Amazon Mytv'


# The full version, including alpha/beta/rc tags
#release = '1.0.0'

html_static_path = ['_static']

def setup(app):
    app.add_css_file('custom.css')

html_meta = {
    "msvalidate.01": "108BF3BCC1EC90CA1EBEFF8001FAEFEA"
   
}




# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. These files are copied after the built-in
# static files, so a file named "default.css" will overwrite the built-in one.
# html_static_path = ['_static']
