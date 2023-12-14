class Person:#parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):#child class with attributes from the parent class
  def __init__(self, fname, lname):#init function belonging to the child class
    Person.__init__(self, fname, lname)#init function belonging to the parent class i used the class name"Person" 

x = Student("Mike", "Olsen")
x.printname()




#using super method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)#used the "super" instead of the class "Person" name

x = Student("Mike", "Olsen")
x.printname()


#adding prperties to the child class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)