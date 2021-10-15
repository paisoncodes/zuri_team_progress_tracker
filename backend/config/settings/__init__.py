from .common import *
import os

# you need to set "env = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ.get("env") == "prod":
    from .production import *
else:
    from .development import *