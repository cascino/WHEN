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
turnCounter = [0]

cP = [0,0]
pos = [0,0]

#def menu(): main menu function. I created a list of functions at the bottom of the file to call from, based on the index of the label of the button that a user clicked. This way, I forwent long conditional statements. 
def menu():
  
  
  startScore[0] = 0
  
  name = GraphWin("Main Menu",520,520)
  
  name.setCoords(-50,-50,50,50)

  
  entry = ["Begin Adventure!","Keyboards","Adventure Size","Difficulty","Lists","Leaderboard"]
  
  buttons = ["Begin Adventure!","Keyboards","Adventure Size","Difficulty","Lists","Leaderboard"]
  
  massButtoner(entry,name)
  
  point = name.getMouse()
  
  while True:
    
    for i in range(len(entry)):
      
      if entry[i].clicked(point):
        
        x = buttons.index(entry[i].getLabel())
        
        name.close()
                
        functionList[x]()
        menu()
        
    point = name.getMouse()
  
#def Keyboards():This function pulls up a screen where users can select their desired keyboard layout. I used my massButtoner function to create buttons from a list.
def Keyboards():
  
  name,val = windowMake("Keyboard Selection",windowList,leaves)
  
  keyboard = ["qwerty","abcdef","dvorak"]
  
  massButtoner(keyboard,name)
  
  prefWriteLoop(keyboard,name,val,"preferences/selectedKey.txt",leaves)
  
  name.close()

  return
  
#def Modes():This function pulls up a screen where users can select their desired adventure size. I used my massButtoner function to create buttons to select from a list.
def Modes():
  
  name, val = windowMake("Map Size",windowList,leaves)
  
  modes = ["Small","Medium","Large","Extra Large","Huge"]
  
  massButtoner(modes,name)
  
  prefWriteLoop(modes,name,val,"preferences/modes.txt",leaves)
  
  name.close()
  
  return

#def keyboard(): This function creates pretty looking keyboards. It iterates through the list of letters in the order from the keyboards file and creates rows based on specified row length.
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

#def Difficulty(): This function pulls up a window for users to select the difficulty from.
def Difficulty():
   
  name, val = windowMake("Difficulty",windowList,leaves)
  
  difficulties = ["Beginner","Intermediate","Advanced","Expert","Prophet"]
  
  massButtoner(difficulties,name)
  
  prefWriteLoop(difficulties,name,val,"preferences/difficulty.txt",leaves)
  
  name.close()
  
  return
  
#def Lists(): This function pulls up a window for users to select their word list from. 
def Lists():
  
  name, val= windowMake("Word Lists",windowList,leaves)
  
  words = ["Countries","Pets","Cities","Pets"]
  
  massButtoner(words,name)
  
  prefWriteLoop(words,name,val,"preferences/wordList.txt",leaves)
  
  name.close()
  
  return
  
#def Play():This function creates the list of rooms that the game will be played in.
def Play():
  
  file = open("preferences/modes.txt")    
  
  lfile = int(file.read())

  
  for i in range(1,(lfile+1)*10):
    
    squareList.append("square"+str(i))
    
    x,y = squareList[i-1].adjacent()
    
    squareList[i] = room(x,y) 
    
    w = (x,y)
    
    if previousSquares.count(w) <1:
      
      previousSquares.append(w)
  
  
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

    elif direction == "Back":
      pos[0] = pos[0] - x
      
      pos[1] = pos[1] - y
    
    else:
      x,y = shift(cP,direction)
    
      cP[0] = x
    
      cP[1] = y
    
      pos[0] = pos[0] + x
    
      pos[1] = pos[1] + y
        
      if not (tuple(pos) in previousSquares):
      
        #Moving the cursor backwards
      
        pos[0] = pos[0] - x
      
        pos[1] = pos[1] - y

    
      
  return 
  
#def shift(): this function accepts the current position and direction in which the cursor representing the player will move in.
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

#def backGroundDraw(): this function draws the background based on the parameters of the room such as the biome and room type
def backGroundDraw(r,b,win):

  bg = Image(Point(0,12),"assets/backgrounds/background.png").draw(win)
  for i in range(8):
    
    if i == 5:
      
      img = Image(Point(0,12),"assets/sprites/grass6.png").draw(win)
      
      img = Image(Point(0,12),"assets/sprites/{0}{1}.png".format(r,i+1)).draw(win)
      
    else:
      
     img = Image(Point(0,12),"assets/sprites/{0}{1}.png".format(b,i+1)).draw(win)

#def displayRoom(): This function displays the current room as well as some buttons for the user to interact with. This is how the user will move around the map and interact with hangman puzzle opportunities. Returns the direction that the player will move in, if any.
def displayRoom(currentRoom):

  r,b = currentRoom.getType()

  if r == "home":

    if leaveCheck() == True:
      finalWinScreen(startScore[0])
      return "None"
      
    else:
      
      return "Back"
      
  beenBool = currentRoom.beenHere()
    
  name = GraphWin("Encounter!",520,520)

  name.setCoords(-50,-50,50,50)
  
  options = ["Left","Up","Down","Right","Interact","View Map"]
  
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

  
  currentScore = Text(Point(38,45),"Score: {0}".format(startScore[0]))
  currentScore.setFill('white')
  
  currentScore.draw(name)
  turns = Text(Point(38,40),"Turns: {0}".format(turnCounter[0]))
  turns.setFill('white')
  
  
  turns.draw(name)
  
  point = name.getMouse()
    
  while not mainMenu.clicked(point):
    
    for i in range(len(options)):
      
      if options[i].clicked(point):
        
        if i < 4: 
          
          name.close()

          turnCounter[0] = turnCounter[0] + 1
          
          return options[i].getLabel()
          
        elif i == 5:
          
          viewMap()
          
        elif i == 4:
          
          startScore[0] = startScore[0] + interaction(r,b)
          
          currentRoom.been()
          
          options[i].deactivate()
          
    point = name.getMouse()
  if leaveCheck() == True:
    cleanUp()
    
    name.close()
  
    menu()
  
    return "None"

  else:
    
    name.close()
    return "Back"

#def viewMap(): this function displays the map layout based on the list of rooms that were generated. also contains a how to button that calls the how to function.
def viewMap():
  
  name, val = windowMake("Map Layout",windowList,leaves)

  MapText = Text(Point(0,40),"Here is the layout for your adventure:").draw(name)
  
  for i in range(len(previousSquares)):
    
    newx,newy = previousSquares[i]
    
    j = Rectangle(Point(2*(2*newx-1),2*(2*newy-1)),Point(2*(2*newx+1),2*(2*newy+1)))
  
    b,c = squareList[i].getType()
    
    co = biomes.index(c)
    
    j.setFill(colours[co])
    
    if squareList[i].beenHere() == True:
      
      j.setFill("grey")

    elif squareList[i].getType()[0] == "home":
      j.setFill("magenta")
    j.draw(name)
    
  currentSquare = Circle(Point(4*pos[0],4*pos[1]),1)
  
  currentSquare.setFill("orange")
  
  currentSquare.draw(name)

  howButton = Button(name,Point(-40,30),15,5,"How to")
  howButton.activate()
  
  point = name.getMouse()
  
  while (not leaves[val].clicked(point)):
    if howButton.clicked(point):
      howTo()
    point = name.getMouse()
    
  name.close()
  
  return
#def interaction(): this function handles the actual hangman puzzle gameplay and puts together the hangman functions from hangmethods.py
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
#def catmove(): this function handles moving the cat around for the cat animation. Takes the difference in the point's x and y values and splits it into 10 frames, moving the cat each time by drawing and undrawing cat sprites. It also cycles through a walking animation.
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

#def winscreen(): the screen that a player will see when they complete a hangman puzzle successfully. also contains a little animation
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
    
#def loseScreen(): the screen that a player will see when they do not successfully complete a hangman puzzle. also contains a little animation
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

#def cleanUp(): this function cleans up the lists of rooms and player data from the current adventure, making it clean for the next adventure.
def cleanUp():
  
  squareList.clear()
  
  previousSquares.clear()
  
  squareList.append(room(0,0))
  
  previousSquares.append((0,0))
  
  pos[0],pos[1] = 0,0
  
  cP[0],cP[1] = 0,0

#def finalWinScreen(): this function is the final screen that a player sees once they have reached herberts home.
def finalWinScreen(score):
  
  name, val = windowMake("Herbert Found His Home!",windowList,leaves)
  
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)

  textBox = Rectangle(Point(30,30),Point(-30,-30))
  
  textBox.setFill("white")
  
  textBox.draw(name)
  
  preText = Text(Point(0,10),"You found Herbert's Home!\n On this adventure,\n you have travelled to:\n {0} Regions!\n\n Your final score is:\n".format(turnCounter[0]))
  
  preText.setSize(15)
  
  preText.draw(name)

  scoreText = Text(Point(0,-15),"{0} coins!".format(score))
  
  scoreText.setSize(15)
  
  scoreText.draw(name)
  
  for i in range(score):
    
    scoreText.setText("{0} coins!".format(0+i+1))
    
    if i > (score * 3 / 8):
      catter = Image(Point(-25,-25),"assets/sprites/miao{0}.png".format(8-int(i/(score/8)%4)))
      
    else:
      catter = Image(Point(-25,-25),"assets/sprites/miao{0}.png".format(28-int(i/(score/8)%4)))
      
    catter.draw(name)
    
    sleep(0.1)
    
    catter.undraw()
    
  catter = Image(Point(-25,-25),"assets/sprites/miao8.png").draw(name)
  
  ctc = Text(Point(0,-20),"Click anywhere to Continue")
  
  ctc.draw(name)
  
  point = name.getMouse()
  
  name.close()
  
  writeLeaderBoard(score)

#def howTo(): text that outlines how the player should play. pulls up a separate window from the viewmap screen.
def howTo():
  
  name, val = windowMake("How To!",windowList,leaves)

  instructions = Image(Point(0,30),"assets/backgrounds/instructions.png").draw(name)
  howtext = Text(Point(0,0),"Your goal is to find Herbert's Home!\nUse the map to guide you towards the magenta square, which\n marks Herbert's Humble Abode! Yellow squares mark ruins,\n blue squares mark oceans and green squares mark plains.\n\n However, before returning home, Herbert would\n like to collect some coins!\n\nHelp Herbert solve chest and house puzzles to collect coins \nfor his coin collection! You may only collect coins from one \nregion once, and exhausted regions are marked as \ngrey on your map.").draw(name)

  point = name.getMouse()
  
  while not leaves[val].clicked(point):
    point = name.getMouse()

  name.close()

#def viewLeaderBoard(): pulls up the leaderboard from the leaderboard file and also sorts it to show the top scoring usernames
def viewLeaderBoard():
  file = open("leaderboard.txt","r")
  listFile = file.readlines()

  
  name, val = windowMake("View Leaderboard",windowList,leaves)
  sorteds = []
  scoreList = []
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)
  title = Image(Point(0,30),"assets/backgrounds/highScores.png").draw(name)
  textBox = Rectangle(Point(30,20),Point(-30,-32))
  
  leaves[val].unMake()
  leaves[val].reMake(name)
  textBox.setFill("white")
  
  textBox.draw(name)
  
  for i in range(len(listFile)):
    j = listFile[i].split("-")
    
    scoreList.append(int(j[1]))
  newScores = sorted(scoreList)
  
  for i in range(len(newScores)):
    k = scoreList.index(newScores[i])
    sorteds.append(listFile[k])
    listFile.remove(listFile[k])
    scoreList.remove(newScores[i])
    
  for i in range(10):
    scoreEntry = Text(Point(0,15-5*i),"{0}. {1}".format(i+1,sorteds[-i-1])).draw(name)

  point = name.getMouse()

  while not leaves[val].clicked(point):
    point = name.getMouse()

  name.close()
  file.close()
  return
#def writeLeaderBoard(): a function that writes the users username and their score to the leaderboard.
def writeLeaderBoard(score):

  file = open("leaderboard.txt","a")

  keyboards = open("preferences/keyboards.txt","r")

  keySel = open("preferences/selectedKey.txt","r")
  
  name, val = windowMake("Enter Your Name",windowList,leaves)
  
  keytype = keyboards.readlines()[int(keySel.read())].split(",")
  
  username = ""

  usernameDraw = Text(Point(0,0),username)
  usernameDraw.draw(name)

  keylist = []
  
  for i in range(27):
    
    keylist.append("key" + str(i))
    
  keyboard(keytype,name,keylist)

  point = name.getMouse()
  
  while not leaves[val].clicked(point):
    
    for i in range(27):
      
      if keylist[i].clicked(point):

        letter = keylist[i].getLabel()

        if letter == "<":
          
          username = username[0:-2]
          
          usernameDraw.setText(username)
        else:
          
          username = username + letter
          
          usernameDraw.setText(username)

    point = name.getMouse()

  file.write("{0}-{1}\n".format(username,score))
  
  keyboards.close()
  keySel.close()
  return

#def leaveCheck(): a function that asks the user if they are sure if they want to leave the game through either the quit button or going to herberts home.
def leaveCheck():

  name, val = windowMake("Enter Your Name",windowList,leaves)
  leaves[val].deactivate()
  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(name)
  title = Image(Point(0,30),"assets/backgrounds/attention.png").draw(name)
  
  textBox = Rectangle(Point(30,20),Point(-30,-40))
  
  textBox.setFill("white")
  
  textBox.draw(name)

  preText = Text(Point(0,10),"Are you sure you \nWant to terminate\n this adventure?\nHerbert wants more coins...")
  preText.setSize(15)
  preText.draw(name)

  yesButton = Button(name,Point(20,-15),10,5,"Yes")
  yesButton.activate()
  noButton = Button(name,Point(-20,-15),10,5,"No")
  noButton.activate()  

  point = name.getMouse()
  while True:
    if yesButton.clicked(point):
      name.close()
      return True
    elif noButton.clicked(point):
      name.close()
      return False
    else:
      point = name.getMouse()
  
functionList = [Play,Keyboards,Modes,Difficulty,Lists,viewLeaderBoard]
windowList = []
leaves = []


menu()