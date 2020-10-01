
from pyControl.utility import *
import hardware_definition as hw
####################################### State machine.######################################

states = ['choice',           
          'reward']

#################################### Events.################

events = ['poke_1', 
          'poke_2', 
          'poke_3', 
          'poke_4', 
          'poke_5',
          'poke_6','poke_6_out',
          'session_timer']

###################################################################################################

initial_state = 'choice'


#####################################################################################################
v.steps_rate = 3000
v.n_steps = 3000000
v.session_duration = 10*minute


##############################################################################

def run_start(): 
    # Set session timer and turn on houslight.
    set_timer('session_timer', v.session_duration)  
                             
    
def run_end():
    # Turn off all hardware outputs.  
    hw.off()
############################################################## STATE_1 #########################

def choice(event):
    if event == 'entry':
        hw.five_poke.poke_1.LED.off()
        hw.five_poke.poke_2.LED.off()
        hw.five_poke.poke_3.LED.off()
        hw.five_poke.poke_4.LED.off()
        hw.five_poke.poke_5.LED.off()
        hw.reward_port.LED.off()
        hw.reward_port.SOL.off()
        hw.syringe_pump.backward(v.steps_rate, v.n_steps)
    elif event == 'exit':
        hw.five_poke.poke_1.LED.off()
        hw.five_poke.poke_2.LED.off()
        hw.five_poke.poke_3.LED.off()
        hw.five_poke.poke_4.LED.off()
        hw.five_poke.poke_5.LED.off()
        hw.reward_port.LED.off()
        hw.reward_port.SOL.off()
        

          

################################################################################################################
def all_states(event):
    # When 'session_timer' event occurs stop framework to end session.
    if event == 'session_timer':
        stop_framework()
        

##def run_end():
    ##hw.off() # Turn off all outputs.

