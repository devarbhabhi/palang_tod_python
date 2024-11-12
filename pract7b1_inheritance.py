class Shape:
    author='Krishna Gupta'
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def Areal(self,x,y):
        self.x=x
        self.y=y
        a=self.x*self.y
        print("Area of Rectangle",a)
    print(author)
class Square(Shape):
    def _init_(self,x):
        self.x=x
    def Area(self,x):
        self.x=x
        a=self.x*self.x
        print("Area of Square",a)
r=Shape()
r.Areal(12,34)
s=Square()
s.Area(34)
s.Areal(16,32)
