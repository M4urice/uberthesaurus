from Tkinter import *
from thesaurus import Thesaurus
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
import tkSimpleDialog


class MyApp():
	"""Class for a GUI """


	def __init__(self, parent,thes=""):
		""" initialize the GUI with all visible elements and menus """


		#self.MyParent of MyApp
		self.MyParent = parent
		# import a thesaurus if given as an argument or create an empty one
		if thes is "":
			self.t1=Thesaurus("Thesaurusname")
		else:
			self.t1=thes

		# scrollbars for the listboxes
		self.scrollbar1 = Scrollbar(self.MyParent, orient=VERTICAL)
		self.scrollbar2 = Scrollbar(self.MyParent, orient=VERTICAL)
		# 2 listboxes for des and terms
		self.deslistbox = Listbox(self.MyParent, yscrollcommand=self.scrollbar1.set, exportselection=0)
		self.termlistbox = Listbox(self.MyParent, yscrollcommand=self.scrollbar2.set, exportselection=0)
		#self.termlistbox.bind("<<Double-Button-1>>", lambda event:self.deslistbox.select_set())
		self.deslistbox.bind("<<ListboxSelect>>", lambda event: self.update_tlist())

		# a frame for changing elements
		self.myContainer1 = Frame(self.MyParent)
		# add scrollbars for the listboxes
		self.scrollbar1.config(command=self.deslistbox.yview)
		self.scrollbar2.config(command=self.termlistbox.yview)
		#add buttons for interaktion with des
		self.add1_button=Button(self.MyParent, text='Hinzufuegen', command=self.add_des, width=10)
		self.edit1_button=Button(self.MyParent, text='Bearbeiten', command=self.edit_des, width=10)
		self.del1_button=Button(self.MyParent, text="Loeschen", command=self.del_des, width=10)
		#add buttons for interaktion with terms
		self.add2_button=Button(self.MyParent, text='Hinzufuegen', command=self.add_term, width=10)
		self.edit2_button=Button(self.MyParent, text='Bearbeiten', command=self.edit_term, width=10)
		self.del2_button=Button(self.MyParent, text="Loeschen", command=self.del_term, width=10)
		# confige the spacing
		self.MyParent.columnconfigure(1, weight=0)
		self.MyParent.columnconfigure(1, pad=0)
		self.MyParent.columnconfigure(2, pad=7)
		self.MyParent.columnconfigure(3, pad=7)
		self.MyParent.rowconfigure(1, weight=0)
		self.MyParent.rowconfigure(2, weight=0)
		self.MyParent.rowconfigure(3, weight=1)
		# place all GUI-elements
		self.add1_button.grid(row=1, column=0, pady=2, sticky=NW)
		self.edit1_button.grid(row=2, column=0, pady=2, sticky=NW)
		self.del1_button.grid(row=3, column=0, pady=2, sticky=NW)

		self.deslistbox.grid(row=1, column=1, rowspan=3, sticky=N)
		self.scrollbar1.grid(row=3, column=2, pady=3, sticky=N)
		self.termlistbox.grid(row=1,column=3, rowspan=3, sticky=N)
		self.scrollbar2.grid(row=3,column=4, pady=3, sticky=N)

		self.add2_button.grid(row=1,column=5, pady=2, sticky=NW)
		self.edit2_button.grid(row=2,column=5, pady=2, sticky=NW)
		self.del2_button.grid(row=3,column=5, pady=2, sticky=NW)
		# self.myContainer1.grid()

		# Menu
		self.menu = Menu(self.MyParent)
		self.MyParent.config(menu=self.menu)
		self.filemenu = Menu(self.menu)
		self.menu.add_cascade(label="Datei", menu=self.filemenu)
		# Main Menu
		self.filemenu.add_command(label="Neu", command=self.new_thes)
		self.filemenu.add_command(label="Verbinden", command=self.t1.connect)
		self.filemenu.add_command(label="Import", command=self.importdatei)
		self.filemenu.add_command(label="Export", command=self.export)
		self.filemenu.add_command(label="Schliessen", command=self.exit_prog)


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
			for key,value in sorted(tlist.iteritems()):
				for elem in value:
					self.termlistbox.insert(END, key + " "+elem)
			self.termlistbox.select_set(0)
		else:
			self.termlistbox.delete(0, END)
			self.termlistbox.select_set(0)


	def del_des(self):
		""" Deletes the selected element of the listbox for the descriptors"""

		if self.deslistbox.curselection() != ():
			self.t1.delete_entries(self.deslistbox.get(self.deslistbox.curselection()))
			self.update_dlist()
			self.update_tlist()


	def add_des(self):
		""" Deletes the selected element of the listbox for the relations and terms"""

		self.des = tkSimpleDialog.askstring("Deskriptor hinzufuegen", "Deskriptor:")
		if self.des is not None:
			self.t1.create_entries(des)
			self.update_dlist()
			self.update_tlist()


	def edit_des(self):
		"""Opens up a dialog for descriptor editing"""

		self.des = tkSimpleDialog.askstring("Deskriptor bearbeiten", "Bearbeiten:")
		if self.des is not None:
			self.t1.edit_entries(self.deslistbox.get(self.deslistbox.curselection()),des)
			self.update_dlist()
			self.update_tlist()


	def del_term(self):
		""" Deletes the selected term from the termlist """

		if self.termlistbox.curselection() != ():
			self.term=self.termlistbox.get(self.termlistbox.curselection())
			self.term=term.split(" ")
			self.t1.entries[self.deslistbox.get(self.deslistbox.curselection())].remove_term(self.term[0],self.term[1])
			self.update_tlist()


	def add_term(self):
		"""Opens up a dialog for term adding"""

		self.term = tkSimpleDialog.askstring("Term hinzufuegen", "Rel Term:")
		if self.term is not None:
			self.term=self.term.split(" ")
			self.t1.add(self.deslistbox.get(self.deslistbox.curselection()), self.term[1], self.term[0])
			self.update_dlist()
			self.update_tlist()


	def edit_term(self):
		"""Opens up a dialog for term/rel editing"""

		self.rel_term=tkSimpleDialog.askstring("Term bearbeiten", "Rel Term")
		if self.rel_term is not None:
			self.rel_term=self.rel_term.split(" ")
			self.rel_term_old=self.termlistbox.get(self.termlistbox.curselection()).split(" ")
			if self.rel_term[0]!=self.rel_term_old[0]:
				self.t1.entries[self.deslistbox.get(self.deslistbox.curselection())].edit_rel(str(self.rel_term_old[0]), str(self.rel_term_old[1]), str(self.rel_term[0]))
			if self.rel_term[1]!=self.rel_term_old[1]:
				self.t1.entries[self.deslistbox.get(self.deslistbox.curselection())].edit_term(str(self.rel_term_old[0]), str(self.rel_term_old[1]), str(self.rel_term[1]))
			self.update_dlist()
			self.update_tlist()


	def exit_prog(self):
		"""Shows the export dialog and exits the program"""

		#tkSimpleDialog
		self.export()
		self.MyParent.destroy()


	def new_thes(self):
		"""Clears all entries of the thesaurus"""

		self.t1.entries={}
		self.update_dlist()
		self.update_tlist()


	def export(self):
		"""Extracts the filetype and calls the real export method if a valid filename is given"""

		self.formats = [
		('Comma-separated values','*.csv'),
		('JavaScript Object Notation','*.json'),
		('Extensible Markup Language','*.xml'),
    	]
		self.filename = asksaveasfilename(filetypes=self.formats, title="Den Thesaurus exportieren", defaultextension=".xml")
		if len(self.filename)>0:
			self.t1.export_thesaurus(self.filename)
		else:
			print "Keine Datei angegeben."


	def importdatei(self):
		"""Extracts the filetype and calls the real import method if a valid filename is given"""

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