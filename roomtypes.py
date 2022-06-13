from graphics import *
from shortcuts import *


def wilds():
  name, val = windowMake("Wilderness",windowList,leaves)


  #far corners
  grass = Image(Point(0,0),"assets/sprites/grasses/grass1.png").draw(name)
  #closer but still far corners
  grass = Image(Point(0,0),"assets/sprites/grasses/grass2.png").draw(name)


  
  grass = Image(Point(0,0),"assets/sprites/grasses/grass3.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/grasses/grass4.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/grasses/grass5.png").draw(name)
  

  #CENTERPIECE
  #if something something
  grass = Image(Point(0,0),"assets/sprites/houses/house6.png").draw(name)
  
  
  grass = Image(Point(0,0),"assets/sprites/grasses/grass7.png").draw(name)

  #near area 
  grass = Image(Point(0,0),"assets/sprites/grasses/grass8.png").draw(name)
  

def urban():
  name, val = windowMake("Urban District",windowList,leaves)

  
def trees():
  name, val = windowMake("Forest",windowList,leaves)


  #far corner
  grass = Image(Point(0,0),"assets/sprites/trees/tree1.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/trees/tree2.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/trees/tree3.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/trees/tree4.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/trees/tree5.png").draw(name)


  #CENTERPIECE
  #if something something
  grass = Image(Point(0,0),"assets/sprites/trees/tree6.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/trees/tree7.png").draw(name)

  
  grass = Image(Point(0,0),"assets/sprites/trees/tree8.png").draw(name)

  

def forestHouse():
  return


def zoneGraphic(background,centerpiece):
  for i in range(8):
    if i == 6:
      img = Image(Point(0,0),"assets/")

  
windowList = []
leaves = []