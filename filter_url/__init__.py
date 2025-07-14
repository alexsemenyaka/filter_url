

"""
filter_url: Some description, maybe?
"""

import importlib.metadata

_metadata = importlib.metadata.metadata("filter_url")
__version__ = _metadata["Version"]
__author__ = _metadata["Author-email"]
__license__ = _metadata["License"]

__all__ = [
]
