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
		if term not in self.dict.values():
			if rel in self.dict.keys():
				self.dict[rel].append(term)
			else:
				self.dict[rel] = [term]
			return True
		else:
			return False
			#print "Dieser Term existiert schon im Deskriptorsatz für " + self._name + "."

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
create_dset("Bubu")
print dsetdict.keys()
dsetdict["Bla"].add_term("Lala", "VB")
print dsetdict["Bla"].get_terms()
