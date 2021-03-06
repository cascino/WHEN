from graphics import *
from button import *

#creates a window and a leave button
def windowMake(windowName,list,leaves):
  
  list.append(windowName)
  
  leaves.append(windowName)
  
  lval = leaves.index(windowName)
  
  val = list.index(windowName)
  
  list[val] = GraphWin(windowName,520,520)
  
  list[val].setCoords(-50,-50,50,50)
  
  leaves[lval] = Button(list[val],Point(-40,40),10,4,"Ok")
  
  leaves[lval].activate()
  
  return list[val], val

#creates a bunch of buttons based on a list all at once
def massButtoner(list,win):

  bg = Image(Point(0,0),"assets/backgrounds/bg.png").draw(win)

  cat = Image(Point(-30,-20),"assets/sprites/miao30.png").draw(win)

  title = Image(Point(0,30),"assets/backgrounds/title.png").draw(win)
  for i in range(len(list)):
    list[i] = Button(win,Point(0,10-i*10),30,5,list[i])
    list[i].activate()

#writes a preference to a file
def prefWriteLoop(list,win,val,file,leaves):
  point = Point(-50,-50)
  while not leaves[val].clicked(point):
    for i in range(len(list)):
      if list[i].clicked(point):
        file = open(file,"w")
        file.write(str(i))
        file.close()
        win.close()
        return
    point = win.getMouse()

