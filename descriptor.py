import json, csv

class Descriptorset(object):

	def __init__(self, name):
		self._name = name
		self.dict = {}

	def get_name(self):
		return self._name

	def set_name(self, newname):
		self._name = newname

	def get_terms(self):
		return self.dict

	def add_term(self, term, rel):
		if len(self.dict) == 0:
			self.dict[rel] = [term]
			return True
		else:
			for elem in self.dict.values():
				if term not in elem:
					if rel == "BS":
						print "Es sind bereits Relationen vorhanden. Bitte editiere den Deskriptor."
						return False
					else:
						if "BS" in self.dict.keys():
							print "Dies ist kein Deskriptor. Bitte fuege die Relation bei BS ein."
							return False
						else:
							if rel in self.dict.keys():
								if term not in self.dict[rel]:
									self.dict[rel].append(term)
							else:
								self.dict[rel] = [term]
							return True
				else:
					print term + " existiert schon im Deskriptorsatz fuer " + self._name + "."
					return False

	def edit_term(self, rel, term, newterm):
		# for elem in self.dict[rel]:
		# print "edit:" + elem
		# if elem == term:
		# self.dict[rel][self.dict[rel].index(elem)] = newterm
		for n, elem in enumerate(self.dict[rel]):
			if elem == term:
				self.dict[rel][n] = newterm

	def remove_term(self, rel, term):
		if rel in self.dict.keys():
			self.dict[rel].remove(term)

	def edit_rel(self, rel, term, newrel):
		self.remove_term(rel, term)
		self.add_term(term, newrel)

#################################################
# TODO: move to new .py file

dsetdict = {}


def create_dset(setname):
	"""This creates a new descriptorset which is added to the list dsetdict """
	if setname not in dsetdict.keys():
		dsetdict[setname] = Descriptorset(setname)
	else:
		print "Deskriptorset " + setname + " gibt es schon"

def add(name, term, rel):
	if dsetdict[name].add_term(term, rel):
		create_dset(term)

def export_dsets(format, filename):
	"""This exports all elements of the list dsetdict to JSON, CSV or XML"""
	# make a dict tempdict with str from objectdict dsetdict
	tempdict = {}
	for  elem in dsetdict:
		tempdict[elem] = dsetdict[elem].get_terms()
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
		pass
	else:
		print "Fehler! Unbekanntes Format!"


def import_dsets(format, filename):
	"""This imports descriptorsets from JSON, CSV or XML and returns a dict"""
	if format == "JSON":
		with open("%s.json"%filename,"r") as json_input:
			data = json.load(json_input)
			return data
	elif format == "CSV":
		data = {}
		with open('%s.csv'%filename, 'r') as csv_input:
			reader = csv.reader(csv_input, delimiter=";")
			for row in reader:
				pass
			return data
	elif format == "XML":
		pass
	else:
		print "Fehler! Unbekanntes Format!"

# Testing:

create_dset("Auto")
create_dset("Esel")
create_dset("Fahrrad")
#print dsetdict.keys()


dsetdict["Fahrrad"]. add_term("Klingel", "VB")
dsetdict["Fahrrad"].add_term("Fahrzeuge", "UB")
dsetdict["Fahrrad"].add_term("Mofa", "VB")
#print dsetdict["Fahrrad"].add_term("Yes", "OB")


add("Fahrrad", "Fortbewegungsmittel", "UB")
#print dsetdict["Fahrrad"].get_terms()
add("Esel", "Fortbewegungsmittel", "OB")
#print dsetdict["Yolo"].get_terms()
export_dsets("JSON", "lol")
export_dsets("CSV", "lol")
print import_dsets("JSON", "lol")
print import_dsets("CSV", "lol")
#for elem in dsetdict:
#	print elem

#print sorted(dsetdict)
