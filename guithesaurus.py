from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile


class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		#Label
		#label_ober=Label(root, text="Oberbegriff")
		#label_unter=Label(root, text="Unterbegriff")
		#label_verwandt=Label(root, text="Verwandterbegriff")
		#self.label_suche=Label(text="Suche:")
		#label_einfueg=Label(root, text="Einfuegen:")
		#label_als=Label(root, text="Als:")

		#Entry
		#entry_suche = Entry(root)
		#entry_oberbegriff = Entry(root)
		#entry_unterbegriff = Entry(root)
		#entry_verwandterbegriff = Entry(root)
		#entry_einfueg = Entry(root)
		#entry_als = Entry(root)

		#Button
		#speichern_button=Button(root, text='Speichern')
		#suchen_button=Button(root, text='Suchen')
		#einfueg_button=Button(root, text="Einfuegen")
		
		
		# Menu
		menu = Menu(root)
		root.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label="Datei", menu=filemenu)
		# Main Menu
		filemenu.add_command(label="Neu")
		filemenu.add_command(label="Import")
		filemenu.add_command(label="Export")
		filemenu.add_command(label="Oeffnen")
		filemenu.add_command(label="Speichern")
		filemenu.add_command(label="Schliessen", command=root.quit)
        # Deskrptor Menu
		desmenu = Menu(menu)
		menu.add_cascade(label="Deskritpor", menu=desmenu)
		desmenu.add_command(label="Deskriptorliste")
		desmenu.add_command(label="Suche", command=self.suche)
        # Verwaltung
		vermenu = Menu(menu)
		menu.add_cascade(label="Verwaltung", menu=vermenu)
		vermenu.add_command(label="einfuegen", command=self.newdeskriptor)
		vermenu.add_command(label="loeschen")
		vermenu.add_command(label="bearbeiten")


	def suche(self):
		self.myContainer1.destroy()
		self.label_suche = Label(self.myContainer1, text="Suche:")
		self.label_suche.grid(row=0)
		self.entry_suche = Entry(self.myContainer1)
		self.entry_suche.grid(row=0, column=1)
		self.suchen_button=Button(self.myContainer1, text='Suchen')
		self.suchen_button.grid(row=1)


	def newdeskriptor(self):
		self.myContainer1.destroy()
		self.label_ober.grid(row=0)
		self.label_unter.grid(row=1)
		self.label_verwandt.grid(row=2)
		self.entry_oberbegriff.grid(row=0, column=1)
		self.entry_unterbegriff.grid(row=1, column=1)
		self.entry_verwandterbegriff.grid(row=2, column=1)
		self.speichern_button.grid(row=4)



root= Tk()
myapp = MyApp(root)
root.mainloop()