
from tkinter import *
from tkinter import ttk
    
root = Tk()
style = ttk.Style()



button = ttk.Button(text = "Go To Funeral")
button.pack()
style.map("C.TButton",
    foreground=[('pressed', 'green'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
button.config(style = "C.TButton")
f = ttk.Button(text = "Press [F] To Pay Respects")
pic = PhotoImage(file =
        "E:/school/2018-19/caps/A Foot in the Door/images/pressf.png").subsample(3,3)

f.config(image = pic, compound = TOP)
def callback():
    button.state(["disabled"])
    f.pack()
    f.config(command = reviver())

def reviver():
    button.state(["!disabled"])
    print("F")

button.config(command = callback)

# logo = PhotoImage(file = 'E:/school/2018-19/caps/A Foot in the Door/images/Football+of+Food+Gif.gif') # change path to image as necessary
# button.config(image = logo, compound = LEFT)
# small_logo = logo.subsample(5, 5)
# button.config(image = small_logo)

root.mainloop()
