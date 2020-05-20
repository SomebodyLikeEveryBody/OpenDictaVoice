import tkinter

WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150

class Builded_GUI:
    def __init__(self, p_resources_path):
        self._resources_path = str(p_resources_path)
        self._window = self.build_window()
        self._rec_button = self.build_rec_button()
        self._stop_button = self.build_stop_button()
        self._language_chooser_menu = self.build_language_chooser()

        self._language_chooser_menu.pack()
        self._rec_button.pack()

    def build_window(self):
        ret_window = tkinter.Tk()
        ret_window.title("[ODV]")
        ret_window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        ret_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        ret_window.wm_attributes("-topmost", True)
        ret_window.wait_visibility(ret_window)
        ret_window.attributes('-alpha', 0.7)

        return ret_window

    def on_closing(self):
        print("AU REVOIR")
        self._window.destroy()

    def build_rec_button(self):
        img = tkinter.PhotoImage(file=self._resources_path + 'imgs/record.png')
        ret_button = tkinter.Button(self._window, image=img)
        ret_button.image = img
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT) 

        return ret_button

    def build_stop_button(self):
        img = tkinter.PhotoImage(file=self._resources_path + 'imgs/stop_record.png')
        ret_button = tkinter.Button(self._window, image=img)
        ret_button.image = img
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        return ret_button

    def build_language_chooser(self):
        choices = { 'fr','en'}
        language_stringvar = tkinter.StringVar(self._window)
        language_stringvar.set('fr') 
        ret_menu = tkinter.OptionMenu(self._window, language_stringvar, *choices)
        ret_menu.language_stringvar = language_stringvar
        return ret_menu

    def set_rec_button_visible(self):
        self._stop_button.pack_forget()
        self._rec_button.pack()

    def set_stop_button_visible(self):
        self._rec_button.pack_forget()
        self._stop_button.pack()

    def launch(self):
        self._window.mainloop()

    #returns the string that represents the current language, e.g. "fr" or "en"
    def get_language(self):
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
