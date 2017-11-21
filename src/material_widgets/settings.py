"""Customize the sources of the Material CSS and JS files by adding the
MATERIAL_CSS and MATERIAL_JS string constants to the project's ``settings.py``
file.

Default values point to the latest Material CSS and JS from unpkg.com.

Examples
--------
MATERIAL_CSS and MATERIAL_JS string constants should be placed in the project's
``settings.py`` to override default settings.

>>> MATERIAL_CSS = "https://example.com/material.css"

Path joins can be used as long as they result in a valid URL string.

>>> MATERIAL_JS = os.path.join(STATIC_ROOT, "js/material.js")

"""

from django.conf import settings

MATERIAL_CSS = getattr(settings, 'MATERIAL_CSS',
                       ("https://unpkg.com/material-components-web@latest"
                        + "/dist/material-components-web.min.css")
                      )

MATERIAL_JS = getattr(settings, 'MATERIAL_JS',
                      ("https://unpkg.com/material-components-web@latest"
                       + "/dist/material-components-web.min.js")
                     )
