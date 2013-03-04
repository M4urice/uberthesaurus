from Tkinter import *  
def callback():

   print 'called the callback'  
root=Tk()  
#Erstellen des Menues

menuobj=Menu(root) #Menuekonstruktor

root.config(menu=menuobj)  
filemenu=Menu(menuobj)

menuobj.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New', command=callback)

filemenu.add_command(label='Open', command=callback)

filemenu.add_separator()

filemenu.add_command(label='Exit', command=callback)  
helpmenu=Menu(menuobj)

menuobj.add_cascade(label, menu=helpmenu)

helpmenu.add_command(label='About', command=callback)  
mainloop()