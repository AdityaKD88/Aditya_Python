class Shape:

    def __init__(self,w=0,h=0):
        self.width=w
        self.height=h

    def area(self):
        return self.height*self.width

    def parameter(self):
        return 2*self.height*self.width
    
    def __lt__(self,other):
        if self.area() < other.area():
            return True
        return False

    def __repr__(self):
        return str(self.area())

items=[Shape(2,2),Shape(1,5),Shape(3,3),Shape(10,10),Shape(3,2)]
print(items)


if Shape(38,39) > Shape(13,72):
    print('Yes')

items.sort()
print(items)