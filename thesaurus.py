import json, csv
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
from descriptor import Descriptor

class Thesaurus(object):
	"""docstring for descriptorset"""
	def __init__(self, name):
		self.name = name
		self.thesaurus = {}


	def create_dset(self, setname):
		"""This creates a new descriptorset which is added to the dict "thesaurus" """
		if setname not in self.thesaurus.keys():
			self.thesaurus[setname] = Descriptor(setname)
		else:
			print "Deskriptorset " + setname + " gibt es schon"

	def edit_dset(self, setname, newname):
		"""Edits the name of a descriptorset."""
		self.thesaurus[setname].set_name(newname)
		#TODO edit setname in self.thesaurus

	def add(self, name, term, rel):
		"""This forwards its variables to add_term and also checks whether a new term has been created successfully. If so, it will create a set for the new term."""
		if self.thesaurus[name].add_term(term, rel):
			self.create_dset(term)

	def export_thesaurus(self, format, filename):
		"""This exports all elements of the dict "self.thesaurus" to JSON, CSV or XML"""
		# make a dict tempdict with str from objectdict self.thesaurus
		tempdict = {}
		for  elem in self.thesaurus:
			tempdict[elem] = self.thesaurus[elem].get_terms()
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
			xmlthesaurus = Element( "Deskriptorsets")
			for name, terms in tempdict.iteritems():
				xmldset = SubElement(xmlthesaurus, name)
				for elem in terms:
					xmlelem = SubElement(xmldset, elem)
					xmlelem.text=""
					for elm in terms[elem]:
						xmlelem.text +=elm+", "
			## print xml
			xml = tostring(xmlthesaurus)
			dom = parseString(xml)
			print dom.toprettyxml('    ')
		else:
			print "Fehler! Unbekanntes Format!"


	def import_dsets(self, format, filename):
		"""This imports descriptorsets from JSON, CSV or XML and returns a dict"""
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

if __name__ == '__main__':
	t1=Thesaurus("Fahrzeugthesaurus")

	# DSET TESTS
	t1.create_dset("Auto")
	t1.create_dset("Esel")
	t1.create_dset("Fahrrad")
	t1.thesaurus["Fahrrad"].add_term("Klingel", "VB")
	t1.thesaurus["Fahrrad"].add_term("Fahrzeuge", "UB")
	t1.thesaurus["Fahrrad"].add_term("Mofa", "VB")
	#no me gusta
	print t1.thesaurus["Fahrrad"].add_term("Yes", "OB")
	t1.add("Fahrrad", "Fortbewegungsmittel", "UB")
	t1.add("Esel", "Fortbewegungsmittel", "OB")



	# IMPORT/EXPORT
	t1.export_thesaurus("JSON", "lol")
	t1.export_thesaurus("CSV", "lol")
	t1.export_thesaurus("XML", "lol")
	t1.import_dsets("JSON", "lol")
	t1.import_dsets("CSV", "lol")
	t1.import_dsets("XML", "lol")