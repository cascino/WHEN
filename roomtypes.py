from graphics import *
from shortcuts import *


def wilderness():
  name, val = windowMake("Wilderness",windowList,leaves)
  grass = Image(Point(0,0),"assets/sprites/grasses/grass4.png").draw(name)
  grass = Image(Point(0,0),"assets/sprites/grasses/grass3.png").draw(name)


  #The "centerpiece of the region, has interactables and stuff"
  grass = Image(Point(0,0),"assets/sprites/grasses/grass2.png").draw(name)
  
  grass = Image(Point(0,0),"assets/sprites/grasses/grass1.png").draw(name)
  
  
  

windowList = []
leaves = []