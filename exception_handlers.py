"""
This module contains functions to handle execeptions
"""


def get_error_type(function_to_validate, *args):
    """
    (function, *args) -> type(Exception) | None
    validates a function and return error type if found or None
    """
    try:
        function_to_validate(*args)
    except Exception as e:
        return type(e)
