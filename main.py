import tkinter as tk
from GUI_Functions import *
from tkinter import *
from tkinter import filedialog

files = []
report= open("report.txt", 'r')
report = report.read()


def addFile():
    filename = filedialog.askopenfilename(title="Select File", filetypes=(("text", "*txt"), ("all files", "*.*")))
    file = open(filename, 'r')
    print(file.read())
    file.close()


def Report():
    popUp = Toplevel()
    popUp.title("AI Search Report")
    popUp.geometry("800x800")

    report_label = Label(popUp, text="Report")
    report_label.pack()

    report_text = Text(popUp, width=120, height=100)
    report_text.pack(pady=30)


    report_text.insert(END, report)


'''Window'''
window = tk.Tk()
window.title("AI Search")
window.geometry("400x400")


GUI = GUI_Functions()

'''Frame and Canvas'''
canvas = tk.Canvas(window, height=400, width=500, bg="#00008B")
canvas.pack()

frame = tk.Frame(window, bg="green")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

space = Label(frame, text=" ", bg="green")
space.pack()


'''Buttons'''

openfile = Button(frame, text="Open", padx=10, pady=5, fg="black", command=lambda: [GUI.OpenTextFile()])
breathfirst = Button(frame, text="Breath First Search", padx=10, pady=5, fg="black", command=GUI.breathFirst)
depthfirst = Button(frame, text="Depth First Serch", padx=10, pady=5, fg="black", command=GUI.depthFirst)
bestfirst = Button(frame, text="Best First Serch", padx=10, pady=5, fg="black",  command=GUI.bestFirst)
astar = Button(frame, text="A* First Serch", padx=10, pady=5, fg="black", command=GUI.aStar)

reports = Button(frame, text="Report", padx=10, pady=5, fg="black", command=Report)
clear = Button(frame, text="clear", padx=10, pady=5, fg="black", command=lambda: [GUI.close()])
closefile = Button(frame, text="close", padx=10, pady=5, fg="black", command=window.destroy)



openfile.pack()
breathfirst.pack()
depthfirst.pack()
bestfirst.pack()
astar.pack()

reports.pack()
clear.pack()
closefile.pack()


window.mainloop()