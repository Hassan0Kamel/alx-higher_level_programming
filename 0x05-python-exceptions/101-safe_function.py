#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Execuon safely.
    Args:
        fct: Thction to execute.
        args: Argumect.
    Returns:
        If an error occurs - Nne.
        Otherwise - thet of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
