# TODO: there's code missing in one or more lines below
class Base:
def __init__(self, x, y, size):

# TODO: will need to fill this in
def draw(self):
return ""
class Circle():
def __init__(x, y, size):
super().__init__(x,y,size)
def draw(self):
return f"""
3
CMPE 131: HW2a: Python
({self.x}, {self.y})
{self.size}
, - ~ ~ ~ - ,
, ' ' ,
, ,
, ,
, ,
, ,
, ,
, ,
, ,
, , '
' - , _ _ _ , '
"""
class Square(Base):
def __init__(self, y, size):
super().__init__(x,y,size)
def draw():
return f"""
({self.x}, {self.y})
{self.size}
--------------------
| |
| |
| |
| |
| |
| |
| |
| |
--------------------
"""
# All of the code below is correct
def draw_any_shape(myShape):
print(myShape.draw())
def main():
s = Square(1,2,3)
draw_any_shape(s)
c = Circle(2,2,1)
draw_any_shape(c)
main()
4
