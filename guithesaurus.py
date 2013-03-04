from Tkinter import *

root = Tk()

def New():
	message_text = "Willkommen auf unserem ersten Thesaurus Versuch!"
	msg = Message (root, text=message_text).pack()

def Suche():
	Label(root, text="Suche").grid(row=0)
	entry_suche = Entry(root)
	entry_suche.grid(row=0, column=1)
	Button(root, text='Suchen',).grid(row=1)

def NewDeskriptor():
	Label(root, text="Oberbegriff").grid(row=0)
	Label(root, text="Unterbegriff").grid(row=1)
	Label(root, text="Verwandterbegriff").grid(row=2)
	entry_oberbegriff = Entry(root)
	entry_oberbegriff.grid(row=0, column=1)
	entry_unterbegriff = Entry(root)
	entry_unterbegriff.grid(row=1, column=1)
	entry_verwandterbegriff = Entry(root)
	entry_verwandterbegriff.grid(row=2, column=1)
	Button(root, text='Speichern',).grid(row=4)

# Main Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu", command=New)
filemenu.add_command(label="Import")
filemenu.add_command(label="Export")
filemenu.add_command(label="Oeffnen")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Schliessen")
# Deskrptor Menu
desmenu = Menu(menu)
menu.add_cascade(label="Deskritpor", menu=desmenu)
desmenu.add_command(label="Deskriptorliste")
desmenu.add_command(label="Suche", command=Suche)
# Verwaltung
vermenu = Menu(menu)
menu.add_cascade(label="Verwaltung", menu=vermenu)
vermenu.add_command(label="einfuegen", command=NewDeskriptor)
vermenu.add_command(label="loeschen")
vermenu.add_command(label="bearbeiten")

root.mainloop()