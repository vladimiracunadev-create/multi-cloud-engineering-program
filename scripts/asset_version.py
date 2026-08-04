"""Single source of truth for the versioned asset query string.

Kept dependency-free on purpose: the Pages deploy job verifies the published
site without installing the site extras, so it must import this without
pulling in the generator's third-party dependencies.

Bump this whenever site/app.js, site/index.html, site/service-worker.js or the
class assets change, so browsers and the service worker fetch the new files
instead of serving a stale cached copy.
"""

ASSET_VERSION = "2.1.0-r1"
