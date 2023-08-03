from tkinter import *
import numpy as np
import importlib
from parametric import Parametric3D

def write_to_file():
    txt = function_write.get(1.0, END)
    f = open("funcs.py", "w")
    f.write(txt)
    f.close()

def run_file():
    import funcs
    importlib.reload(funcs)
    p = Parametric3D(funcs.r, 2, 3, funcs.tht, funcs.phi, funcs.title)
    p.plot()

root = Tk()
root.geometry("800x800")
root.title("Parametric Surface Visualiser")

save = Button(root, text="Save", command=write_to_file)
save.grid(column=0, row=1)

run = Button(root, text="Run", command=run_file)
run.grid(column=1, row=1)

function_write = Text(root)
function_write.grid(column=2, row=2)
function_write.insert(INSERT, 
"""from numpy import *

title = "My Surface"

# Define the domain of your plot here
tht = linspace(0, 2*pi) 
phi = linspace(0, 2*pi)

# Define the function of your plot here
def r(u, v):
    x = 
    y = 
    z = 
    return x, y, z
""")

instructions = Label(root, text="Write your function above, then hit save and run")
instructions.grid(column=2, row=4)

root.mainloop()