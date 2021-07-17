import os


def has_root_permission():
    """
    Check root permissions
    """

    return os.geteuid() == 0