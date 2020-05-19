#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:22:11 2020

@author: fschwarz
"""

from pynput import keyboard

class Keyboard_listener:
    def __init__(self, p_do_when_triggered, p_do_when_untriggered):
        self._ctrl_pressed = False
        self._shift_pressed = False
        self._triggered = False
        self._do_when_triggered = p_do_when_triggered
        self._do_when_untriggered = p_do_when_untriggered

        listener = keyboard.Listener(
            on_press=self.do_on_keypressed,
            on_release=self.do_on_keyreleased)

        listener.start()
        
    def do_on_keypressed(self, key):
        if key == keyboard.Key.ctrl:
            self._ctrl_pressed = True

        if key == keyboard.Key.shift:
            self._shift_pressed = True
                
        if self._ctrl_pressed and self._shift_pressed and not self._triggered:
            self._do_when_triggered()
            self._triggered = True
        
    def do_on_keyreleased(self, key):
        if key == keyboard.Key.ctrl:
            self._ctrl_pressed = False
                
        if key == keyboard.Key.shift:
            self._shift_pressed = False
                
        if (not self._ctrl_pressed) and (not self._shift_pressed) and self._triggered:
            self._do_when_untriggered()
            self._triggered = False


    ########################
    # Attribute management #
    ########################

    @property
    def ctrl_pressed(self):
        raise PermissionError("It is not authorized to access or modify [ctrl_pressed] attribute")
        return None

    @ctrl_pressed.setter
    def ctrl_pressed(self, p_value):
        raise PermissionError("It is not authorized to access or modify [ctrl_pressed] attribute")

    @property
    def shift_pressed(self):
        raise PermissionError("It is not authorized to access or modify [shift_pressed] attribute")
        return None

    @shift_pressed.setter
    def shift_pressed(self, p_value):
        raise PermissionError("It is not authorized to access or modify [shift_pressed] attribute")

    @property
    def triggered(self):
        raise PermissionError("It is not authorized to access or modify [triggered] attribute")
        return None

    @triggered.setter
    def triggered(self, p_value):
        raise PermissionError("It is not authorized to access or modify [triggered] attribute")

    @property
    def do_when_triggered(self):
        return self._do_when_triggered

    @do_when_triggered.setter
    def do_when_triggered(self, p_value):
        if (type(p_value) != type(self.__init__)):
            raise PermissionError("[do_when_untriggered] attribute must be affected with a function type value")
    @property
    def do_when_untriggered(self):
        return self._do_when_untriggered

    @do_when_untriggered.setter
    def do_when_untriggered(self, p_value):
        if (type(p_value) != type(self.__init__)):
            raise PermissionError("[do_when_untriggered] attribute must be affected with a function type value")
