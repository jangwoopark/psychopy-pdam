#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.73.02), January 30, 2012, at 01:15
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
import numpy as np  # whole numpy lib is available, pre-pend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os #handy system and path functions
from psychopy import core, data, event, logging, visual, gui
from psychopy.constants import *

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[-1,-1,-1], colorSpace=u'rgb')

#Initialise components for routine:FIX
FIXClock=core.Clock()
text=visual.TextStim(win=win, ori=0, name='text',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for routine:PD
PDClock=core.Clock()
Cue=visual.TextStim(win=win, ori=0, name='Cue',
    text="      You are now playing \nthe PRISONER'S DILEMMA \n   game with your partner",
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
game=visual.PatchStim(win=win, name='game',
    tex='Screenshot.png', mask=None,
    ori=0, pos=[0, 0], size=[2,2], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512, interpolate=False, depth=-1.0)
choose=visual.TextStim(win=win, ori=0, name='choose',
    text='Do you cooperate or default?',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
wait=visual.TextStim(win=win, ori=0, name='wait',
    text='Wait',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
feed=visual.TextStim(win=win, ori=0, name='feed',
    text='Your partner chose to',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
feed_b=visual.TextStim(win=win, ori=0, name='feed_b',
    text='\n\n(cooperate or default)',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-6.0)

#Initialise components for routine:FIX
FIXClock=core.Clock()
text=visual.TextStim(win=win, ori=0, name='text',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for routine:PDAS
PDASClock=core.Clock()
Cue_2=visual.TextStim(win=win, ori=0, name='Cue_2',
    text="      You are now playing \nthe PRISONER'S DILEMMA\n  APPROVAL STAGE game \n         with your partner",
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
game_2=visual.PatchStim(win=win, name='game_2',
    tex='Screenshot.png', mask=None,
    ori=0, pos=[0, 0], size=[2, 2], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512, interpolate=False, depth=-1.0)
choose_2=visual.TextStim(win=win, ori=0, name='choose_2',
    text='Do you cooperate or default?',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
wait_2=visual.TextStim(win=win, ori=0, name='wait_2',
    text='Wait',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
feed_2=visual.TextStim(win=win, ori=0, name='feed_2',
    text='Your partner chose to',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
feed_b_2=visual.TextStim(win=win, ori=0, name='feed_b_2',
    text='\n\n(cooperate or default)',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-6.0)
AS=visual.TextStim(win=win, ori=0, name='AS',
    text='Do you approve or disapprove?',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
feed_3=visual.TextStim(win=win, ori=0, name='feed_3',
    text='Your partner chose to',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
feed_b_3=visual.TextStim(win=win, ori=0, name='feed_b_3',
    text='\n\n(approve or disapprove)',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

#Start of routine FIX
t=0; FIXClock.reset()
frameN=-1

#update component parameters for each repeat
#keep track of which have finished
FIXComponents=[]#to keep track of which have finished
FIXComponents.append(text)
for thisComponent in FIXComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=FIXClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*text* updates
    if t>=0.0 and text.status==NOT_STARTED:
        #keep track of start time/frame for later
        text.tStart=t#underestimates by a little under one frame
        text.frameNStart=frameN#exact frame index
        text.setAutoDraw(True)
    elif text.status==STARTED and t>=(0.0+6.0):
        text.setAutoDraw(False)
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in FIXComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine FIX
for thisComponent in FIXComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#Start of routine PD
t=0; PDClock.reset()
frameN=-1

#update component parameters for each repeat
key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
key_resp.status=NOT_STARTED
#keep track of which have finished
PDComponents=[]#to keep track of which have finished
PDComponents.append(Cue)
PDComponents.append(game)
PDComponents.append(choose)
PDComponents.append(key_resp)
PDComponents.append(wait)
PDComponents.append(feed)
PDComponents.append(feed_b)
for thisComponent in PDComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=PDClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*Cue* updates
    if t>=0.0 and Cue.status==NOT_STARTED:
        #keep track of start time/frame for later
        Cue.tStart=t#underestimates by a little under one frame
        Cue.frameNStart=frameN#exact frame index
        Cue.setAutoDraw(True)
    elif Cue.status==STARTED and t>=(0.0+4.0):
        Cue.setAutoDraw(False)
    
    #*game* updates
    if t>=4.0 and game.status==NOT_STARTED:
        #keep track of start time/frame for later
        game.tStart=t#underestimates by a little under one frame
        game.frameNStart=frameN#exact frame index
        game.setAutoDraw(True)
    elif game.status==STARTED and t>=(4.0+4.0):
        game.setAutoDraw(False)
    
    #*choose* updates
    if t>=8.0 and choose.status==NOT_STARTED:
        #keep track of start time/frame for later
        choose.tStart=t#underestimates by a little under one frame
        choose.frameNStart=frameN#exact frame index
        choose.setAutoDraw(True)
    elif choose.status==STARTED and t>=(8.0+4.0):
        choose.setAutoDraw(False)
    
    #*key_resp* updates
    if t>=8.0 and key_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
        key_resp.tStart=t#underestimates by a little under one frame
        key_resp.frameNStart=frameN#exact frame index
        key_resp.status=STARTED
        #keyboard checking is just starting
        key_resp.clock.reset() # now t=0
    elif key_resp.status==STARTED and t>=(8.0+4.0):
        key_resp.status=STOPPED
    if key_resp.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['y', 'n'])
        if len(theseKeys)>0:#at least one key was pressed
            key_resp.keys.extend(theseKeys)#storing all keys
            key_resp.rt.append(key_resp.clock.getTime())
    
    #*wait* updates
    if t>=12.0 and wait.status==NOT_STARTED:
        #keep track of start time/frame for later
        wait.tStart=t#underestimates by a little under one frame
        wait.frameNStart=frameN#exact frame index
        wait.setAutoDraw(True)
    elif wait.status==STARTED and t>=(12.0+2.0):
        wait.setAutoDraw(False)
    
    #*feed* updates
    if t>=14.0 and feed.status==NOT_STARTED:
        #keep track of start time/frame for later
        feed.tStart=t#underestimates by a little under one frame
        feed.frameNStart=frameN#exact frame index
        feed.setAutoDraw(True)
    elif feed.status==STARTED and t>=(14.0+2.0):
        feed.setAutoDraw(False)
    
    #*feed_b* updates
    if t>=14.0 and feed_b.status==NOT_STARTED:
        #keep track of start time/frame for later
        feed_b.tStart=t#underestimates by a little under one frame
        feed_b.frameNStart=frameN#exact frame index
        feed_b.setAutoDraw(True)
    elif feed_b.status==STARTED and t>=(14.0+2.0):
        feed_b.setAutoDraw(False)
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in PDComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine PD
for thisComponent in PDComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#Start of routine FIX
t=0; FIXClock.reset()
frameN=-1

#update component parameters for each repeat
#keep track of which have finished
FIXComponents=[]#to keep track of which have finished
FIXComponents.append(text)
for thisComponent in FIXComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=FIXClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*text* updates
    if t>=0.0 and text.status==NOT_STARTED:
        #keep track of start time/frame for later
        text.tStart=t#underestimates by a little under one frame
        text.frameNStart=frameN#exact frame index
        text.setAutoDraw(True)
    elif text.status==STARTED and t>=(0.0+6.0):
        text.setAutoDraw(False)
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in FIXComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine FIX
for thisComponent in FIXComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#Start of routine PDAS
t=0; PDASClock.reset()
frameN=-1

#update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse() #create an object of type KeyResponse
key_resp_2.status=NOT_STARTED
key_resp_3 = event.BuilderKeyResponse() #create an object of type KeyResponse
key_resp_3.status=NOT_STARTED
#keep track of which have finished
PDASComponents=[]#to keep track of which have finished
PDASComponents.append(Cue_2)
PDASComponents.append(game_2)
PDASComponents.append(choose_2)
PDASComponents.append(key_resp_2)
PDASComponents.append(wait_2)
PDASComponents.append(feed_2)
PDASComponents.append(feed_b_2)
PDASComponents.append(AS)
PDASComponents.append(key_resp_3)
PDASComponents.append(feed_3)
PDASComponents.append(feed_b_3)
for thisComponent in PDASComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=PDASClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*Cue_2* updates
    if t>=0.0 and Cue_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        Cue_2.tStart=t#underestimates by a little under one frame
        Cue_2.frameNStart=frameN#exact frame index
        Cue_2.setAutoDraw(True)
    elif Cue_2.status==STARTED and t>=(0.0+4.0):
        Cue_2.setAutoDraw(False)
    
    #*game_2* updates
    if t>=4.0 and game_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        game_2.tStart=t#underestimates by a little under one frame
        game_2.frameNStart=frameN#exact frame index
        game_2.setAutoDraw(True)
    elif game_2.status==STARTED and t>=(4.0+4.0):
        game_2.setAutoDraw(False)
    
    #*choose_2* updates
    if t>=8.0 and choose_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        choose_2.tStart=t#underestimates by a little under one frame
        choose_2.frameNStart=frameN#exact frame index
        choose_2.setAutoDraw(True)
    elif choose_2.status==STARTED and t>=(8.0+4.0):
        choose_2.setAutoDraw(False)
    
    #*key_resp_2* updates
    if t>=8.0 and key_resp_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        key_resp_2.tStart=t#underestimates by a little under one frame
        key_resp_2.frameNStart=frameN#exact frame index
        key_resp_2.status=STARTED
        #keyboard checking is just starting
        key_resp_2.clock.reset() # now t=0
    elif key_resp_2.status==STARTED and t>=(8.0+4.0):
        key_resp_2.status=STOPPED
    if key_resp_2.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['y', 'n'])
        if len(theseKeys)>0:#at least one key was pressed
            key_resp_2.keys.extend(theseKeys)#storing all keys
            key_resp_2.rt.append(key_resp_2.clock.getTime())
    
    #*wait_2* updates
    if t>=12.0 and wait_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        wait_2.tStart=t#underestimates by a little under one frame
        wait_2.frameNStart=frameN#exact frame index
        wait_2.setAutoDraw(True)
    elif wait_2.status==STARTED and t>=(12.0+2.0):
        wait_2.setAutoDraw(False)
    
    #*feed_2* updates
    if t>=14.0 and feed_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        feed_2.tStart=t#underestimates by a little under one frame
        feed_2.frameNStart=frameN#exact frame index
        feed_2.setAutoDraw(True)
    elif feed_2.status==STARTED and t>=(14.0+2.0):
        feed_2.setAutoDraw(False)
    
    #*feed_b_2* updates
    if t>=14.0 and feed_b_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        feed_b_2.tStart=t#underestimates by a little under one frame
        feed_b_2.frameNStart=frameN#exact frame index
        feed_b_2.setAutoDraw(True)
    elif feed_b_2.status==STARTED and t>=(14.0+2.0):
        feed_b_2.setAutoDraw(False)
    
    #*AS* updates
    if t>=16.0 and AS.status==NOT_STARTED:
        #keep track of start time/frame for later
        AS.tStart=t#underestimates by a little under one frame
        AS.frameNStart=frameN#exact frame index
        AS.setAutoDraw(True)
    elif AS.status==STARTED and t>=(16.0+4.0):
        AS.setAutoDraw(False)
    
    #*key_resp_3* updates
    if t>=16.0 and key_resp_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        key_resp_3.tStart=t#underestimates by a little under one frame
        key_resp_3.frameNStart=frameN#exact frame index
        key_resp_3.status=STARTED
        #keyboard checking is just starting
        key_resp_3.clock.reset() # now t=0
    elif key_resp_3.status==STARTED and t>=(16.0+4.0):
        key_resp_3.status=STOPPED
    if key_resp_3.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['y', 'n'])
        if len(theseKeys)>0:#at least one key was pressed
            key_resp_3.keys=theseKeys[-1]#just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
    
    #*feed_3* updates
    if t>=20.0 and feed_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        feed_3.tStart=t#underestimates by a little under one frame
        feed_3.frameNStart=frameN#exact frame index
        feed_3.setAutoDraw(True)
    elif feed_3.status==STARTED and t>=(20.0+4.0):
        feed_3.setAutoDraw(False)
    
    #*feed_b_3* updates
    if t>=20.0 and feed_b_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        feed_b_3.tStart=t#underestimates by a little under one frame
        feed_b_3.frameNStart=frameN#exact frame index
        feed_b_3.setAutoDraw(True)
    elif feed_b_3.status==STARTED and t>=(20.0+4.0):
        feed_b_3.setAutoDraw(False)
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in PDASComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine PDAS
for thisComponent in PDASComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#Shutting down:
win.close()
core.quit()
