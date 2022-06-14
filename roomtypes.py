from graphics import *
from shortcuts import *


def zoneGraphic(win,foreground,centerpiece):
  img = Image(Point(0,0),"assets/backgrounds/")
  for i in range(8):
    if i == 6:
      img = Image(Point(0,0),"assets/sprites/{0}[1}.png".format(centerpiece,i+1)).draw(win)
    else:
      img = Image(Point(0,0),"assets/sprites/{0}{1}.png".format(foreground,i+1)).draw(win)

  
windowList = []
leaves = []