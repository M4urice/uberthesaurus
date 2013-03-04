from Tkinter import *

root = Tk()

message_text = "Willkommen auf unserem ersten Thesaurus Versuch!"

msg = Message (root, text=message_text).pack()

quit_button = Button(root, text="Quit", command=root.quit).pack()

# Main Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu")
filemenu.add_command(label="Import")
filemenu.add_command(label="Export")
filemenu.add_command(label="Oeffnen")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Schliessen")
# Deskrptor Menu
desmenu = Menu(menu)
menu.add_cascade(label="Deskritpor", menu=desmenu)
desmenu.add_command(label="Deskriptorliste")
desmenu.add_command(label="Suche")
# Verwaltung
vermenu = Menu(menu)
menu.add_cascade(label="Verwaltung", menu=vermenu)
vermenu.add_command(label="einfuegen")
vermenu.add_command(label="loeschen")
vermenu.add_command(label="bearbeiten")