from abc import*

class Shape(ABC):
    @abstractmethod
    def area(self,dim1,dim2):
        pass

class Rectangle(Shape):
    def area(self,dim1,dim2):
        print("Area of rectangle=",dim1*dim2)
        print("The dimensions of the rectangle are:",dim1,"and ",dim2)
obj=Rectangle()
obj.area(10,5)

