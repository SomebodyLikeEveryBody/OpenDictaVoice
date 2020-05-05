#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:22:11 2020

@author: fschwarz
"""

from pynput import keyboard

class Keyboard_listener:
    def __init__(self, p_when_activated, p_when_disactivated):
        self.ctrl = False
        self.shift = False
        self.launched = False
        
        def do_on_press(key):
            if key == keyboard.Key.ctrl:
                self.ctrl = True
            if key == keyboard.Key.shift:
                self.shift = True
                
            if self.ctrl and self.shift and not self.launched:
                p_when_activated()
                self.launched = True
        
        def do_on_release(key):
            if key == keyboard.Key.ctrl:
                self.ctrl = False
                
            if key == keyboard.Key.shift:
                self.shift = False
                
            if (not self.ctrl) and (not self.shift) and self.launched:
                p_when_disactivated()   
                self.launched = False
                
            listener = keyboard.Listener(
                on_press=do_on_press,
                on_release=do_on_release)
            listener.start()

#        
#        def on_press(key):
#            try:
#                print('alphanumeric key {0} pressed'.format(
#                    key.char))
#            except AttributeError:
#                print('special key {0} pressed'.format(
#                    key))
#        
#        def on_release(key):
#            print('{0} released'.format(
#                key))
#            if key == keyboard.Key.esc:
#                # Stop listener
#                return False
