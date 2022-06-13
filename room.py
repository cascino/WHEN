from random import *
from roomtypes import *

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
    roomList = ["a","b","c","d","e","f","g"]
    randroom = randint(0,len(roomList)-1)
    self.roomtype = roomList[randroom]

  def getType(self):
    return(self.roomtype)
    
    

  
    
    