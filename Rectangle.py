class Rectangle:
    def __init__(self, width,height):
        self.width=width
        self.height=height
        
    def RectangleArea(self):
        return self.width*self.height
    
rectangle= Rectangle(5,3)
area = rectangle.RectangleArea()
print(area)