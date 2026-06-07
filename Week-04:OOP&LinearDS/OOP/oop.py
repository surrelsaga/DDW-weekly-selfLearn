import math

# Class definition
class RobotTurtle:
    # Attributes:
    def __init__(self, name, speed=1):
        self._name = name
        self._speed = speed
        self._pos = (0, 0)

    #  getter method
    def get_pos(self):
        return self._pos

    # Methods:
    def move(self, direction):
        update = {'up' : (self.pos[0], self.pos[1] + self.speed),
                  'down' : (self.pos[0], self.pos[1] - self.speed),
                  'left' : (self.pos[0] - self.speed, self.pos[1]),
                  'right' : (self.pos[0] + self.speed, self.pos[1])}
        self._pos = update[direction]


    # def tell_name(self):
    #     print(f"My name is {self.name}")
        
    # def get_name(self):
    #     return self._name
    
    # def set_name(self, value):
    #     self._name = value
        
    # pos = property(get_pos)
    
    # # This is how to set up getter/setter to an attribute
    # name = property(get_name, set_name)
    
    # set up the property getter
    @property
    def name(self):
        return self._name
    
    @name.setter #choose which property to set up setter
    def name(self, value):
        if isinstance(value, str) and value != "":
            self._name = value
    
    @property
    def speed(self):
        return self._speed
    
class Coordinate:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        
        return Coordinate(new_x, new_y)

firstRobot = RobotTurtle('nino')
firstRobot.name = 'rhino'

p1 = Coordinate(3, 4)
p2 = Coordinate(1, 2)
p3 = p1 + p2

print(p3)
