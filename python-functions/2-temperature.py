# def convert_to_celsius(fahrenheit):
    # return(fahrenheit-32)*5/9

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Note the use of a single leading underscore to indicate it's a "protected" attribute

    @property
    def radius(self):
        return self._radius