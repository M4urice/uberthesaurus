import json, pickle, csv

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
	tempdict = {}
	# make a dict tempdict with str from objectdict dsetdict
	for  elem in dsetdict:
		tempdict[elem] = dsetdict[elem].get_terms()
	# handle the export
	if format == "JSON":
		with open("%s.json"%filename,"w") as json_output:
			json.dump(tempdict,json_output)
	elif format == "CSV":
		with open('%s.csv'%filename, 'w') as new_data:
			writer = csv.writer(new_data, delimiter=';')
			writer.writerows(tempdict)
	elif format == "XML":
		pass
	else:
		print "Fehler! Falsches Format!"

def import_dsets():
	"""This imports descriptorsets from JSON, CSV or XML"""
	pass

# Testing:

create_dset("Bla")
create_dset("Blub")
create_dset("Bubu")
#print dsetdict.keys()


dsetdict["Bla"].add_term("Lala", "VB")
dsetdict["Bla"].add_term("Lala", "UB")
dsetdict["Bla"].add_term("Yo", "UB")
dsetdict["Bla"].add_term("No", "VB")
#print dsetdict["Bla"].add_term("Yes", "OB")


add("Bla", "Yolo", "UB")
#print dsetdict["Bla"].get_terms()
add("Yolo", "Totally", "OB")
#print dsetdict["Yolo"].get_terms()
export_dsets("JSON","lol")
export_dsets("CSV","lol")

#for elem in dsetdict:
#	print elem

#print sorted(dsetdict)
