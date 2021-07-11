import os


def has_permissions():
    """
    Check sudo permissions
    """

    return os.geteuid() == 0