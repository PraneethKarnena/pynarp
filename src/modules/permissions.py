import os


def has_permissions():
    return os.geteuid() == 0