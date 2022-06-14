from graphics import *
from room import *
from button import *
from shortcuts import *
from roomtypes import *

def menu():
  name, val = windowMake("Main Menu",windowList,leaves)
  leaves[val].deactivate()
  zoneGraphic(name,"tree","house")
  entry = ["Play","Keyboards","Modes","Difficulty","Lists","Leaderboard","HowTo"]
  buttons = ["Play","Keyboards","Modes","Difficulty","Lists","Leaderboard","HowTo"]
  massButtoner(entry,name)
  point = name.getMouse()
  while True:
    for i in range(5):
      if entry[i].clicked(point):
        x = buttons.index(entry[i].getLabel())
        name.close()
        functionList[x]()
    point = name.getMouse()


def gameWindow():
  name, val = windowMake("View Options",windowList,leaves)
  viewActions = ["View Map","Inventory","Help",]
  buttons = ["View Map","Inventory","Help",]
  massButtoner(viewActions,name)
  
def genMap():
  name, val = windowMake("Map of Forest",windowList,leaves)

  #Creating the first room and tuple of room
  squareList = [room(0,0)]
  previousSquares = [(0,0)]
  l = Rectangle(Point(1,1),Point(-1,-1))
  l.setFill("black")


  viewRoom = Button(name,Point(40,0),10,4,"View")
  viewRoom.activate()
  
  #Button list 
  buttons = ["Up","Down","Left","Right"]
  for i in range(len(buttons)):
    buttons[i] = Button(name,Point(40,40-i*10),10,4,buttons[i])
    buttons[i].activate()

  #Generating the list of squareList
  for i in range(1,30):
    squareList.append("square"+str(i))
    x,y = squareList[i-1].adjacent()
    squareList[i] = room(x,y) 
    w = (x,y)
    if previousSquares.count(w) <1:
      previousSquares.append(w)
  

  #remaking squareList with valid previousSquares list
  for i in range(len(previousSquares)):
    newx,newy = previousSquares[i]
    squareList[i] = room(newx,newy)
    squareList[i].roomassign()
    r,c = squareList[i].getType()
    

    
    
    j = Rectangle(Point(newx-2,newy-2),Point(newx+2,newy+2))
    colours = ["green","green","yellow","blue"]
    biomes = ["grass","tree","ruin","water"]
    co = biomes.index(c)
    j.setFill(colours[co])
    j.draw(name)
    
  cP = [0,0]
  pos = [0,0]
  flag = True
  l.draw(name)

  j = ["Up"]
  point = name.getMouse()
  while flag == True:
    k = previousSquares.index(tuple(pos))
    
    if viewRoom.clicked(point):
      squareList[k].displayRoom()
      
      
      
      
      
    for i in range(len(buttons)):
      if buttons[i].clicked(point):
        j[0] = buttons[i].getLabel()
        
        x,y = shift(cP,j)
        cP[0] = x
        cP[1] = y
        pos[0] = pos[0] + x
        pos[1] = pos[1] + y
        
        if tuple(pos) in previousSquares:
          l.move(x,y)
          #Debugging line for info
          print(squareList[previousSquares.index(tuple(pos))].getType())
          print(squareList[previousSquares.index(tuple(pos))].getCoords())
          #print("Index is",previousSquares.index(tuple(pos)))
        else:
          #Moving the cursor backwards
          pos[0] = pos[0] - x
          pos[1] = pos[1] - y
        
    point = name.getMouse()  
  

#Move the "cursor"
def shift(currentPos,list):
  if list[0] == "Up":
    return 0,4
  elif list[0] == "Left":
    return -4,0
  elif list[0] == "Down":
    return 0,-4
  elif list[0] == "Right":
    return 4,0




genMap()

functionList = []
windowList = []
leaves = []


