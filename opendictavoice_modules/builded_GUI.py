# -*- coding: utf-8 -*-

"""
   Module containing the definition of Builded_GUI class,
   which is supposed to manage all vues and GUI problematics (buttons, window, ...)

   There are 2 constants defined in this file:

   WINDOW_WIDTH: width of the GUI
   WINDOW_HEIGHT: height of the GUI

   You can modify these constants at your convenience to have a window at the size you desire.

"""

import tkinter

WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150

class Builded_GUI:
    """
        Class which is supposed to manage all vues and GUI problematics (buttons, window, ...)

        Attributes:
        ----------

        self._resources_path        : str                     : path of the resources folder
        self._window                : tkinter.Tk() object     : tkinter object to manager the GUI
        self._rec_button            : tkinter.Button() object : rec button shown in the GUI
        self._stop_button           : tkinter.Button() object : stop button shown in the GUI
        self._language_chooser_menu : pyaudio.Stream object   : scrolling menu to choose the language

        Methods:
        -------

        self.build_window()
        self.on_closing()
        self.build_rec_button()
        self.build_stop_button()
        self.build_language_chooser()
        self.set_rec_button_visible()
        self.set_stop_button_visible()
        self.launch()
        self.get_language()
    """

    def __init__(self, p_resources_path):
        """
            Constructor method, initialize all class attributes

            :param p_resources_path: raw string of the path of resources folder
            :type p_resources_path: str
            :return: None
            :rtype: None
        """
        self._resources_path = str(p_resources_path)
        self._window = self.build_window()
        self._rec_button = self.build_rec_button()
        self._stop_button = self.build_stop_button()
        self._language_chooser_menu = self.build_language_chooser()

        self._language_chooser_menu.pack()
        self._rec_button.pack()

    def build_window(self):
        """
            Instanciates a tkinter.Tk() object that will be the main window of the application,
            then customizes and returns it

            :return: tkinter.Tk() object instanctiated
            :rtype: tkinter.Tk() object
        """

        ret_window = tkinter.Tk()
        ret_window.title("[ODV]")
        ret_window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        ret_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        ret_window.wm_attributes("-topmost", True)
        ret_window.wait_visibility(ret_window)
        ret_window.attributes('-alpha', 0.7)

        return ret_window

    def on_closing(self):
        """
            Method called when self._window is closed in order to destroy it properly

            :return: None
            :rtype: None
        """

        print("AU REVOIR")
        self._window.destroy()

    def build_rec_button(self):
        """
            Instanciates a tkinter.Button() object, then customizes to make a rec_button, and returns it

            :return: tkinter.Button() object instantiated
            :rtype: tkinter.Button() object
        """

        img = tkinter.PhotoImage(file=self._resources_path + 'imgs/record.png')
        ret_button = tkinter.Button(self._window, image=img)
        ret_button.image = img
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        return ret_button

    def build_stop_button(self):
        """
            Instanciates a tkinter.Button() object, then customizes to make a stop_button, and returns it

            :return: tkinter.Button() object instantiated
            :rtype: tkinter.Button() object
        """
        img = tkinter.PhotoImage(file=self._resources_path + 'imgs/stop_record.png')
        ret_button = tkinter.Button(self._window, image=img)
        ret_button.image = img
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        return ret_button

    def build_language_chooser(self):
        """
            Instanciates a tkinter.StringVar() object, then customizes to make a language chooser menu
            and returns it

            :return: tkinter.StringVar() object instantiated
            :rtype: tkinter.StringVar() object
        """
        choices = { 'fr','en'}
        language_stringvar = tkinter.StringVar(self._window)
        language_stringvar.set('fr')
        ret_menu = tkinter.OptionMenu(self._window, language_stringvar, *choices)
        ret_menu.language_stringvar = language_stringvar
        return ret_menu

    def set_rec_button_visible(self):
        """
            Shows the rec button visible in the GUI and hide the stop button

            :return: None
            :rtype: None
        """
        self._stop_button.pack_forget()
        self._rec_button.pack()

    def set_stop_button_visible(self):
        """
            Shows the stop button visible in the GUI and hide the rec button

            :return: None
            :rtype: None
        """
        self._rec_button.pack_forget()
        self._stop_button.pack()

    def launch(self):
        """
            Launches the mainloop of the GUI

            :return: None
            :rtype: None
        """
        self._window.mainloop()

    #returns the string that represents the current language, e.g. "fr" or "en"
    def get_language(self):
        """
            Returns the string that represents the current language chosen by the user,
            e.g. "fr" or "en"

            :return: self._language_chooser_menu attribute
            :rtype: str
        """
        return self._language_chooser_menu.language_stringvar.get()


    ########################
    # Attribute management #
    ########################

    @property
    def resources_path(self):
        return (self._resources_path)

    @resources_path.setter
    def resources_path(self, p_value):
        self._resources_path = str(p_value)

    @property
    def window(self):
        raise PermissionError("It is not authorized to access or modify [window] attribute")
        return None

    @window.setter
    def window(self, p_value):
        raise PermissionError("It is not authorized to access or modify [window] attribute")

    @property
    def rec_button(self):
        return self._rec_button

    @rec_button.setter
    def rec_button(self, p_value):
        raise PermissionError("It is not authorized to modify [rec_button] attribute")

    @property
    def stop_button(self):
        return self._stop_button

    @stop_button.setter
    def stop_button(self, p_value):
        raise PermissionError("It is not authorized to modify [stop_button] attribute")

    @property
    def language_chooser_menu(self):
        raise PermissionError("It is not authorized to access or modify [language_chooser_menu] attribute")
        return None

    @language_chooser_menu.setter
    def language_chooser_menu(self, p_value):
        raise PermissionError("It is not authorized to access or modify [language_chooser_menu] attribute")
