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
        if rel in self.dict.keys():
            self.dict[rel].append(term)
        else:
            self.dict[rel] = [term]

    def edit_term(self, rel, term, newterm):
        # for elem in self.dict[rel]:
        #     print "edit:" + elem
        #     if elem == term:
        #         self.dict[rel][self.dict[rel].index(elem)] = newterm
        for n, elem in enumerate(self.dict[rel]):
            if elem == term:
                self.dict[rel][n] = newterm

    def remove_term(self, rel, term):
        if rel in self.dict.keys():
            self.dict[rel].remove(term)

    def edit_rel(self, rel, term, newrel):
        self.remove_term(rel, term)
        self.add_term(term, newrel)

descriptorset1 = Descriptorset("Auto")

descriptorset1.add_term("Brumm", "VB")
descriptorset1.add_term("Toeff", "VB")
descriptorset1.edit_term("VB", "Toeff", "Tut")
descriptorset1.remove_term("VB", "Tut")
descriptorset1.edit_rel("VB", "Brumm", "OB")
print descriptorset1.get_terms()
