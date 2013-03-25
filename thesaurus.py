import json, csv
import os.path
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from descriptor import Descriptor

class Thesaurus(object):
	"""docstring for Thesaurus"""
	def __init__(self, name):
		self.name = name
		self.entries = {}


	def create_entries(self, setname):
		"""Creates a new descriptor which is added to the dict "entries" """
		if setname not in self.entries.keys():
			self.entries[setname] = Descriptor(setname)
		#else:
		#	print "Eintrag " + setname + " gibt es schon."

	def edit_entries(self, setname, newname):
		"""Edits the name of a descriptorset."""
		self.entries[newname] = self.entries[setname]
		self.entries[newname].set_name(newname)
		for object in self.entries:
			self.entries[object].edit_term_norel(setname, newname)
		self.delete_entries(setname)


	def delete_entries(self, setname):
		"""Deletes reference to a set."""
		for object in self.entries:
			self.entries[object].remove_term_norel(setname)
		del self.entries[setname]

	def add(self, name, term, rel):
		"""	This forwards its variables to add_term and also checks
		whether a new term has been created successfully.
		If so, it will create a set for the new term."""
		if self.entries[name].add_term(term, rel):
			self.create_entries(term)

	def export_thesaurus(self, filename):
		"""Exports all entries of the thesaurus to JSON, CSV or XML"""
		extension = os.path.splitext(filename)[1]
		tempdict = {}
		for  elem in self.entries:
			tempdict[elem] = self.entries[elem].get_terms()

		if extension == ".json":
			with open(filename,"w") as json_output:
				#indent=5 for pretty print
				json.dump(tempdict, json_output, sort_keys=True, indent=5)

		elif extension == ".csv":
			with open(filename, 'w') as csv_output:
					writer = csv.writer(csv_output, delimiter=";")
					writer.writerow(tempdict.keys())
					writer.writerow(tempdict.values())

		elif extension == ".xml" or extension == ".xhtml":
			entries = ET.Element( "data")
			for name, terms in tempdict.iteritems():
				xmlentries = ET.SubElement(entries, "descriptor")
				xmlentries.set("name",name)
				for rel in terms:
					xmlelem = ET.SubElement(xmlentries, "relation")
					xmlelem.set("name",rel)
					for term in terms[rel]:
						xmlterm=ET.SubElement(xmlelem, "term")
						xmlterm.text=term
			#pretty-print
			self.indent(entries,2)
			tree = ET.ElementTree(entries)

			tree.write(filename)

		else:
			print "Fehler! Unbekanntes Format!"


	# method taken from  http://effbot.org/zone/element.htm
	def indent(self, elem, level=0):
		i = "\n" + level*"  "
		if len(elem):
			if not elem.text or not elem.text.strip():
				elem.text = i + "  "
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
			for elem in elem:
				self.indent(elem, level+1)
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
		else:
			if level and (not elem.tail or not elem.tail.strip()):
				elem.tail = i


	def import_thesaurus(self, filename):
		"""Imports thesauri from JSON, CSV or XML and returns a dict"""
		extension = os.path.splitext(filename)[1]
		if extension == ".json":
			self.entries={}
			with open(filename,"r") as json_input:
				tempdict = json.load(json_input)
				for entr,descr in tempdict.iteritems():
					self.create_entries(entr)
					if descr !={}:
						for rel,termlist in descr.iteritems():
							for term in termlist:
								self.entries[entr].add_term(term, rel)


		elif extension == ".csv":
			self.entries={}
			with open(filename, 'r') as csv_input:
				reader = csv.reader(csv_input, delimiter=";")
				row1 = reader.next()
				row2 = reader.next()
				for i in range(len(row1)):
					self.create_entries(row1[i])
					row2[i]=row2[i].split("],")
					for elem in row2[i]:
						elem=elem.translate(None,"{'[ ]}").split(":")
						if elem[0]!="":
							rel=elem[0]
							terms=elem[1].split(",")
							for term in terms:
								self.add(row1[i], term, rel)

		elif extension == ".xml" or extension== ".xhtml":
			self.entries={}
			tree=ET.parse(filename)
			root=tree.getroot()
			for descriptor in root:
				self.create_entries(descriptor.attrib.values()[0])
				for relation in descriptor:
					for term in relation:
						self.add(descriptor.attrib.values()[0], term.text, relation.attrib.values()[0])

		else:
			print "Fehler! Unbekanntes Format!"


	def connect(self):
		"""Finds relations between descriptorsets and connects them."""
		for entry in self.entries:
			for rel in self.entries[entry].dict.keys():
				if rel == "OB":
					for term in self.entries[entry].dict[rel]:
						self.add(term, entry, "UB")
				elif rel == "UB":
					for term in self.entries[entry].dict[rel]:
						self.add(term, entry, "OB")
				elif rel == "VB":
					for term in self.entries[entry].dict[rel]:
						self.add(term, entry, "VB")
				elif rel == "BS":
					for term in self.entries[entry].dict[rel]:
						self.add(term, entry, "BF")
				elif rel == "BF":
					for term in self.entries[entry].dict[rel]:
						self.add(term, entry, "BS")
				else:
					print "There are faulty relations in this thesaurus."
						
						
					

if __name__ == '__main__':
	t1=Thesaurus("Fahrzeugthesaurus")

	# entries TESTS
	t1.create_entries("Auto")
	t1.create_entries("Esel")
	t1.create_entries("Fahrrad")
	t1.create_entries("Bewegung")
	t1.add("Fahrrad", "Klingel", "UB")
	t1.add("Fahrrad", "Speiche", "UB")
	t1.add("Fahrrad", "Fortbewegungsmittel", "OB")
	t1.add("Esel", "Fortbewegungsmittel", "OB")
	t1.add("Bewegung", "Fortbewegungsmittel", "VB")
	#print t1.entries["Fahrrad"].add_term("Yes", "OB")
	print t1.entries["Fahrrad"].get_terms()
	t1.edit_entries("Fortbewegungsmittel", "Transport")
	print t1.entries["Fahrrad"].get_terms()
	t1.connect()
	print t1.entries["Transport"].get_terms()
	





	# # IMPORT/EXPORT
	# t1.export_thesaurus("JSON", "testfile")
	# t1.export_thesaurus("CSV", "testfile")
	# t1.export_thesaurus("XML", "testfile")
	# t1.import_thesaurus("JSON", "testfile")

	# t1.import_thesaurus("CSV", "testfile")
	# t1.import_thesaurus("XML", "testfile")
	# for elem in t1.entries:
	# 	print elem,":",t1.entries[elem].get_terms()
