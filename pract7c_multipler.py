class Numbers(object):
    MULTIPLER=3.5
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def add(self,x,y):
        self.x=x
        self.y=y
        return self.x+self.y
    @classmethod
    def multiply(cls,a):
        return cls.MULTIPLER*a
    @staticmethod
    def subtract(b,c):
        return b-c
    @property
    def value(self):
        print("Getting Value")
        return(self.x,self.y)
    @value.setter
    def value(self,xy_tuple):
        print("Setting Value")
        self.x,self.y=xy_tuple
    @value.deleter
    def value(self):
        print("Deleting Value")
        del self.x
        del self.y
        print("Value Deleted")
x=Numbers()
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
Add=x.add(a,b)
print("Addition is :",Add)
Sub=x.subtract(a,b)
print("Subtraction is :",Sub)
Mul=x.multiply(a)
print("Multiplication is :",Mul)
get_var=x.value
print(get_var)
x.value=(20,10)
get_var=x.value
print(get_var)
del x.value
