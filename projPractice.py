import runWorld as rw
import drawWorld as dw
import pygame as pg

################################################################

# This program is an interactive simulation/game. Mario is in the
# center of the screen, and a "goomba" is running toward him in the
# negative x direction. Mario jumps up on each "mouse down" event.
#
# The state of Mario is represented by a tuple (x, delta-x, y, delta-y).
# The first element, x, represents the x coordinate of Mario.
# The second element, delta-x, represents the amount that the
# position changes on each iteration of the simulation loop, in this
# case, Mario's x-position does not change. Y represents the y
# coordinate of Mario, and delta-y represents the change in his y position
#
#
# 
# The initial state of Mario in this program is (width/4,0,height/1.3,0,True), meaning that he
# starts towards the middle of the screen in the x direction, and
# towards the bottom in the y direction, standing still.
#
# Pressing a mouse button down while this simulation run updates Mario's state
# by leaving x unchanged but increasing y. That is, pressing a mouse
# key causes Mario to jump up.
#
# The simulation ends either when Mario successfully jumps over the
# "goomba" and the "goomba" reaches the edge of the screen, meaning
# "Mario Wins". Or, the simulation ends when Mario collides with the
# "Goomba" and "Mario Loses"

################################################################

# Initialize world
name = "Simple Mario Fun. Press the mouse to jump over the objects. Make sure you time it right!"
width = 500
height = 550
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
mario = dw.loadImage("Paper Mario.png")
goomba = dw.loadImage("goomba.png")

# state -> image (IO)
# draw Mario toward the bottom of the screen (height/4) and at the x
# coordinate given by the first component of the state tuple. Draw the
# goomba in the same y coordinate, but further to the right than Mario.
#
def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(mario, (state[0], state[2]))
    dw.draw(goomba, (state[0], state[2]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    newYvalue = state[3]
    newstate = state[4]
    if state[0][4] == False:
       newYvalue += 1
    if newYvalue > 18:
        newYvalue = 0
        newstate = True
    return(state[0]+state[1], state[1], state[2]+state[3], newYvalue, newstate)

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0):
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
        if state[4]:
            return (state[0], state[1], state[2], -18, False)
        return state
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

#
# x pos of g
# y pos of mario
# 
    
# The cat starts at the left, moving right 
initState = ((width/4, 0, height/1.3, 0,True)
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
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
