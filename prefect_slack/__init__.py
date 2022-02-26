from . import _version
from .credentials import SlackCredentials

__all__ = ["SlackCredentials"]

__version__ = _version.get_versions()["version"]
