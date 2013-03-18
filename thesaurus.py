import json, csv
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
from descriptor import Descriptor

class Thesaurus(object):
	"""docstring for Thesaurus"""
	def __init__(self, name):
		self.name = name
		self.entries = {}


	def create_entries(self, setname):
		"""This creates a new descriptor which is added to the dict "entries" """
		if setname not in self.entries.keys():
			self.entries[setname] = Descriptor(setname)
		else:
			print "Deskriptorset " + setname + " gibt es schon"

	def edit_entries(self, setname, newname):
		"""Edits the name of a descriptorset."""
		self.entries[newname] = self.entries[setname]
		self.entries[newname].set_name(newname)
		self.delete_entries(setname)
		#to do: edit all other relations to this set


	def delete_entries(self, setname):
		"""Delete reference to a set."""
		del self.entries[setname]
		#to do: remove all other connections to this set

	def add(self, name, term, rel):
		"""This forwards its variables to add_term and also checks whether a new term has been created successfully. If so, it will create a set for the new term."""
		if self.entries[name].add_term(term, rel):
			self.create_entries(term)

	def export_thesaurus(self, format, filename):
		"""This exports all elements of the dict "self.entries" to JSON, CSV or XML"""
		# make a dict tempdict with str from objectdict self.entries
		tempdict = {}
		for  elem in self.entries:
			tempdict[elem] = self.entries[elem].get_terms()
		# handle the export
		if format == "JSON":
			with open("%s.json"%filename,"w") as json_output:
				json.dump(tempdict,json_output)
		elif format == "CSV":
				with open('%s.csv'%filename, 'w') as csv_output:
					writer = csv.writer(csv_output, delimiter=";")
					writer.writerow(tempdict.keys())
					writer.writerow(tempdict.values())
		elif format == "XML":
			xmlentries = Element( "Deskriptorsets")
			for name, terms in tempdict.iteritems():
				xmlentries = SubElement(xmlentries, name)
				for elem in terms:
					xmlelem = SubElement(xmlentries, elem)
					xmlelem.text=""
					for elm in terms[elem]:
						xmlelem.text +=elm+", "
			## print xml
			xml = tostring(xmlentries)
			dom = parseString(xml)
			print dom.toprettyxml('    ')
		else:
			print "Fehler! Unbekanntes Format!"


	def import_thesaurus(self, format, filename):
		"""This imports thesauri from JSON, CSV or XML and returns a dict"""
		if format == "JSON":
			with open("%s.json"%filename,"r") as json_input:
				data = json.load(json_input)
				#print "JSON: ", data
		elif format == "CSV":
			data = {}
			with open('%s.csv'%filename, 'r') as csv_input:
				reader = csv.reader(csv_input, delimiter=";")
				for row in reader:
					keys = row
					values= reader.next()
					for elem in range(len(keys)):
						data[keys[elem]]=values[elem]
		elif format == "XML":
			pass
		else:
			print "Fehler! Unbekanntes Format!"


	def connect(self):
		"""Finds relations between descriptorsets and connects them."""


if __name__ == '__main__':
	t1=Thesaurus("Fahrzeugthesaurus")

	# entries TESTS
	t1.create_entries("Auto")
	t1.create_entries("Esel")
	t1.create_entries("Fahrrad")
	t1.entries["Fahrrad"].add_term("Klingel", "VB")
	t1.entries["Fahrrad"].add_term("Fahrzeuge", "UB")
	t1.entries["Fahrrad"].add_term("Mofa", "VB")
	#no me gusta
	print t1.entries["Fahrrad"].add_term("Yes", "OB")
	t1.add("Fahrrad", "Fortbewegungsmittel", "UB")
	t1.add("Esel", "Fortbewegungsmittel", "OB")



	# IMPORT/EXPORT
	t1.export_thesaurus("JSON", "lol")
	t1.export_thesaurus("CSV", "lol")
	t1.export_thesaurus("XML", "lol")
	t1.import_thesaurus("JSON", "lol")
	t1.import_thesaurus("CSV", "lol")
	t1.import_thesaurus("XML", "lol")