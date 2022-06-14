from random import *
from roomtypes import *
from graphics import *

class room:
  def __init__(self,xPos,yPos):
    
    self.xPos = xPos
    self.yPos = yPos
    self.roomtype = "z"
    
  def adjacent(self):
    a = self.xPos
    b = self.yPos
    
    rbin = [0,2]
    rmove = [-2,2]
    shuffle(rbin)
    shuffle(rmove)
    newList = [int(rbin[0])*rmove[0],rbin[1]*rmove[1]]
    
    return(a+newList[0],b+newList[1])
    
    
  def getCoords(self):
    return self.xPos,self.yPos

  def roomassign(self):
    roomList = ["house","chest",]
    biomeList = ["grass","tree","ruin","water",]
    randroom = randint(0,len(roomList)-1)
    randbiome = randint(0,len(biomeList)-1)
    self.roomtype = roomList[randroom]
    self.biometype = biomeList[randbiome]

  def getType(self):
    return(self.roomtype,self.biometype)

  def displayRoom(self):
    window = GraphWin("Encounter!",520,520)
    window.setCoords(-50,-50,50,50)
    img = Image(Point(0,10),"assets/backgrounds/background.png").draw(window)



    
    for i in range(8):
      if i == 5:
        img = Image(Point(0,10),"assets/sprites/grass6.png").draw(window)
        img = Image(Point(0,10),"assets/sprites/{0}{1}.png".format(self.roomtype,i+1)).draw(window)
      else:
        img = Image(Point(0,10),"assets/sprites/{0}{1}.png".format(self.biometype,i+1)).draw(window)
    
    
    

  
    
    