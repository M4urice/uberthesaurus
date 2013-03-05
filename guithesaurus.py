from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()
# klasse machen: vergessen alle was gezeichnet wurde dann neu



	
#def New():
	
	

def Suche():
	label_ober.grid_forget()
	label_unter.grid_forget()
	label_verwandt.grid_forget()
	entry_oberbegriff.grid_forget()
	entry_unterbegriff.grid_forget()
	entry_verwandterbegriff.grid_forget()
	speichern_button.grid_forget()
	label_suche.grid(row=0)
	entry_suche.grid(row=0, column=1)
	suchen_button.grid(row=1)

def NewDeskriptor():
	label_suche.grid_forget()
	entry_suche.grid_forget()
	suchen_button.grid_forget()
	label_ober.grid(row=0)
	label_unter.grid(row=1)
	label_verwandt.grid(row=2)
	entry_oberbegriff.grid(row=0, column=1)
	entry_unterbegriff.grid(row=1, column=1)
	entry_verwandterbegriff.grid(row=2, column=1)
	speichern_button.grid(row=4)
	
def openfile():
	label_suche.grid_forget()
	entry_suche.grid_forget()
	suchen_button.grid_forget()
	label_ober.grid_forget()
	label_unter.grid_forget()
	label_verwandt.grid_forget()
	entry_oberbegriff.grid_forget()
	entry_unterbegriff.grid_forget()
	entry_verwandterbegriff.grid_forget()
	speichern_button.grid_forget()
	name = askopenfilename()
	
#Label
label_ober=Label(root, text="Oberbegriff")
label_unter=Label(root, text="Unterbegriff")
label_verwandt=Label(root, text="Verwandterbegriff")
label_suche=Label(root)

#Entry
entry_suche = Entry(root)
entry_oberbegriff = Entry(root)
entry_unterbegriff = Entry(root)
entry_verwandterbegriff = Entry(root)

#Button
speichern_button=Button(root, text='Speichern',)
suchen_button=Button(root, text='Suchen',)


# Main Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu")
filemenu.add_command(label="Import")
filemenu.add_command(label="Export")
filemenu.add_command(label="Oeffnen", command=openfile)
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Schliessen", command=root.quit)
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