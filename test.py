import tkinter

def set_button(p_root):
    img = tkinter.PhotoImage(file=r'./stop.png')
    ret_button = tkinter.Button(p_root, text='pouet')
    ret_button.configure(image=img)
    

    return ret_button

def main():
    t = tkinter.Tk()
    button = set_button(t)
    button.pack()

    t.mainloop()

if __name__ == "__main__":
    main()

