from Tkinter import *
from thesaurus import Thesaurus
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile


class MyApp():
	def __init__(self, parent,thes=""):
		#self.MyParent of MyApp
		self.MyParent = parent
		# 2 listboxes for des and terms
		self.deslistbox = Listbox(self.MyParent)
		self.termlistbox = Listbox(self.MyParent)
		# a frame for changing elements
		self.myContainer1 = Frame(self.MyParent)
		# scrollbars for the listboxes
		scrollbar1 = Scrollbar(self.MyParent, orient=VERTICAL)
		scrollbar2 = Scrollbar(self.MyParent, orient=VERTICAL)
		scrollbar1.config(command=self.deslistbox.yview)
		scrollbar2.config(command=self.termlistbox.yview)
		#add buttons for interaktion with des
		add1_button=Button(self.MyParent, text='Hinzufuegen', command=self.add_window)
		edit1_button=Button(self.MyParent, text='Bearbeiten', command=self.edit_window)
		del1_button=Button(self.MyParent, text="Loeschen", command=self.del_des)
		#add buttons for interaktion with terms
		add2_button=Button(self.MyParent, text='Hinzufuegen', command=self.add_window)
		edit2_button=Button(self.MyParent, text='Bearbeiten', command=self.edit_window)
		del2_button=Button(self.MyParent, text="Loeschen", command=self.del_term)
		# confige the spacing
		self.MyParent.columnconfigure(1, weight=1)
		self.MyParent.columnconfigure(2, pad=7)
		self.MyParent.rowconfigure(3, weight=1)
		self.MyParent.rowconfigure(5, pad=7)
		# place all GUI-elements
		add1_button.grid(row=1, sticky=NW, pady=4)
		edit1_button.grid(row=2, sticky=NW)
		del1_button.grid(row=3, sticky=NW, pady=4)

		self.deslistbox.grid(row=1, column=1, rowspan=3, sticky=NS)
		scrollbar1.grid(row=1, column=1, sticky=NE)
		self.termlistbox.grid(row=1,column=2, sticky=NE)
		scrollbar2.grid(row=0,column=4)

		add2_button.grid(row=1,column=5)
		edit2_button.grid(row=2,column=5)
		del2_button.grid(row=3,column=5)
		# self.myContainer1.grid()

		# Menu
		menu = Menu(self.MyParent)
		self.MyParent.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label="Datei", menu=filemenu)
		# Main Menu
		filemenu.add_command(label="Neu")
		filemenu.add_command(label="Import")
		filemenu.add_command(label="Export")
		filemenu.add_command(label="Oeffnen")
		filemenu.add_command(label="Speichern")
		filemenu.add_command(label="Schliessen", command=self.exit_prog)
        # Deskrptor Menu
		desmenu = Menu(menu)
		menu.add_cascade(label="Deskritpor", menu=desmenu)
		desmenu.add_command(label="Deskriptorliste")
		desmenu.add_command(label="Suche", command=self.suche)
        # Verwaltung
		vermenu = Menu(menu)
		menu.add_cascade(label="Verwaltung", menu=vermenu)
		vermenu.add_command(label="einfuegen")
		vermenu.add_command(label="loeschen")
		vermenu.add_command(label="bearbeiten")


		# import a thesaurus if given as an argument
		if thes is "":
			self.t1=Thesaurus("Fahrzeugthesaurus")
		else:
			self.t1=thes

		self.t1.create_dset("Auto")
		self.t1.create_dset("Fahrrad")
		self.t1.thesaurus["Auto"].add_term("Rad", "VB")
		self.t1.thesaurus["Auto"].add_term("Fahrzeuge", "OB")
		self.t1.thesaurus["Auto"].add_term("Lenkrad", "VB")
		self.t1.create_dset("Esel")
		self.t1.create_dset("Motorrad")
		self.t1.create_dset("Skateboard")
		self.t1.create_dset("Reifen")
		for elem in range(100):
			self.t1.create_dset("Des%s" %elem)
		self.update_dlist(self.t1.thesaurus.keys())
		self.update_tlist()


	def update_dlist(self, dlist):
		""" Updates the listbox for the descriptors"""
		self.deslistbox.delete(0, END)
		for elem in sorted(dlist):
			self.deslistbox.insert(END, elem)
		self.deslistbox.activate(1)

	def update_tlist(self):
		""" Updates the listbox for the relations and terms"""
		if self.deslistbox.curselection()!=():
			tlist=self.t1.thesaurus[self.deslistbox.get(self.deslistbox.curselection())].get_terms()
		else:
			tlist=self.t1.thesaurus[self.deslistbox.get(0)].get_terms()
		self.termlistbox.delete(0, END)
		print tlist
		for key,value in tlist.iteritems():
				self.termlistbox.insert(END, key+str(value))

	def add_window(self):
		pass

	def edit_window(self):
		pass

	def del_des(self):
		""" Deletes the selected element of the listbox for the descriptors"""
		if self.deslistbox.curselection() != ():
			self.deslistbox.delete(self.deslistbox.curselection())
			#self.t1.thesaurus.removedes(self.deslistbox.index(self.deslistbox.curselection()))

	def add_des(self,des):
		""" Deletes the selected element of the listbox for the relations and terms"""
		self.deslistbox.insert(END, des)

	def edit_des(self):
		pass

	def del_term(self):
		pass

	def add_term(self,des):
		pass

	def edit_term(self):
		pass

	def exit_prog(self):
		self.save_thes()
		self.MyParent.destroy()
	def save_thes(self):
		pass

	def suche(self):
		self.myContainer1.destroy()
		self.myContainer1 = Frame(self.MyParent)
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
	t1=Thesaurus("Fahrzeugthesaurus")

	# DSET TESTS
	# t1.create_dset("Auto")
	# t1.create_dset("Esel")
	# t1.create_dset("Fahrrad")
	# t1.thesaurus["Fahrrad"].add_term("Klingel", "VB")
	# t1.thesaurus["Fahrrad"].add_term("Fahrzeuge", "UB")
	# t1.thesaurus["Fahrrad"].add_term("Mofa", "VB")
	# #no me gusta
	# #print t1.thesaurus["Fahrrad"].add_term("Yes", "OB")
	# t1.add("Fahrrad", "Fortbewegungsmittel", "UB")
	#t1.add("Esel", "Fortbewegungsmittel", "OB")

	# IMPORT/EXPORT
	# t1.export_thesaurus("JSON", "lol")
	# t1.export_thesaurus("CSV", "lol")
	# t1.export_thesaurus("XML", "lol")
	# t1.import_dsets("JSON", "lol")
	# t1.import_dsets("CSV", "lol")
	# t1.import_dsets("XML", "lol")

	# GUI TESTS
	root= Tk()
	myapp = MyApp(root,t1)
	root.mainloop()