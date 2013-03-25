
class Descriptor(object):
	"""docstring for Descriptor"""
	def __init__(self, name):
		self._name = name
		self.dict = {}

	def get_name(self):
		"""Returns the name of the descriptorset."""
		return self._name

	def set_name(self, newname):
		"""Replaces the old name with a new one."""
		self._name = newname

	def get_terms(self):
		"""Returns the descriptor-dictionary with its terms and relations."""
		return self.dict

	def add_term(self, term, rel):
		"""Adds a new term to a set if it doesnt exist already and if the rules of the thesaurus are met. Also returns True if the term was added successfully."""
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
		"""Replaces the old term with the corrected term."""
		# for elem in self.dict[rel]:
		# print "edit:" + elem
		# if elem == term:
		# self.dict[rel][self.dict[rel].index(elem)] = newterm
		for n, elem in enumerate(self.dict[rel]):
			if elem == term:
				self.dict[rel][n] = newterm

	def remove_term(self, rel, term):
		"""This removes a term from the descriptorset."""
		if rel in self.dict.keys():
			self.dict[rel].remove(term)
			self.remove_rel(rel)
			# to do: delete term in other sets.
			
	def remove_rel(self, rel):
		"""This deletes a relation."""
		if self.dict[rel] == []:
			del self.dict[rel]


	def edit_rel(self, rel, term, newrel):
		"""Used to edit a relation of a term. It removes the term from the old relation and adds it to the correct one."""
		self.remove_term(rel, term)
		self.add_term(term, newrel)


if __name__ == '__main__':
	# TEST Descriptor
	d1 = Descriptor("Baum")
	d1.add_term("Blatt", "VB")
	d1.add_term("Wald", "OB")
	d1.add_term("Pflanze", "OB")
	d1.add_term("Wurzel", "VB")
	d1.add_term("Frucht", "UB")
	#d1.dict["OB"].remove("Wald")
	d1.remove_term("OB", "Wald")
	d1.edit_rel("UB", "Frucht", "VB")
	print d1.get_terms()
