from Tkinter import *
root = Tk()


def Hello():
    label_goodby.pack_forget()
    label_hello.pack()

def Goodby():
    label_hello.pack_forget()
    label_goodby.pack()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
deskmenu = Menu(menu)
helpmenu = Menu(menu)
label_hello = Label(root, text="Hello!")
label_goodby = Label(root, text="Goodby!")
# file menu
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu", command=Hello)
filemenu.add_command(label="Oeffnen")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Schliessen", command=Goodby)
# deskriptor menu
menu.add_cascade(label="Deskriptor", menu=deskmenu)
deskmenu.add_command(label="hinzufuegen")
deskmenu.add_command(label="bearbeiten")
deskmenu.add_command(label="loeschen")

# deskriptor menu
menu.add_cascade(label="Deskriptor", menu=helpmenu)
helpmenu.add_command(label="hinzufuegen")
helpmenu.add_command(label="bearbeiten")
helpmenu.add_command(label="loeschen")

root.mainloop()