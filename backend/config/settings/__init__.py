from .common import *
from decouple import config

# you need to set "env = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if config("env") == "prod":
    from .production import *
else:
    from .development import *
