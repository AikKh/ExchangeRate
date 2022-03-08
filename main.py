from tkinter import *
from tkinter import font
import getValues
import moneys
from likeCss import *

getValues.selAll()
VALUES = getValues.moneys.values
options = [i.upper() for i in moneys.types]

def update(*args):
    window.destroy()
    getValues.selAll()
    window.mainloop()

def countFuction(*args):
    global VALUES
    inp = entry_1.get()
    if entry_1:
        try:
            inp = float(inp)
            warning.destroy()
        except:
            warning.place(x=190, y=360)
        else:
            key1 = variable_1.get()
            key2 = variable_2.get()
            if key1 != key2:
                val1, val2 = VALUES[key1], VALUES[key2]
                res = (val2/val1) * inp 
                entry_2.delete(0, END)
                entry_2.insert(0, str(res)[:6])
            else:
                entry_2.delete(0, END)
                entry_2.insert(0, str(inp))

window = Tk()
window.geometry("600x600")
window.resizable(False, False)
window.title('Exchange rate')

window.config(background='#404040')

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

label = classLabel(window)
label.pack()

entry_1 = classEntry(window)
entry_1.insert(0, '1')
entry_1.place(x=20, y=200)

entry_2 = classEntry(window)
entry_2.place(x=20, y=300)

warning = warningLabel(window)


variable_1 = StringVar(window)
variable_1.set(options[0])

variable_2 = StringVar(window)
variable_2.set(options[0])


menu_1 = OptionMenu(window, variable_1, *options, command=countFuction)
menu_1.config(menuClass)
menu_1.place(x=465, y=200, width=100, height=50)

menu_2 = OptionMenu(window, variable_2, *options, command=countFuction)
menu_2.config(menuClass)
menu_2.place(x=465, y=300, width=100, height=50)

        
count = buttonClass(window, countFuction, 'Count')
count.place(x=0, y=440)

updateButton = buttonClass(window, update, 'Update')
updateButton.config(state='disable')
updateButton.place(x=330, y=440)

window.mainloop()
