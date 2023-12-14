'''module with function that checks if functions are inherited from another class'''
def inherits_from(obj, a_class):
    '''Get the classes the object is an instance of'''
    obj_classes = type(obj).__mro__
    
    ''' Check if any class in the object's method resolution order is a subclass of a_class'''
    for cls in obj_classes:
        if cls is a_class or issubclass(cls, a_class):
            return True
    
    return False


# a = True
# if inherits_from(a, int):
#     print("{} inherited from class {}".format(a, int.__name__))
# if inherits_from(a, bool):
#     print("{} inherited from class {}".format(a, bool.__name__))
# if inherits_from(a, object):
#     print("{} inherited from class {}".format(a, object.__name__))