from random import *
from graphics import *

#creates a room class that has its coordinates, its room type, which biome it is from, and if the player has interacted already with the room. 
class room:
  def __init__(self,xPos,yPos):
    
    self.xPos = xPos
    self.yPos = yPos
    
    self.roomtype = "z"
    self.beenBool = False

  #finds an adjacent room by shuffling two lists together. One coordinate will always be zero, so it is adjacent
  def adjacent(self):
    a = self.xPos
    b = self.yPos
    
    rbin = [0,1]
    rmove = [-1,1]
    
    shuffle(rbin)
    shuffle(rmove)
    newList = [int(rbin[0])*rmove[0],rbin[1]*rmove[1]]
    
    return(a+newList[0],b+newList[1])
    
  #gets the coordinates of a room.
  def getCoords(self):
    return self.xPos,self.yPos

  #assigns the room a room type and a biome type based on the random entry of a list.
  def roomassign(self):
    roomList = ["house","chest","grass","tree"]
    biomeList = ["grass","tree","ruin","water",]
    randroom = randint(0,len(roomList)-1)
    randbiome = randint(0,len(biomeList)-1)
    self.roomtype = roomList[randroom]
    self.biometype = biomeList[randbiome]

  #gets the typs of the room and biome
  def getType(self):
    return(self.roomtype,self.biometype)

  #gets if the player has interacted with the room before
  def beenHere(self):
    return self.beenBool

  #sets the bool of been to true, i.e., the player has interacted with the room before
  def been(self):
    self.beenBool = True

  #assigns the room to "home", where herbert will go and the ending room that terminates the game.
  def assignhome(self):
    self.roomtype = "home"

  
    
    
    

  
    
    