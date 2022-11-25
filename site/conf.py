from pathlib import Path


ROOT = Path(__file__).resolve().parent

# -- Project information -----------------------------------------------------------------------------------------------

project =   "ITSAS"
copyright = "ITSAS taldea - UPV/EHU"
author =    "ITSAS"


# -- Versioning --------------------------------------------------------------------------------------------------------

version = "latest"  # The short X.Y version.
release = "latest"  # The full version, including alpha/beta/rc tags.


# -- Miscellaneous settings --------------------------------------------------------------------------------------------

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

exclude_patterns = [
	"_build",
	"Thumbs.db",
	".DS_Store",
]

pygments_style = 'stata-dark'


# -- Restructured Text settings ----------------------------------------------------------------------------------------

prologPath = "prolog.inc"
try:
	with open(prologPath, "r") as prologFile:
		rst_prolog = prologFile.read()
except Exception as ex:
	print("[ERROR:] While reading '{0!s}'.".format(prologPath))
	print(ex)
	rst_prolog = ""


# -- Options for HTML output -------------------------------------------------------------------------------------------

html_theme = "alabaster"

html_static_path = ['_static']

#html_logo = str(Path(html_static_path[0]) / "logo" / "edaa_banner_white.svg")
#html_favicon = str(Path(html_static_path[0]) / "logo" / "edaa.svg")

# Output file base name for HTML help builder.
htmlhelp_basename = 'ITSASSite'

html_last_updated_fmt = "%d.%m.%Y"


# -- Options for LaTeX / PDF output ------------------------------------------------------------------------------------

from textwrap import dedent

latex_elements = {
	'papersize': 'a4paper',
	'preamble': dedent(r"""
		% ================================================================================
		% User defined additional preamble code
		% ================================================================================
		% Add more Unicode characters for pdfLaTeX.
		% - Alternatively, compile with XeLaTeX or LuaLaTeX.
		% - https://github.com/sphinx-doc/sphinx/issues/3511
		%
		\ifdefined\DeclareUnicodeCharacter
			\DeclareUnicodeCharacter{2265}{$\geq$}
			\DeclareUnicodeCharacter{21D2}{$\Rightarrow$}
		\fi


		% ================================================================================
		"""),
}

latex_documents = [
	( master_doc,
		'ITSAS.tex',
		'ITSAS',
		'ITSAS',
		'manual'
	),
]


# -- Extensions --------------------------------------------------------------------------------------------------------

extensions = [
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.todo',
]


# -- Sphinx.Ext.InterSphinx --------------------------------------------------------------------------------------------

intersphinx_mapping = {
	'python':          ('https://docs.python.org/3', None),
}


# -- Sphinx.Ext.ExtLinks -----------------------------------------------------------------------------------------------

extlinks = {
	'gh':      ('https://github.com/%s', 'gh:'),
}


# -- Sphinx.Ext.ToDo ---------------------------------------------------------------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True
