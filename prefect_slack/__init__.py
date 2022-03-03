from . import _version
from .credentials import SlackCredentials, SlackWebhook  # noqa

__version__ = _version.get_versions()["version"]
