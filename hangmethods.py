from graphics import GraphWin, Point, Text, Rectangle
from random import randrange
from button import Button

#generates the word from the chosen word list
def hangWord(title):

  list = open(title,"r")
  
  listread = list.readlines()
  
  wordIndex = randrange(0,len(listread)-1)

  word = listread[wordIndex]
  
  list.close()
  
  return(word)

#generates the puzzle from the word 
def hangPuzzle(word):
  
  puzzle = []
  
  for i in word:
    if 96 < ord(i.lower()) < 123:

      puzzle.append("*")

    else:

      puzzle.append(i)

  return (puzzle)

#checks if the word is in the puzzle and updates the puzzle
def hangIn(guess, word, puzzle):

  flag = False

  for i in range(len(word)):

    if guess == word[i].lower():

      puzzle[i] = word[i]

      flag = True

  return flag

#draws the word on the screen 
def hangDraw(win,puzzle):
  stars = "".join(puzzle)
  
  currentword = Text(Point(0,0),stars)
  
  currentword.setSize(15)
  currentword.draw(win)
  return(currentword)

#draws the error counter on the screen
def errorDraw(win,errors):
  eDraw = Text(Point(38,40),"Errors:"+str(errors))
  eDraw.setFill('white')
  eDraw.draw(win)
  return(eDraw)

#draws the score on the screen
def sDraw(win,score):
  sDraw = Text(Point(38,45),"Score"+str(score))
  sDraw.setFill('white')
  sDraw.draw(win)
  return(sDraw)

