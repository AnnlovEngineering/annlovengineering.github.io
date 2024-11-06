# -- Project information -----------------------------------------------------
project = 'Annlöv Engineering'
author = 'Annlöv Engineering'
release = '0.9'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # To generate API documentation from docstring
    'sphinx.ext.napoleon',  # To support Google-style or NumPy -style docstring
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinx_rtd_dark_mode',
]

# Paths for templates and static files (such as custom CSS)
templates_path = ['_templates']
exclude_patterns = [
    'env/Lib/site-packages/**/*',  # Exkluderar site-packages i din venv
    '**/env/Lib/site-packages/**/*' # Exkluderar om din venv är på andra nivåer
]

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# user starts in light mode
default_dark_mode = False

# This will import the Read the Docs theme (if you have installed it with pip)
#import sphinx_rtd_theme
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Optional: You can specify a logo or favicon for your documentation.
# html_logo = 'path/to/logo.png'
# html_favicon = 'path/to/favicon.ico'

# Paths for custom static files (such as CSS)
html_static_path = ['..\_static']
html_extra_path = ['..\_static']
