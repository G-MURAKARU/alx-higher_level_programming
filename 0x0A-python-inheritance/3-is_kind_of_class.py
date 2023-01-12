#!/usr/bin/python3


def is_kind_of_class(obj, a_class) -> bool:
    """
    is_kind_of_class returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj (any): input object to investigate
        a_class (_type_): possible class of obj

    Returns:
        bool: whether obj is an instance of a_class or a_class's parent class(es)
    """

    return isinstance(obj, a_class)
