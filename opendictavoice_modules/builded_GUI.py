import tkinter

WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150

class Builded_GUI:
    def __init__(self, p_resources_path):
        self.resources_path = p_resources_path
        self.window = self.build_window()
        self.rec_button = self.build_rec_button()
        self.stop_button = self.build_stop_button()
        self.language_chooser_menu = self.build_language_chooser()

        self.language_chooser_menu.pack()
        self.rec_button.pack()

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
        self.window.destroy()

    def build_rec_button(self):
        img = tkinter.PhotoImage(file=self.resources_path + 'imgs/record.png')
        ret_button = tkinter.Button(self.window, image=img)
        ret_button.image = img
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT) 

        return ret_button

    def build_stop_button(self):
        img = tkinter.PhotoImage(file=self.resources_path + 'imgs/stop_record.png')
        ret_button = tkinter.Button(self.window, image=img)
        ret_button.image = img
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        return ret_button

    def build_language_chooser(self):
        choices = { 'fr','en'}
        language_stringvar = tkinter.StringVar(self.window)
        language_stringvar.set('fr') 
        ret_menu = tkinter.OptionMenu(self.window, language_stringvar, *choices)
        ret_menu.language_stringvar = language_stringvar
        return ret_menu
        
    def set_rec_button_visible(self):
        self.stop_button.pack_forget()
        self.rec_button.pack()
        
    def set_stop_button_visible(self):
        self.rec_button.pack_forget()
        self.stop_button.pack()

    def launch(self):
        self.window.mainloop()

    #returns the string that represents the current language, e.g. "fr" or "en"
    def get_language(self):
        return self.language_chooser_menu.language_stringvar.get()
