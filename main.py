from time import sleep
from tkinter import *
from tkinter import ttk
import getValues
import moneys
from likeCss import *
from threading import Thread

VALUES = getValues.moneys.values
options = [i.upper() for i in moneys.types]

def changeState(state):
    entry_1.config(state=state)
    entry_2.config(state=state)
    menu_1.config(state=state)
    menu_2.config(state=state)
    count.config(state=state)
    updateButton.config(state=state)
    if state == 'normal':
        label.config(text='Go ahead, Mr. Joestar')
    else:
        label.config(text='Loading...')
    

def update(*args):
    progressbar = progressbarClass(window)
    progressbar.place(x=200, y=400)
    progressbar["maximum"] = len(getValues.moneys.types) - 1
    progressbar['value'] = 0
    
    def progressing():
        progress = 0
        changeState(state='disable')
        while progress < len(getValues.moneys.types) - 1:
            if progress != getValues.progress:
                progress = getValues.progress
                progressbar['value'] = progress
                window.update()
        changeState(state='normal')
        sleep(0.2)
        progressbar.destroy()
        
                
    Thread(target=progressing).start()
    Thread(target=getValues.selAll).start()

def countFuction(*args):
    global VALUES
    inp = entry_1.get()
    if entry_1:
        try:
            inp = float(inp)
        except:
            warning.config(state='active')
        else:
            warning.config(state='disabled')
            key1 = variable_1.get()
            key2 = variable_2.get()
            if key1 != key2:
                val1, val2 = VALUES[key1], VALUES[key2]
                res = (val2/val1) * inp 
                entry_2.delete(0, END)
                
                res = str(res).split('.')
                res = res[0] + '.' + res[1][:4 if len(res[1]) > 4 else len(res[1])]
                entry_2.insert(0, res)
            else:
                entry_2.delete(0, END)
                entry_2.insert(0, str(inp))

window = Tk()
window.geometry("600x700")
window.resizable(False, False)
window.title('Exchange rate')

window.config(background='#404040')

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

warning = warningLabel(window)
warning.config(state='disabled')
warning.place(x=20, y=250)


label = classLabel(window, 'Loading...')
label.pack()

entry_1 = classEntry(window)
entry_1.insert(0, '1')
entry_1.place(x=20, y=200)

entry_2 = classEntry(window)
entry_2.place(x=20, y=320)

variable_1 = StringVar(window)
variable_1.set(options[0])

variable_2 = StringVar(window)
variable_2.set(options[0])


menu_1 = OptionMenu(window, variable_1, *options, command=countFuction)
menu_1.config(menuClass)
menu_1.place(x=465, y=200, width=100, height=50)

menu_2 = OptionMenu(window, variable_2, *options, command=countFuction)
menu_2.config(menuClass)
menu_2.place(x=465, y=320, width=100, height=50)

        
count = buttonClass(window, countFuction, 'Count')
count.place(x=0, y=540)

updateButton = buttonClass(window, update, 'Update')
updateButton.place(x=330, y=540)


update()
window.mainloop()
