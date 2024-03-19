# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

# -- Project information -----------------------------------------------------

project = 'ria'
copyright = '2024, Qoherent Inc'
author = 'Qoherent Inc'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx'
]

autodoc_typehints = "none"

html_favicon = 'branding/riacore.png'

autodoc_typehints_format = "short"
python_use_unqualified_type_names = True

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = []

version_link = f"{sys.version_info.major}.{sys.version_info.minor}"
intersphinx_mapping = {'python': (f'https://docs.python.org/{version_link}', None),
                       'numpy': ('https://numpy.org/doc/stable', None),
                       'scipy': ('https://docs.scipy.org/doc/scipy', None),
                       'matplotlib': ('https://matplotlib.org/stable', None),
                       'torch': ('https://pytorch.org/docs/stable/', None)}


def autodoc_process_docstring(app, what, name, obj, options, lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace("np.", "numpy.")


def setup(app):
    app.connect("autodoc-process-docstring", autodoc_process_docstring)

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
