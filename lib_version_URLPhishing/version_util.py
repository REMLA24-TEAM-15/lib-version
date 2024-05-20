"""
Module for version utility functions.
"""

from .version import __version__


class VersionUtil:
    """
    A utility class for version-related operations.
    """

    @staticmethod
    def get_version():
        """
        Get the current version of the library.
        """
        return __version__

