from graphics import *
from room import *
from button import *
from shortcuts import *
from time import *
from hangmethods import *

squareList = [room(0,0)]
previousSquares = [(0,0)]
colours = ["green","green","yellow","blue","magenta"]
biomes = ["grass","tree","ruin","water","home"]
biomeNames = ["plains","forest","ruins","lake"]
startScore = [0]

cP = [0,0]
pos = [0,0]
  
def menu():
  startScore[0] = 0
  
  previousSquares = [(0,0)]
  
  name = GraphWin("Main Menu",520,520)
  
  name.setCoords(-50,-50,50,50)
  
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)
  
  entry = ["Begin Adventure!","Keyboards","Adventure Size","Difficulty","Lists"]
  
  buttons = ["Begin Adventure!","Keyboards","Adventure Size","Difficulty","Lists"]
  
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

def keyboard(keytype,win,keylist):
  
  for i in range(10):
    
    keylist[i] = Button(win,Point(-22.5+5*i,-30),5,5,keytype[i])
    
    keylist[i].activate()
    
  for i in range(10,19):
    
    keylist[i] = Button(win,Point(-20+5*(i-10),-35),5,5,keytype[i])
    
    keylist[i].activate()
    
  for i in range(19,27):
    
    keylist[i] = Button(win,Point(-17.5+5*(i-19),-40),5,5,keytype[i])
    
    keylist[i].activate()

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
  file = open("preferences/modes.txt")
  
  lfile = int(file.read())
  
  squareList = [room(0,0)]
  
  for i in range(1,(lfile+1)*10):
    
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

  
  squareList[len(previousSquares)-1].assignhome()
  
  viewMap()
  
  while True:
    
    k = previousSquares.index(tuple(pos))
    
    direction = displayRoom(squareList[k])
    
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

def backGroundDraw(r,b,win):
  
  img = Image(Point(0,12),"assets/backgrounds/background.png").draw(win)
  
  for i in range(8):
    
    if i == 5:
      
      img = Image(Point(0,12),"assets/sprites/grass6.png").draw(win)
      
      img = Image(Point(0,12),"assets/sprites/{0}{1}.png".format(r,i+1)).draw(win)
      
    else:
      
     img = Image(Point(0,12),"assets/sprites/{0}{1}.png".format(b,i+1)).draw(win)
      
def displayRoom(currentRoom):
  
  r,b = currentRoom.getType()

  beenBool = currentRoom.beenHere()
    
  name = GraphWin("Encounter!",520,520)
  
  name.setCoords(-50,-50,50,50)
  
  options = ["Left","Up","Down","Right","Interect","View Map"]
  
  backGroundDraw(r,b,name)
  
  moveMatrix = [(-1,0),(0,1),(0,-1),(1,0)]
  
  for i in range(len(options)):
    
    options[i] = Button(name,Point(-40+i*16,-45),15,5,options[i])
    
    options[i].activate()

  for i in range(4):
    
    if ((moveMatrix[i][0] + pos[0],moveMatrix[i][1] + pos[1]) not in previousSquares):
      
      options[i].deactivate()

  mainMenu = Button(name,Point(-40,40),10,5,"Quit")
  
  mainMenu.activate()

  
  textBox = Rectangle(Point(-45,-40),Point(45,-25))
  
  textBox.setFill("beige")
  
  textBox.draw(name)

  disScore = Text(Point(40,40),"Your current score is:")
  
  catter = Image(Point(-40,-20),"assets/sprites/miao19.png")
  
  catter.draw(name)

  for i in range(6):
    
    sleep(0.1)
    
    catter.move(0,2*(-1) ** i)

  rVal = biomes.index(b)
  
  if r == "grass":
    
    r = "meadow"
  
  catTalk = Text(Point(0,-33),"This is a {0} in the {1}! Miao Miao\n Solve this {0} puzzle to get coins?".format(r,biomeNames[rVal]))

  if (r == "meadow") or (r == "tree") or (beenBool == True):
    
    options[4].deactivate()
    
    catTalk = Text(Point(0,-33),"This is a {0} in the {1}! Miao Miao\n You cant get coins from this {0}".format(r,biomeNames[rVal]))

  catTalk.draw(name)
  
  point = name.getMouse()
  
  while not mainMenu.clicked(point):
    
    for i in range(len(options)):
      
      if options[i].clicked(point):
        
        if i < 4: 
          
          name.close()
          
          return options[i].getLabel()
          
        elif i == 5:
          
          viewMap()
          
        elif i == 4:
          
          startScore[0] = startScore[0] + interaction(r,b)
          
          currentRoom.been()
          
          options[i].deactivate()
          
    point = name.getMouse()
  
  name.close()
  
  menu()
  
  return "None"
    
def viewMap():
  name, val = windowMake("Map Layout",windowList,leaves)

  MapText = Text(Point(0,30),"Here is the layout for your adventure:").draw(name)
  
  for i in range(len(previousSquares)):
    
    newx,newy = previousSquares[i]
    
    j = Rectangle(Point(2*(2*newx-1),2*(2*newy-1)),Point(2*(2*newx+1),2*(2*newy+1)))
  
    b,c = squareList[i].getType()
    
    co = biomes.index(c)
    
    j.setFill(colours[co])
    
    if squareList[i].beenHere() == True:
      
      j.setFill("grey")
    
    j.draw(name)
    
  currentSquare = Circle(Point(4*pos[0],4*pos[1]),1)
  
  currentSquare.setFill("orange")
  
  currentSquare.draw(name)
  
  point = name.getMouse()
  
  while (not leaves[val].clicked(point)):
    
    point = name.getMouse()
    
  name.close()
  
  return
  
def interaction(r,b):
  name, val = windowMake(r+" encounter!",windowList,leaves)

  file = open("preferences/difficulty.txt","r")
  
  lfile = int(file.read())
  
  backGroundDraw(r,b,name)
  
  keySel = open("preferences/selectedKey.txt","r")
  
  keyboards = open("preferences/keyboards.txt","r")
  
  listType = open("preferences/wordList.txt","r")
  
  keytype = keyboards.readlines()[int(keySel.read())].split(",")
  
  wordInd = int(listType.read()[0:1])
  
  words = ["Countries","Pets","Foods","League"]
  
  word = hangWord("categories/"+words[wordInd]+".txt")

  score = 0
  errors = 0
  puzzle = hangPuzzle(word)
  rect = Rectangle(Point(-40,7),Point(40,0))
  rect.setFill("grey")
  rect.draw(name)
  j = hangDraw(name,puzzle)
  e = errorDraw(name,errors)
  s = sDraw(name,score)

  miao = Image(Point(-40,-20),"assets/sprites/miao19.png")
  miao.draw(name)
  happy = Image(Point(0,30),"assets/sprites/miao21.png")
  
  keylist = []  
  
  for i in range(27):
    keylist.append("key" + str(i))
  keyboard(keytype,name,keylist)

  while (errors < (5-lfile)) and ("".join(puzzle[0:-1]) != word[0:-1]):
    point = name.getMouse()
    for i in range(26):
      if keylist[i].clicked(point):
        
        guess = keylist[i].getLabel()
        
        keylist[i].deactivate()
        
        miao.undraw()
        
        catmove(Point(-40,-20),name,point,5)
        
        catmove(point,name,Point(0,30),9)
        
        if hangIn(guess,word,puzzle) == True:
          
          errors += 0
          
          score += 10
          
          happy.draw(name)
          
          for i in range(4):
            
            sleep(0.1)
            
            happy.move(0,2*(-1) ** i)
            
          happy.undraw()
          
        else:
          
          errors += 1

          score = int(score/2)
          
        catmove(Point(0,30),name,Point(-40,-20),13)
        miao.draw(name)
        

      j.setText("".join(puzzle))
      e.setText("Errors:"+str(errors))
      s.setText("Score:"+str(score))
      
  
  if errors >= (5-lfile):
    for i in range(6):
      sleep(0.1)
      miao.move(2*(-1) ** i,0)
    loseScreen(score,word)
  else:
    for i in range(6):
      sleep(0.1)
      miao.move(0,2*(-1) ** i)
    winScreen(score)
      
  
  keySel.close()
  listType.close()
  keyboards.close()
  name.close()
  
  return score


def catmove(start,win,point,inter):
  cx = start.getX()
  cy = start.getY()

  dx = point.getX() - cx
  dy = point.getY() - cy

  
  for i in range(10):
    
    catList = Image(Point(cx+dx*i/10,cy+dy*i/10),"assets/sprites/miao{0}.png".format(int(i%4+inter)))
    
    catList.draw(win)
    
    sleep(0.1)
    
    catList.undraw()
    
def winScreen(score):
  
  name, val = windowMake("You solved the puzzle!",windowList,leaves)
  
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)

  textBox = Rectangle(Point(30,30),Point(-30,-30))
  
  textBox.setFill("white")
  
  textBox.draw(name)
  
  preText = Text(Point(0,20),"You solved the puzzle!\n From this encounter,\n you have found:")
  
  preText.setSize(20)
  
  preText.draw(name)

  scoreText = Text(Point(0,0),"{0} coins!".format(score))
  
  scoreText.setSize(20)
  
  scoreText.draw(name)
  
  for i in range(score):
    
    scoreText.setText("{0} coins!".format(startScore[0]+i+1))
    
    if i > (score * 3 / 8):
      catter = Image(Point(-25,-25),"assets/sprites/miao{0}.png".format(8-int(i/(score/8)%4)))
      
    else:
      catter = Image(Point(-25,-25),"assets/sprites/miao{0}.png".format(28-int(i/(score/8)%4)))
      
    catter.draw(name)
    
    sleep(0.1)
    
    catter.undraw()
    
  catter = Image(Point(-25,-25),"assets/sprites/miao8.png").draw(name)
  
  ctc = Text(Point(0,-10),"Click anywhere to Continue")
  
  ctc.draw(name)
  
  point = name.getMouse()
  
  name.close()
  
  return
    

def loseScreen(score,word):
  
  name, val = windowMake("You did not solve the puzzle!",windowList,leaves)
  
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)
  
  textBox = Rectangle(Point(30,30),Point(-30,-30))
  
  textBox.setFill("white")
  
  textBox.draw(name)
  
  preText = Text(Point(0,20),"You did not solve the puzzle...")
  
  preText.draw(name)
  
  wordText = Text(Point(0,10),"The word was: {0}".format(word))
  
  for i in range(8):

    if i < 5:
      catter = Image(Point(-25,-25),"assets/sprites/miao{0}.png".format(int(i%4+5)))
      
    else:
      
      catter = Image(Point(-25,-25),"assets/sprites/miao{0}.png".format(int(i%4+25)))
      
    catter.draw(name)
    
    sleep(0.5)
    
    catter.undraw()
    
  catter = Image(Point(-25,-25),"assets/sprites/miao28.png").draw(name)
  
  ctc = Text(Point(0,-10),"Click anywhere to Continue")
  
  ctc.draw(name)
  
  point = name.getMouse()
  
  name.close()
  
  return
  
functionList = [Play,Keyboards,Modes,Difficulty,Lists]
windowList = []
leaves = []

menu()