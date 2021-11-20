class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Car started, let's ride!")
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print(f"Speed is {self.speed} Vrooooom!")
        else:
            print("You need to start the car first")
    def stop(self):
        self.speed = 0
# inherit Vehicle
class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True
        print(self.trunk_open)
    def close_trunk(self):
        self.trunk_open = False
        print(self.trunk_open)

#car = Car()
#car.start()
#print(car.trunk_open)

# override contructor from parent class with custom parameters
class MotorCycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__(True, 85) # call parent class constructor with parameters
    def start(self):
        print('motor broken, damn!')
        super().start()

motorCycle = MotorCycle(True)
motorCycle.start()
motorCycle.increase_speed(15)

if isinstance(motorCycle, MotorCycle):
    print(f'motorcycle is of type {motorCycle}')

# ways of defining a tuple
mytuple = 1, 2, 'Quoc', False, 2.0
mytuplewithparentheses = (1,2,3,'Quoc',True,3.5)
# convert list to tuple by using tuple constructor
mytupleconstructor = tuple([1,2,3,4,'Quoc'])

#forcing keywords when calling the function
def f1(*, integer, string):
    print(integer, string)

f1(integer = 1, string = False)

#unpack dictionary
def f2(a, b):
    print(a, b)

dic = { "a": 2, "b": 3}

f2(**dic)    

# decorator function with accepts a func (function) parameter
def print_argument(func):
    # wrapper function which receives parameter of added function
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)

    return wrapper

#below statement adds function add_one(x) to the decorator function
@print_argument
def add_one(x):
    return x + 100

# invoke add_one which calls the decorator function
print(add_one(1))

# anonymous functions lambda
substract_one = lambda x : x - 1
print(substract_one(100))

# use anonymous functions lambda as arguments
numbers = [1,2,3,4,5]
substracted_by_one = map(substract_one, numbers)

for number in substracted_by_one:
    print(number)

# list comprehensions [ <expression> for item in list if <conditional> ]
list_comp = [substract_one(x) for x in range(1, 20) if x % 2 == 0]
print(list_comp)

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(4)]
print (matrix)

# matrix wordt eerst gelooped dan sublist wordt geloopt en dan resultaat (expression) is value 
x = [value 
     for sublist in matrix
     for value in sublist]
print (x)

# Set comprehensions { <expression> for item in list if <conditional> } accolades instead of brackets
set_comp = {s for s in range(1,5) if s % 2 == 1} # dividable by two
print(set_comp)

#Dictionary comprehensions same as above but define key and value in expression part
dic_comp = { d : d**2 for d in range(1,5) }
print(dic_comp)

# iterator / iterable
myGenerator = range(0, 5)
myIterator = myGenerator.__iter__()
print(myIterator.__next__())
print(myIterator.__next__())

myString = "Quoc" # myString is an iterable object
myIteratorable = myString.__iter__() # returns a iterator

# for loops need an iterable object
for letter in myIteratorable:
    print(letter)

# for loops dictionary with key and values
for k,v in dic.items():
    print(f"{k}:{v}")
