from psychopy import visual, event, core, gui, data, logging
import os #handy system and path functions
from psychopy.hardware.emulator import launchScan
import numpy as np  # whole numpy lib is available, pre-pend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName

#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

# settings for launchScan:
MR_settings = { 
    'TR': 2.000, # duration (sec) per volume
    'volumes': 11, # number of whole-brain 3D volumes / frames
    'sync': '5', # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
    }
infoDlg = gui.DlgFromDict(MR_settings, title='fMRI parameters', order=['TR','volumes'])
if not infoDlg.OK: core.quit()

win = visual.Window(size=(1280, 800), fullscr=True, monitor='testmonitor',
color=[-1,-1,-1], colorSpace='rgb')
globalClock = core.Clock()

# summary of run timing, for each key press:
output = 'vol    onset key\n'
for i in range(-1 * MR_settings['skip'], 0):
    output += '%d prescan skip (no sync)\n' % i

key_code = MR_settings['sync']
counter = visual.TextStim(win, height=.05, pos=(0,0), color=win.rgb+0.5)
output += "  0    0.000 %s start of scanning run, vol 0\n" % key_code
pause_during_delay = (MR_settings['TR'] > .4)
sync_now = False

# can simulate user responses, here 3 key presses in order 'a', 'b', 'c' (they get sorted by time):
simResponses = [(0, '5'), (2, '5'), (4, '5'), (6, '5'), (8, '5'), (10, '5'), (12, '5'), (14, '5'), (16, '5'), (18, '5'), (20, '5'), (22, '5')]

# launch: operator selects Scan or Test (emulate); see API documentation
vol = launchScan(win, MR_settings, globalClock=globalClock, simResponses=simResponses)

infer_missed_sync = False # best if your script timing works without this, but this might be useful sometimes
max_slippage = 0.02 # how long to allow before treating a "slow" sync as missed
    # any slippage is almost certainly due to timing issues with your script or PC, and not MR scanner

duration = MR_settings['volumes'] * MR_settings['TR']
# note: globalClock has been reset to 0.0 by launchScan()

#create stimuli

#Initialise components for routine:PD

fix=visual.TextStim(win=win, ori=0, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1, autoLog=True)
    
Cue=visual.TextStim(win=win, ori=0, name='Cue',
    text="      You are now playing \nthe PRISONER'S DILEMMA \n   game with your partner",
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1, autoLog=True)
    
game=visual.SimpleImageStim(win=win, 
    image='Screenshot.png', pos=[0.0, 0.0], units=None,
    opacity=1.0, name='game', autoLog=True)
    
choose=visual.TextStim(win=win, ori=0, name='choose',
    text='Do you cooperate or default?',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1, autoLog=True)
    
wait=visual.TextStim(win=win, ori=0, name='wait',
    text='Wait',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1, autoLog=True)
    
feed=visual.TextStim(win=win, ori=0, name='feed',
    text='Your partner chose to',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1, autoLog=True)
    
feed_b=visual.TextStim(win=win, ori=0, name='feed_b',
    text='\n\n(cooperate or default)',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1, autoLog=True)
    
#start routine
t=0; globalClock.reset()
frameN=-1

while t<duration:
    #get current time
    t=globalClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    allKeys = event.getKeys()
    for key in allKeys:
        if key != MR_settings['sync']:
            output += "%3d  %7.3f %s\n" % (vol-1, t, str(key))
    if 'escape' in allKeys:
        output += 'user cancel, '
        break
    # detect sync or infer it should have happened:
    if MR_settings['sync'] in allKeys:
        sync_now = key_code # flag
        onset = t
    if infer_missed_sync:
        expected_onset = vol * MR_settings['TR']
        now = t
        if now > expected_onset + max_slippage:
            sync_now = '(inferred onset)' # flag
            onset = expected_onset
    if sync_now:
        #*fix* updates
        if (0.0+4.0)>t>=0.0:
            #keep track of start time/frame for later
            fix.tStart=t#underestimates by a little under one frame
            fix.frameNStart=frameN#exact frame index
            fix.setAutoDraw(True)
            win.flip()

        #*Cue* updates
        if (4.0+4.0)>t>=4.0:
            fix.setAutoDraw(False)
            #keep track of start time/frame for later
            Cue.tStart=t#underestimates by a little under one frame
            Cue.frameNStart=frameN#exact frame index
            Cue.setAutoDraw(True)
            win.flip()

            #*game* updates
        if (8.0+4.0)>t>=8.0:
            Cue.setAutoDraw(False)
            #keep track of start time/frame for later
            game.tStart=t#underestimates by a little under one frame
            game.frameNStart=frameN#exact frame index
            game.draw()
            win.flip()
        
        #*choose* updates
        if (12.0+4.0)>t>=12.0:

            #keep track of start time/frame for later
            choose.tStart=t#underestimates by a little under one frame
            choose.frameNStart=frameN#exact frame index
            choose.setAutoDraw(True)
            win.flip()
        
        #*wait* updates
        if (16.0+2.0)>t>=16.0:
            choose.setAutoDraw(False)
            #keep track of start time/frame for later
            wait.tStart=t#underestimates by a little under one frame
            wait.frameNStart=frameN#exact frame index
            wait.setAutoDraw(True)
            win.flip()
            
            #*feed* and *feed_b* updates
        if (18.0+2.0)>t>=18.0:
            wait.setAutoDraw(False)
            #keep track of start time/frame for later
            feed.tStart=t#underestimates by a little under one frame
            feed.frameNStart=frameN#exact frame index
            feed.setAutoDraw(True)
            feed_b.tStart=t#underestimates by a little under one frame
            feed_b.frameNStart=frameN#exact frame index
            feed_b.setAutoDraw(True)
            win.flip()
            
        if (20.0+2.0)>t>=20:
            feed.setAutoDraw(False)
            feed_b.setAutoDraw(False)
            win.flip()
            
        counter.setText("%d volumes\n%.3f seconds" % (vol, onset))
        output += "%3d  %7.3f %s\n" % (vol, onset, sync_now)
        vol += 1
        sync_now = False

output += "end of scan (vol 0..%d = %d of %s). duration = %7.3f" % (vol - 1, vol, MR_settings['volumes'], globalClock.getTime())
print output
#print 'For the test, there should be 5 trials (vol 0..4, key 5), with three simulated subject responses (a, b, c)'

core.quit()