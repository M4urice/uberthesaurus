from Tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
deskmenu = Menu(menu)
helpmenu = Menu(menu)
# file menu
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu")
filemenu.add_command(label="Oeffnen")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Schliessen")
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
