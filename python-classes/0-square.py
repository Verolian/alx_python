'''the module will define the class square'''
class Square:
    '''initializing size'''
    def __init__(self, size):
        self.__size = size
        

if __name__ == "__main__":
    my_square = Square(3)
    '''Output:class '__main__.Square'''
    print(type(my_square))  
    
    '''Output: {'_Square__size': 3}'''
    print(my_square.__dict__)  
    ''' Trying to access private attribute directly raises an AttributeError'''
    try:
        print(my_square.size)  

    except AttributeError as e: # Output: 'Square' object has no attribute 'size'
        print(e)  
    try:
        print(my_square.__size)  
        ''' Trying to access private attribute directly raises an AttributeError'''
    except AttributeError as e:
        print(e)  # Output: 'Square' object has no attribute '__size'
print(Square.__dict__)     