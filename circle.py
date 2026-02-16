class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(Self):
        return (22/7) * (Self.radius ** 2)
    
    def perimeter(Self):
        return 2*(22/7)*Self.radius
    
    def display(Self):
        print("Area of the Circle is:", Self.area())
        print("Perimeter of the Circle is:", Self.perimeter())

c1=circle(5)
c1.display()