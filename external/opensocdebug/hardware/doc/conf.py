# -*- coding: utf-8 -*-
#
# Open SoC Debug Hardware documentation build configuration file, created by
# sphinx-quickstart on Tue Dec 20 09:23:57 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.abspath('../test/cocotb'))
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'mocks')))
# sys.path.append(os.path.abspath(os.environ.get('COCOTB')))
#sys.path.append(os.path.abspath(os.path.join(os.environ.get('COCOTB'), 'lib')))
os.environ["SPHINX_BUILD"] = "1"


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.todo']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Open SoC Debug Hardware'
copyright = u'2016-2017, The Open SoC Debug Contributors'
author = u'The Open SoC Debug Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The Read the Docs theme is available from
# https://github.com/snide/sphinx_rtd_theme
#
# Install with
# - pip install sphinx_rtd_theme
# or
# - apt-get install python-sphinx-rtd-theme

try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
except ImportError:
    sys.stderr.write('Warning: The Sphinx \'sphinx_rtd_theme\' HTML theme was ' +
                     'not found. Make sure you have the theme installed to produce pretty ' +
                     'HTML output. Falling back to the default theme.\n')

    html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'OpenSoCDebugHardware.tex', u'Open SoC Debug Hardware Documentation',
     u'The Open SoC Debug Contributors', 'manual'),
]


# autodoc configuration
# See additional mocks for objects which cannot be automatically mocked in
# mocks/*.
autodoc_mock_imports = ["cocotb.triggers", "cocotb.result", "cocotb.clock"]
autodoc_member_order = 'bysource'

# Napoleon configuration (converts Google-style docstrings to autodoc)
napoleon_numpy_docstring = False
napoleon_google_docstring = True
