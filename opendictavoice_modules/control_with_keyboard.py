#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:22:11 2020

@author: fschwarz
"""


from pynput import keyboard



class Control_With_KeyBoard :
    def __init__(self, whenActivated, whenDisactivated):
        
        
        self.ctrl = False
        self.shift = False
        self.launched = False
        
        def on_press(key):
            if key == keyboard.Key.ctrl:
                self.ctrl = True
            if key == keyboard.Key.shift:
                self.shift = True
                
            if self.ctrl and self.shift and not self.launched:
                whenActivated()
                self.launched = True
        
        def on_release(key):
            if key == keyboard.Key.ctrl:
                self.ctrl = False
                
            if key == keyboard.Key.shift:
                self.shift = False
                
            if (not self.ctrl) and (not self.shift) and self.launched:
                whenDisactivated()   
                self.launched = False
                
        
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
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
