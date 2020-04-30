import tkinter
import os

WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150

class builded_GUI:
    def __init__(self):
        self.window = self.set_window()
        self.rec_button = self.set_rec_button()
        self.stop_button = self.set_stop_button()

        self.rec_button.pack()

    def set_window(self):
        ret_window = tkinter.Tk()
        ret_window.title("[ODV]")
        ret_window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        ret_window.protocol("WM_DELETE_WINDOW", self.on_closing)

        return ret_window

    def on_closing(self):
        print("AU REVOIR")
        self.window.destroy()


    def set_rec_button(self):
        img = tkinter.PhotoImage(file=r'./record.png')
        ret_button = tkinter.Button(self.window, image=img)
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
#        ret_button.bind('<Button-1>', self.switch_buttons)

        return ret_button

    def set_stop_button(self):
        img = tkinter.PhotoImage(file=r'./stop.png')
        ret_button = tkinter.Button(self.window, image=img)
        ret_button.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
#        ret_button.bind('<Button-1>', self.switch_buttons)

        return ret_button

    def switch_buttons(self, event):
        l = [self.rec_button, self.stop_button]
        l.remove(event.widget)
        event.widget.pack_forget()
        l[0].pack()

    def launch(self):
        self.window.mainloop()
