# -*- coding: utf-8 -*-
#
# Multilingual websites with Sphinx documentation build configuration file, created by
# sphinx-quickstart on Thu Nov 13 11:09:54 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

extlinks = {}
extensions = []
intersphinx_mapping = {}

from atelier.sphinxconf import configure
configure(globals(), 'lino_welfare.projects.std.settings.doctests')

extensions += ['lino.sphinxcontrib.actordoc']
extensions += ['lino.sphinxcontrib.logo']


from django.conf import settings
settings.SITE.title = "Lino Welfare Reference Manual"

from django.utils.importlib import import_module
for n in 'atelier lino'.split():
    m = import_module(n)
    intersphinx_mapping[n] = (m.intersphinx_urls['docs'], None)


extensions += ['sphinx.ext.autosummary']
autosummary_generate = True
autodoc_default_flags = ['members']


primary_domain = 'py'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
#~ project = u"Lino-Welfare"
project = settings.SITE.title
copyright = u'2012-2014, Luc Saffre'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
#~ version = lino_welfare.__version__
# The full version, including alpha/beta/rc tags.
#~ from lino_welfare.modlib.pcsw.settings import LINO
release = settings.SITE.version

# The short X.Y version.
version = '.'.join(release.split('.')[:2])


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#~ language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = []

exclude_patterns = [
    '.build/*',
    'include/*',
]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Lino Welfare"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#~ html_logo = 'logo.jpg'
# html_logo = 'lino-logo-2.png'
# html_logo = '.static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'
#~ last_updated = True

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#~ html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# http://sphinx.pocoo.org/latest/config.html#confval-html_sidebars
html_sidebars = {
    '**': ['languages.html', 'globaltoc.html',
           'searchbox.html', 'links.html'],
}


# Additional templates that should be rendered to pages, maps page names to
# template names.
#~ html_additional_pages = {
    #~ '*': 'links.html',
#~ }


# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = ''
#~ html_use_opensearch = 'http://lino.saffre-rumma.net'

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'welfare'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'lino.tex', ur'lino', ur'Luc Saffre', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

#language="de"

#~ show_source = True

#~ srcref_base_uri="http://code.google.com/lino"
#~ srcref_base_uri="http://code.google.com/p/lino/source/browse/#hg" 

extlinks.update(ticket=('http://trac.lino-framework.org/ticket/%s', '#'))

# extlinks = {
#   'issue': ('http://code.google.com/p/lino/issues/detail?id=%s', 'Issue '),
#   'checkin': ('http://code.google.com/p/lino-welfare/source/detail?r=%s', 'Checkin '),
#   'srcref': ('http://code.google.com/p/lino-welfare/source/browse%s', ''),
#   'extjs': ('http://www.sencha.com/deploy/dev/docs/?class=%s', ''),
#   'extux': ('http://extjs-ux.org/ext-docs/?class=%s', ''),
#   'welfareticket': ('http://welfare.lino-framework.org/tickets/%s.html', ''),
#   'djangoticket': ('http://code.djangoproject.com/ticket/%s', 'Django ticket #'),
#   'lino': ('http://www.lino-framework.org%s.html', ''),
# }

# extlinks.update(
#     lino=('http://www.lino-framework.org%s.html', ''))

# import lino_welfare
# extlinks.update(srcref=(lino_welfare.srcref_url, ''))

#~ nitpicky = True # use -n in Makefile instead

#~ todo_include_todos = True

# http://sphinx.pocoo.org/theming.html
# html_theme = "classic"
# html_theme_options = dict(collapsiblesidebar=True, externalrefs=True)
