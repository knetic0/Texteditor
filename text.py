from tkinter import *
from tkinter import filedialog
import os
from tkinter import Text
import tkinter as tk
from tkinter.colorchooser import *

root = Tk()
root.geometry('1920x1080')
root.title('Notepad Pro')

timer = 0
timerS = 0


global i, zero
i = 1
zero = 0

textA = Text(root,width=1920,height=1080,font=('Arial Rounded MT Bold',20))
textA.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

def run():
	global file1
	os.system(f"cmd /c {file1}")

def saveas():
	file = filedialog.asksaveasfile()
	file.write(textA.get(1.0,END))
	file.close()


def openfile():
	textA.delete(1.0,END)
	global file1
	file1 = filedialog.askopenfilename()
	readFile = open(file1,'r')
	textA.insert(tk.END, readFile.read())

	readFile.close()

def save():
	global file1

	writeFile = open(file1,'w')
	writeFile.write(textA.get(1.0,END))
	writeFile.close()

def colorChoose():
	color = askcolor()

	textA.config(fg=color[1])


def bigger(x):
	global timer
	global timerBig
	timer += x
	timerBig = 20 + timer
	textA.config(font=('',timerBig))


def smaller(y):
	global timerBig
	global timerS
	timerS -= y
	timerBig -= y
	textA.config(font=('Ink Free',timerBig))

def fontChoose():
	gui = Tk()
	gui.title('Choose Font')
	gui.geometry('420x420')

	global result

	def chooseButton():

		result = listBox.curselection()


		if result[0] == 0:
			label1.config(font=('Calibri',20))
			textA.config(font=('Calibri',20))

		elif result[0] == 1:
			label1.config(font=('Ink Free',20))
			textA.config(font=('Ink Free',20))

		elif result[0] == 2:
			label1.config(font=('Arial',20))
			textA.config(font=('Arial',20))

	listBox = Listbox(gui,font=('Calibri',20))
	listBox.pack()
	label1 = Label(gui,text='Hello World',font=('Calibri',20))
	label1.pack()

	listBox.insert(0, 'Calibri')
	listBox.insert(1, 'Ink Free')
	listBox.insert(2, 'Arial')

	button1 = Button(gui,text='Choose',font=('Calibri',20),command=chooseButton)
	button1.pack()

	gui.mainloop()

#auto reaction
'''
def auto():
	textA.insert('end',')')

def autoT():
	global i
	global zero
	textA.insert(i.zero,'\t')

def autoTab():
	global i
	i += 1


def autoWr():
	textA.insert(1.0,"'")
'''
def bgColor():
	bgChooser = askcolor()
	textA.config(bg=bgChooser[1])

	colorChoose()

optionsMenu = Menu(my_menu,tearoff=False)
settingsMenu = Menu(my_menu,tearoff=False)
runMenu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=optionsMenu)
my_menu.add_cascade(label='Settings',menu=settingsMenu)
my_menu.add_cascade(label='Run',menu=runMenu)
optionsMenu.add_command(label='Save as',command=saveas)

optionsMenu.add_command(label='Open File',command=openfile)
optionsMenu.add_command(label='Save',command=save)

root.bind("<Control-s>",lambda x: save())
root.bind("<Control-+>",lambda x: bigger(2))
root.bind("<Control-_>",lambda x: smaller(2))
root.bind("<Alt-s>",lambda x: saveas())
root.bind("<F5>",lambda x: run())
'''
root.bind("<Shift-(>",lambda x: auto())
root.bind("<'>",lambda x: autoWr())
root.bind("<Shift-:>",lambda x: autoT())
root.bind("<Return>",lambda x: autoTab())
'''

settingsMenu.add_command(label='Font++',command=lambda:bigger(2))
settingsMenu.add_command(label='Font--',command=lambda:smaller(2))
settingsMenu.add_command(label='Font Color',command=colorChoose)
settingsMenu.add_command(label='Font Type',command=fontChoose)
settingsMenu.add_command(label='Background Color',command=bgColor)

runMenu.add_command(label='Run',command=run)


root.mainloop()

