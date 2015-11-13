# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw

###############################################################################

# Initialize world
name = "Cat Go!"
width = 500
height = 500
rw.newDisplay(width, height, name)

###############################################################################

# Display the state by drawing a cat at the x coordinate
myimage = dw.loadImage("cat.bmp")

# state -> image (IO) 
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (stage, width/2))

draw(surf, loc)
