import runWorld as rw
import drawWorld as dw
import pygame as pg

################################################################

# This program is an interactive simulation/game. Mario starts in the
# middle of the screen, and every time the mouse is clicked, he jumps
# upward. A goomba is moving left across the screen. The object of the
# game is to avoid the goomba by jumping over it.  
#
# The state of the goomba is represented by a tuple (xpos, delta-xpos,ypos,delta-ypos,jumping).
# The first element, xpos, represents the x-coordinate of the
# goomba.
# The second element, delta-xpos, represents the amount that the
# position changes on each iteration of the simulation loop. The third
# element, ypos, represents the y-coordinate of the goomba.The fourth
# element, delta-ypos, represents the amount the y-coordinate changes
# on each iteration of the simulation loop. The fourth element,
# jumping represents whether the object is jumping or not.

#The same principles are applied to the mario tuple.

# 
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation runs 
# The simulation ends when the goomba leaves the screen. 

################################################################

# Initialize world
name = "Simple Mario Fun. Press the mouse to jump over the objects. Make sure you time it right!"
width = 1000
height = 550
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
mario = dw.loadImage("Paper Mario.png")
goomba = dw.loadImage("goomba.png")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(mario, (state[0][0], state[0][2]))
    dw.draw(goomba, (state[1][0], state[1][2]))
    

################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    return (updateMario(state[0]), updateGoomba(state[1]))

def updateMario(state):
    newYvalue = state[3]
    newstate = state[4]
    if state[4] == False:
       newYvalue += 1
    if newYvalue > 26:
        newYvalue = 0
        newstate = True
    return((state[0], state[1], state[2]+state[3], newYvalue, newstate))

def updateGoomba(state):
    return((state[0]+state[1], state[1], state[2], state[3]))

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[1][0] > width or state[1][0] < 0):
        return True
    else:
        return False

################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if state[0][4]:
            return (((state[0][0], state[0][1], state[0][2], -26, False), (state[1][0],  state[1][1], state[1][2], state[1][3])))
        return state
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# x pos of g
# y pos of mario
# 
    
# Mario starts off-center to the left, standing still. The Goomba
# starts off on the right side of the screen, moving to the left, toward Mario. 
initState = ((450, 0, 420, 0, True), (900, -4, 465, 0, False))

# initState = (mario_y, mario_is_jumping, goomba_x, .., ..)
# state[0] = mario_y, state[1] = mario_is_jumpin

# initState = ((mario_y, mario_is_jumping), (goomba_x))
# initState = (marioState, goombaState)
# state[0][0] = mario_y, state[1][0] = goomba_x
# def updateState(state):
#    return (updateMario(state[0]), updateGoomba(state[1]))
 
# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
