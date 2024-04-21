from . import _version

__version__ = _version.get_versions()["version"]

from .json_wrapper import JsonWrapper
from .object_wrapper import ObjectWrapper
