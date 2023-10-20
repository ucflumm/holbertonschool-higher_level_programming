def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check inheritance from.
    :return: True if the object inherits from a_class, otherwise False.
    """
    if type(obj) is not a_class:
        for base in type(obj).__mro__:
            if base is a_class:
                return True
    return False
