#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:22:11 2020

@author: fschwarz
"""

from pynput import keyboard

class Keyboard_listener:
    def __init__(self, p_do_when_triggered, p_do_when_untriggered):
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.triggered = False
        self.do_when_triggered = p_do_when_triggered
        self.do_when_untriggered = p_do_when_untriggered

        listener = keyboard.Listener(
            on_press=self.do_on_keypressed,
            on_release=self.do_on_keyreleased)
        listener.start()
        
    def do_on_keypressed(self, key):
        if key == keyboard.Key.ctrl:
            self.ctrl_pressed = True
        if key == keyboard.Key.shift:
            self.shift_pressed = True
                
        if self.ctrl_pressed and self.shift_pressed and not self.triggered:
            self.do_when_triggered()
            self.triggered = True
        
    def do_on_keyreleased(self, key):
        if key == keyboard.Key.ctrl:
            self.ctrl_pressed = False
                
        if key == keyboard.Key.shift:
            self.shift_pressed = False
                
        if (not self.ctrl_pressed) and (not self.shift_pressed) and self.triggered:
            self.do_when_untriggered()
            self.triggered = False
                

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
