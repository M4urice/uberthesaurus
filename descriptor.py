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
			print "hey"
		else:
			for elem in self.dict.values(): # for schleife muss gestoppt werden!
				print self.dict
				if term not in elem:
					print "pups"
					if rel == "BS":
						print "Es sind bereits Relationen vorhanden. Bitte editiere den Deskriptor."
						#return False
					else:
						if "BS" in self.dict.keys():
							print "Dies ist kein Deskriptor. Bitte fuege die Relation bei BS ein."
							#return False
						else:
							if rel in self.dict.keys():
								if term not in self.dict[rel]:
									self.dict[rel].append(term)
							else:
								self.dict[rel] = [term]
							#return True
				else:
					print term + " existiert schon im Deskriptorsatz fuer " + self._name + "."
					#return False

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


dsetdict = {}


def create_dset(setname):
	if setname not in dsetdict.keys():
		dsetdict[setname] = Descriptorset(setname)
	else:
		print "Deskriptorset " + setname + " gibt es schon"
		
		



create_dset("Bla")
create_dset("Blub")
create_dset("Bubu")
print dsetdict.keys()

dsetdict["Bla"].add_term("Lala", "VB")
dsetdict["Bla"].add_term("Lala", "UB")
dsetdict["Bla"].add_term("Yo", "UB")
dsetdict["Bla"].add_term("No", "VB")
dsetdict["Bla"].add_term("Yes", "OB")
print dsetdict["Bla"].get_terms()
