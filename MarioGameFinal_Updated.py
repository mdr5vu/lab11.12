import runWorld as rw
import drawWorld as dw
import pygame as pg
from numpy import absolute

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
# Pressing a mouse button down while this simulation runs
# The simulation ends when the goomba leaves the screen.

################################################################

# Initialize world
name = "Simple Mario Fun. Press the mouse to jump over the objects. Make sure you time it right!"
width = 1000
height = 550
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing mario and the goomba at that x coordinate
mario = dw.loadImage("Paper Mario.png")
goomba = dw.loadImage("goomba.png")

def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(mario, (state.mario[0], state.mario[2]))
    dw.draw(goomba, (state.goomba[0], state.goomba[2]))
   

################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).


class State:
    mario = (450, 0, 420, 0 , True)
    goomba = (900, -4, 465, 0, False)
   
# state -> state
def updateState(state):
    state.mario = updateMario(state.mario)
    state.goomba = updateGoomba(state.goomba)
    return state

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
    newXV = state[1]
    if state[0] < 5 or state[0] > 995:
        newXV = newXV * -1.2
    return((state[0]+newXV, newXV, state[2], state[3]))

################################################################

# Terminate the simulation when the mario and goomba touch.
# state -> bool
def endState(state):
    if (absolute(state.mario[0]-state.goomba[0]) < 80 and absolute(state.mario[2]-state.goomba[2]) < 80):
        return True
    else:
        return False

################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with mario jumping each time the mouse is
# clicked. THe game is to keep mario alive by avoiding the goomba.
#
# state -> event -> state
#
def handleEvent(state, event): 
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if state.mario[4]:
            state.mario = (state.mario[0], state.mario[1], state.mario[2], -26, False)
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
initState = State()

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
