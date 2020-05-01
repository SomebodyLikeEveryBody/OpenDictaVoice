import tkinter

WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150

class builded_GUI:
    def __init__(self, p_resources_path):
        self.resources_path = p_resources_path
        self.window = self.build_window()
        self.rec_button = self.build_rec_button()
        self.stop_button = self.build_stop_button()

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

    def switch_buttons(self, event):
        l = [self.rec_button, self.stop_button]
        l.remove(event.widget)
        event.widget.pack_forget()
        l[0].pack()

    def launch(self):
        self.window.mainloop()
