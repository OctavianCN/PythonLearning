######### Named Tuples - Application - Returning Multiple Values ##########

from random import  randint, random
from collections import namedtuple

def random_color():
    red = randint(0,255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(),2)
    return red, green, blue, alpha

color = random_color()
print(color)

Color = namedtuple('Color', 'red green blue alpha')
def random_color():
    red = randint(0,255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(),2)
    return Color(red, green, blue, alpha) # better approch

color = random_color()
print(color)
print(color.red)