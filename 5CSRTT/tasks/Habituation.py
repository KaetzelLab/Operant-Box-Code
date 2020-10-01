"""This file is created for 5-CSRTT habituation, task starts with reward and trial starts by presenting all light
of the five-choice light on for undefined time any poke at five_choice give reward

reward ==> five choice all lights on ==> reward

Important readouts:
Responses :- #Correct_response (can also rename as Responses )

"""


from pyControl.utility import *
import hardware_definition as hw

states = ['choice',
          'reward']


events = ['poke_1',
          'poke_2',
          'poke_3',
          'poke_4',
          'poke_5',
          'poke_6',
          'poke_6_out',
          'session_timer']

initial_state = 'reward'

# variables
v.steps_rate = 2000
v.n_steps = 1500
v.session_duration = 30 * minute


def run_start():
    # Set session timer and turn on houslight.
    set_timer('session_timer', v.session_duration)
    hw.reward_port.SOL.on()


def run_end():
    # Turn off all hardware outputs.
    hw.off()


def reward(event):
    if event == 'entry': 
        hw.syringe_pump.backward(v.steps_rate, v.n_steps)
        hw.reward_port.LED.on()
    elif event == 'exit':
        hw.reward_port.LED.off()
        hw.speaker.off()
    elif event == 'poke_6_out' or event == 'poke_6':
        hw.reward_port.LED.off()
        print('reward_obtained')
        goto_state('choice')


def choice(event):
    if event == 'entry':
        hw.five_poke.poke_1.LED.on()
        hw.five_poke.poke_2.LED.on()
        hw.five_poke.poke_3.LED.on()
        hw.five_poke.poke_4.LED.on()
        hw.five_poke.poke_5.LED.on()
    elif event == 'exit':
        hw.syringe_pump.backward(v.steps_rate, v.n_steps)
        hw.five_poke.poke_1.LED.off()
        hw.five_poke.poke_2.LED.off()
        hw.five_poke.poke_3.LED.off()
        hw.five_poke.poke_4.LED.off()
        hw.five_poke.poke_5.LED.off()
        hw.speaker.off()
    elif event == 'poke_1' or event == 'poke_2' or event == 'poke_3' or event == 'poke_4' or event == 'poke_5':
        hw.five_poke.poke_1.LED.off()
        hw.five_poke.poke_2.LED.off()
        hw.five_poke.poke_3.LED.off()
        hw.five_poke.poke_4.LED.off()
        hw.five_poke.poke_5.LED.off()
        print('Correct_response')
        goto_state('reward')



def all_states(event):
    # When 'session_timer' event occurs stop framework to end session.
    if event == 'session_timer':
        stop_framework()

