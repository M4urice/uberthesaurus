from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile


class MyApp():
	def __init__(self, parent):
		#parent of MyApp
		self.myParent = parent
		# 2 listboxes for des and terms
		self.deslistbox = Listbox(parent)
		termlistbox = Listbox(parent)
		# a frame for changing elements
		self.myContainer1 = Frame(parent)
		# scrollbars for the listboxes
		scrollbar1 = Scrollbar(parent, orient=VERTICAL)
		scrollbar2 = Scrollbar(parent, orient=VERTICAL)
		scrollbar1.config(command=self.deslistbox.yview)
		scrollbar2.config(command=termlistbox.yview)
		#add buttons for interaktion with des
		add1_button=Button(parent, text='Hinzufuegen')
		edit1_button=Button(parent, text='Bearbeiten')
		del1_button=Button(parent, text="Loeschen")
		#add buttons for interaktion with terms
		add2_button=Button(parent, text='Hinzufuegen')
		edit2_button=Button(parent, text='Bearbeiten')
		del2_button=Button(parent, text="Loeschen")
		parent.columnconfigure(1, weight=1)
		parent.columnconfigure(3, pad=7)
		parent.rowconfigure(3, weight=1)
		parent.rowconfigure(5, pad=7)
		# place all GUI-elements
		add1_button.grid(row=0, sticky=NW, pady=4)
		edit1_button.grid(row=1, sticky=NW)
		del1_button.grid(row=2, sticky=NW, pady=4)
		self.deslistbox.grid(row=1, column=1, rowspan=3, sticky=NS)
		scrollbar1.grid(row=1, column=1, sticky=NE)
		#termlistbox.grid(row=1,column=2, sticky=NE)
		# scrollbar2.grid(row=0,column=4)
		# add2_button.grid(row=0,column=5)
		# edit2_button.grid(row=1,column=5)
		# del2_button.grid(row=2,column=5)
		#self.myContainer1.grid()



		# Menu
		menu = Menu(parent)
		parent.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label="Datei", menu=filemenu)
		# Main Menu
		filemenu.add_command(label="Neu")
		filemenu.add_command(label="Import")
		filemenu.add_command(label="Export")
		filemenu.add_command(label="Oeffnen")
		filemenu.add_command(label="Speichern")
		filemenu.add_command(label="Schliessen", command=parent.quit)
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

	def update_dlist(self, dlist):
		self.deslistbox.delete(0, END)
		for elem in dlist:
			self.deslistbox.insert(END, elem)

	def suche(self):
		self.myContainer1.destroy()
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
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


if __name__ == '__main__':

	root= Tk()
	myapp = MyApp(root)
	root.mainloop()