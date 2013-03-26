from Tkinter import *
from thesaurus import Thesaurus
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
import tkSimpleDialog


class MyApp():
	def __init__(self, parent,thes=""):

		#self.MyParent of MyApp
		self.MyParent = parent
		# import a thesaurus if given as an argument or create an empty one
		if thes is "":
			self.t1=Thesaurus("Fahrzeugthesaurus")
		else:
			self.t1=thes

		# scrollbars for the listboxes
		scrollbar1 = Scrollbar(self.MyParent, orient=VERTICAL)
		scrollbar2 = Scrollbar(self.MyParent, orient=VERTICAL)
		# 2 listboxes for des and terms
		self.deslistbox = Listbox(self.MyParent, yscrollcommand=scrollbar1.set, exportselection=0)
		self.termlistbox = Listbox(self.MyParent, yscrollcommand=scrollbar2.set, exportselection=0)
		#self.termlistbox.bind("<<Double-Button-1>>", lambda event:self.deslistbox.select_set())
		self.deslistbox.bind("<<ListboxSelect>>", lambda event: self.update_tlist())

		# a frame for changing elements
		self.myContainer1 = Frame(self.MyParent)
		# add scrollbars for the listboxes
		scrollbar1.config(command=self.deslistbox.yview)
		scrollbar2.config(command=self.termlistbox.yview)
		#add buttons for interaktion with des
		add1_button=Button(self.MyParent, text='Hinzufuegen', command=self.add_window, width=10)
		edit1_button=Button(self.MyParent, text='Bearbeiten', command=self.edit_window, width=10)
		del1_button=Button(self.MyParent, text="Loeschen", command=self.del_des, width=10)
		#add buttons for interaktion with terms
		add2_button=Button(self.MyParent, text='Hinzufuegen', command=self.add_window, width=10)
		edit2_button=Button(self.MyParent, text='Bearbeiten', command=self.edit_window, width=10)
		del2_button=Button(self.MyParent, text="Loeschen", command=self.del_term, width=10)
		# confige the spacing
		self.MyParent.columnconfigure(1, weight=0)
		self.MyParent.columnconfigure(1, pad=0)
		self.MyParent.columnconfigure(2, pad=7)
		self.MyParent.columnconfigure(3, pad=7)
		self.MyParent.rowconfigure(1, weight=0)
		self.MyParent.rowconfigure(2, weight=0)
		self.MyParent.rowconfigure(3, weight=1)
		# place all GUI-elements
		add1_button.grid(row=1, column=0, pady=2, sticky=NW)
		edit1_button.grid(row=2, column=0, pady=2, sticky=NW)
		del1_button.grid(row=3, column=0, pady=2, sticky=NW)

		self.deslistbox.grid(row=1, column=1, rowspan=3, sticky=N)
		scrollbar1.grid(row=3, column=2, pady=3, sticky=N)
		self.termlistbox.grid(row=1,column=3, rowspan=3, sticky=N)
		scrollbar2.grid(row=3,column=4, pady=3, sticky=N)

		add2_button.grid(row=1,column=5, pady=2, sticky=NW)
		edit2_button.grid(row=2,column=5, pady=2, sticky=NW)
		del2_button.grid(row=3,column=5, pady=2, sticky=NW)
		# self.myContainer1.grid()

		# Menu
		menu = Menu(self.MyParent)
		self.MyParent.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label="Datei", menu=filemenu)
		# Main Menu
		filemenu.add_command(label="Neu")
		filemenu.add_command(label="Verbinden", command=self.t1.connect)
		filemenu.add_command(label="Import", command=self.importdatei)
		filemenu.add_command(label="Export", command=self.export)
		filemenu.add_command(label="Schliessen", command=self.exit_prog)
		# TESTING
		self.t1.create_entries("Auto")
		self.t1.create_entries("Fahrrad")
		self.t1.add("Auto", "Rad", "VB")
		self.t1.add("Auto", "Fahrzeuge", "OB")
		self.t1.add("Auto", "Lenkrad", "VB")
		self.t1.add("Fahrrad", "Rad", "VB")
		self.t1.add("Fahrrad", "Fahrzeuge", "OB")
		self.t1.add("Fahrrad", "Lenkrad", "VB")
		self.t1.create_entries("Esel")
		self.t1.create_entries("Motorrad")
		self.t1.create_entries("Skateboard")
		self.t1.create_entries("Reifen")
		for elem in range(100):
			self.t1.create_entries("Des%s" %elem)
		self.update_dlist()
		self.update_tlist()


	def update_dlist(self):
		""" Updates the listbox for the descriptors"""
		self.deslistbox.delete(0, END)
		for elem in sorted(self.t1.entries.keys()):
			self.deslistbox.insert(END, elem)
		self.deslistbox.select_set(0)


	def update_tlist(self):
		""" Updates the listbox for the relations and terms"""
		if self.t1.entries!={}:
			if self.deslistbox.curselection()!=():
				tlist=self.t1.entries[self.deslistbox.get(self.deslistbox.curselection())].get_terms()
			else:
				tlist=self.t1.entries[self.deslistbox.get(0)].get_terms()
			self.termlistbox.delete(0, END)
			for key,value in tlist.iteritems():
				for elem in value:
					self.termlistbox.insert(END, key + " "+elem)
			self.termlistbox.select_set(0)


	def add_window(self):
		tkSimpleDialog.askstring("Hinzufuegen", "Hinzufuegen:")
		
	def edit_window(self):
		tkSimpleDialog.askstring("Bearbeiten", "Bearbeiten:")


	def del_des(self):
		""" Deletes the selected element of the listbox for the descriptors"""
		if self.deslistbox.curselection() != ():
			self.deslistbox.delete(self.deslistbox.curselection())
			#self.t1.entries.removedes(self.deslistbox.index(self.deslistbox.curselection()))


	def add_des(self,des):
		""" Deletes the selected element of the listbox for the relations and terms"""
		self.deslistbox.insert(END, des)


	def edit_des(self):
		pass


	def del_term(self):
		""" Deletes the selected element of the listbox for the descriptors"""
		if self.termlistbox.curselection() != ():
			self.termlistbox.delete(self.termlistbox.curselection())


	def add_term(self,des): 
		pass


	def edit_term(self):
		pass


	def exit_prog(self):
		self.export()
		self.MyParent.destroy()


	def export(self):
		formats = [
		('Comma-separated values','*.csv'),
		('JavaScript Object Notation','*.json'),
		('Extensible Markup Language','*.xml'),
    	]
		self.filename = asksaveasfilename(filetypes=formats, title="Den Thesaurus exportieren", defaultextension=".xml")
		if len(self.filename)>0:
			self.t1.export_thesaurus(self.filename)
		else:
			print "Keine Datei angegeben."

	def importdatei(self):
		self.filename = askopenfilename()
		if len(self.filename)>0:
			self.t1.import_thesaurus(self.filename)
			self.update_dlist()
		else:
			print "Keine Datei angegeben."





if __name__ == '__main__':
	t1=Thesaurus("Fahrzeugthesaurus")
	root= Tk()
	myapp = MyApp(root,t1)
	root.mainloop()