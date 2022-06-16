from graphics import *
from room import *
from button import *
from shortcuts import *
from time import *



squareList = [room(0,0)]
previousSquares = [(0,0)]
colours = ["green","green","yellow","blue"]
biomes = ["grass","tree","ruin","water"]
biomeNames = ["plains","forest","ruins","lake"]

cP = [0,0]
pos = [0,0]

def menu():
  
  name, val = windowMake("Main Menu",windowList,leaves)
  leaves[val].deactivate()
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)
  
  entry = ["Play","Keyboards","Modes","Difficulty","Lists"]
  buttons = ["Play","Keyboards","Modes","Difficulty","Lists"]
  massButtoner(entry,name)
  point = name.getMouse()
  while True:
    for i in range(len(entry)):
      if entry[i].clicked(point):
        x = buttons.index(entry[i].getLabel())
        name.close()
        print(x)
        functionList[x]()
    point = name.getMouse()

def Keyboards():
  name,val = windowMake("Keyboard Selection",windowList,leaves)
  keyboard = ["qwerty","abcdef","dvorak"]
  massButtoner(keyboard,name)
  prefWriteLoop(keyboard,name,val,"preferences/selectedKey.txt",leaves)
  name.close()
  menu()
  return

def Modes():
  name, val = windowMake("Map Size",windowList,leaves)
  modes = ["Small","Medium","Large","Extra Large","Huge"]
  massButtoner(modes,name)
  prefWriteLoop(modes,name,val,"preferences/modes.txt",leaves)
  name.close()
  menu()
  return

def Difficulty():
  name, val = windowMake("Difficulty",windowList,leaves)
  difficulties = ["Beginner","Intermediate","Advanced","Expert","Prophet"]
  massButtoner(difficulties,name)
  prefWriteLoop(difficulties,name,val,"preferences/difficulty.txt",leaves)
  name.close()
  menu()
  return

def Lists():
  name, val= windowMake("Word Lists",windowList,leaves)
  words = ["Countries","Pets","Foods","League"]
  massButtoner(words,name)
  prefWriteLoop(words,name,val,"preferences/wordList.txt",leaves)
  name.close()
  menu()
  return

def Play():
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



  while True:
    k = previousSquares.index(tuple(pos))
    w,z = squareList[k].getType()
    
    direction = displayRoom(w,z)
    if direction == "None":
      return
    
    x,y = shift(cP,direction)
    cP[0] = x
    cP[1] = y
    pos[0] = pos[0] + x
    pos[1] = pos[1] + y
        
    if not (tuple(pos) in previousSquares):
      #Moving the cursor backwards
      pos[0] = pos[0] - x
      pos[1] = pos[1] - y
        
#Move the "cursor"
def shift(currentPos,list):
  if list == "Up":
    return 0,1
  elif list == "Left":
    return -1,0
  elif list == "Down":
    return 0,-1
  elif list == "Right":
    return 1,0
  elif list == "None":
    return 0,0

def displayRoom(r,b):
  name = GraphWin("Encounter!",520,520)
  name.setCoords(-50,-50,50,50)
  
  options = ["Left","Up","Down","Right","Interect","View Map"]
  
  img = Image(Point(0,12),"assets/backgrounds/background.png").draw(name)
  
  for i in range(8):
    if i == 5:
      img = Image(Point(0,12),"assets/sprites/grass6.png").draw(name)
      img = Image(Point(0,12),"assets/sprites/{0}{1}.png".format(r,i+1)).draw(name)
    else:
     img = Image(Point(0,12),"assets/sprites/{0}{1}.png".format(b,i+1)).draw(name)
  moveMatrix = [(-1,0),(0,1),(0,-1),(1,0)]
  
  for i in range(len(options)):
    options[i] = Button(name,Point(-40+i*16,-45),15,5,options[i])
    options[i].activate()

  for i in range(4):
    if ((moveMatrix[i][0] + pos[0],moveMatrix[i][1] + pos[1]) not in previousSquares):
      options[i].deactivate()

  mainMenu = Button(name,Point(-40,40),10,5,"Menu")
  mainMenu.activate()

  if (r == "grass") or (r == "tree"):
    options[4].deactivate()
  textBox = Rectangle(Point(-45,-40),Point(45,-25))
  textBox.setFill("beige")
  textBox.draw(name)
  catter = Image(Point(-40,-20),"assets/sprites/miao.png")
  catter.draw(name)

  for i in range(6):
    sleep(0.1)
    catter.move(0,2*(-1) ** i)

  rVal = biomes.index(b)
  if r == "grass":
    r = "meadow"
  catTalk = Text(Point(0,-30),"This is a {0} in the {1}! Miao Miao".format(r,biomeNames[rVal])).draw(name)
  
  point = name.getMouse()
  while not mainMenu.clicked(point):
    for i in range(len(options)):
      if options[i].clicked(point):
        if i < 4: 
          name.close()
          return options[i].getLabel()
        elif i == 5:
          viewMap()
       # elif i == 4:

    point = name.getMouse()
  name.close()
  menu()
  return "None"
    
def viewMap():
  name, val = windowMake("Map Layout",windowList,leaves)
  
  for i in range(len(previousSquares)):
    newx,newy = previousSquares[i]
    j = Rectangle(Point(2*(2*newx-1),2*(2*newy-1)),Point(2*(2*newx+1),2*(2*newy+1)))
  
    b,c = squareList[i].getType()
    co = biomes.index(c)
    j.setFill(colours[co]) 
    j.draw(name)
    
  currentSquare = Circle(Point(4*pos[0],4*pos[1]),1)
  currentSquare.setFill("orange")
  currentSquare.draw(name)
  
  point = name.getMouse()
  while (not leaves[val].clicked(point)):
    point = name.getMouse()
  name.close()
  
  return
  
functionList = [Play,Keyboards,Modes,Difficulty,Lists]




windowList = []
leaves = []

menu()
