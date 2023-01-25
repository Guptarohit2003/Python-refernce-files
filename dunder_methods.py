#dunders = double underscores

'''class Person:
    def __init__(self,weight,age,salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self,other):
        return self.weight + other.weight

p1 = Person(44,50,33)
p2 = Person(32,66,30)

print(p1+p2)'''

# Scenario
# Create a class representing a time interval;
# the class should implement its own method for addition, subtraction on time interval class objects;
# the class should implement its own method for multiplication of time interval class objects by an integer-type value;
# the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
# the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
# check the argument type, and in case of a mismatch, raise a TypeError exception.

'''class time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __add__(self,other):
        if isinstance(other, time):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            another = other.hours*3600 + other.minutes*60 + other.seconds
            new_time = own + another
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        else:
            raise TypeError("can only add time intervals")
    def __sub__(self,other):
        if isinstance(other, time):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            another = other.hours*3600 + other.minutes*60 + other.seconds
            new_time = own - another
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        else:
            raise TypeError("can only subtract time intervals")
    def __mul__(self,other):
        if isinstance(other, int):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            new_time = own*other
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        else:
            raise TypeError("can only multiply time interval objects by int")
    def __str__(self):
        return "%s:%s:%s"%(self.hours,self.minutes,self.seconds)

t1 = time(hours=21, minutes=58, seconds=50)
t2 = time(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'

print("EVERYTHING WORKING FINE")'''
        

# Scenario
# Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
# to add an integer to a time interval object means to add seconds;
# to subtract an integer from a time interval object means to remove seconds.


'''class time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __add__(self,other):
        if isinstance(other, time):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            another = other.hours*3600 + other.minutes*60 + other.seconds
            new_time = own + another
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        elif isinstance(other,int):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            new_time = own + other
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        else:
            raise TypeError("can only add time intervals or int object")
    def __sub__(self,other):
        if isinstance(other, time):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            another = other.hours*3600 + other.minutes*60 + other.seconds
            new_time = own - another
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        elif isinstance(other,int):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            new_time = own - other
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds) 
        else:
            raise TypeError("can only subtract time intervals or int object")
    def __mul__(self,other):
        if isinstance(other, int):
            own = self.hours*3600 +self.minutes*60 +self.seconds
            new_time = own*other
            new_hours = new_time//3600
            new_minutes = (new_time%3600)//60
            new_seconds = new_time %60
            return time(hours=new_hours,minutes=new_minutes,seconds=new_seconds)
        else:
            raise TypeError("can only multiply time interval objects by int")
    def __str__(self):
        return "%s:%s:%s"%(self.hours,self.minutes,self.seconds)

t1 = time(hours=21, minutes=58, seconds=50)
t2 = time(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'
assert str(t1 + 62) == '21:59:52'
assert str(t1 - 62) == '21:57:48'

print("EVERYTHING WORKING FINE")'''




































