#11th day oops
#class
 #classes=classes are userdefined blue print or prototype
#eg:if calculator is class then sum,multiplication and subraction will be methods
#so classes will consists of methods class variables,instance variables and constructor etc
#> creation of new object not needed ex in java we will create new to create object

class calculator:
    num=100
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print('i am called automatically when object is created')
    def getdata(self):
        print("i am now executing as method in class")
    def summation(self):
        return self.firstnumber + self.secondnumber+calculator.num
obj = calculator(20,20)
obj.getdata()
print(obj.num)
print(obj.summation())
# obj1 = calculator()
# obj1.getdata()
#constructor is a method when object is created constructor is first one to call
#self is used as a reference to the current instance of a class whe you define methods with in a class
#you must include self as the first parameter in the method definition.
#self keyword is mandatory for calling variable names into method.constructor name should be
#'__name__' when creating.,new keyword does not required for object.
