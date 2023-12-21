''''the start of my new module and class'''
class Base:
    '''the new nb-object with a value of zero'''
    __nb_objects = 0
    '''setting the id to public'''
    def __init__(self, id=None):
        '''start of conditions in the function'''
        if id is not None:
            self.id = id
        else:
            '''the base class with the increament setting'''
            Base.__nb_objects +-1
            self.id = Base.__nb_objects

'''the test code'''
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)