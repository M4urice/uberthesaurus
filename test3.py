from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()
# klasse machen: vergessen alle was gezeichnet wurde dann neu

class App:

    def __init__(self, top=None, master=None):
        if top is None:
            if master is None:
                top = Tk()
            else:
                top = Toplevel(master)
        self.top = top
        self.buttonframe = Frame(top)
        self.buttonframe.pack()
        self.panelframe = Frame(top,  borderwidth=2, relief=GROOVE)
        self.panelframe.pack(expand=1, fill=BOTH)
        self.panels = {}
        self.curpanel = None

    def addpanel(self, name, klass):
        button = Button(self.buttonframe, text=name,
                        command=lambda self=self, name=name: self.show(name))
        button.pack(side=LEFT)
        frame = Frame(self.panelframe)
        instance = klass(frame)
        self.panels[name] = (button, frame, instance)
        if self.curpanel is None:
            self.show(name)

    def show(self, name):
        (button, frame, instance) = self.panels[name]
        if self.curpanel:
            self.curpanel.pack_forget()
        self.curpanel = frame
        frame.pack(expand=1, fill="both")

class New:

    def __init__():
        message_text = "Willkommen auf unserem ersten Thesaurus Versuch!"
        msg = Message (root, text=message_text).pack()
class Suche:

    def __init__(self, frame):
        self.label(root, text="Suche").grid(row=0)
        self.entry_suche = Entry(root)
        self.entry_suche.grid(row=0, column=1)
        self.button(root, text='Suchen',).grid(row=1)

class NewDeskriptor:

    def NewDeskriptor(self, frame):
        self.label(root, text="Oberbegriff").grid(row=0)
        self.label(root, text="Unterbegriff").grid(row=1)
        self.label(root, text="Verwandterbegriff").grid(row=2)
        self.entry_oberbegriff = Entry(root)
        self.entry_oberbegriff.grid(row=0, column=1)
        self.entry_unterbegriff = Entry(root)
        self.entry_unterbegriff.grid(row=1, column=1)
        self.entry_verwandterbegriff = Entry(root)
        self.entry_verwandterbegriff.grid(row=2, column=1)
        self.Button(root, text='Speichern',).grid(row=4)
    
def openfile():
    name = askopenfilename()
    


# Main Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu", command=New)
filemenu.add_command(label="Import")
filemenu.add_command(label="Export")
filemenu.add_command(label="Oeffnen",command=openfile)
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Schliessen", command=root.quit)
# Deskrptor Menu
desmenu = Menu(menu)
menu.add_cascade(label="Deskritpor", menu=desmenu)
desmenu.add_command(label="Deskriptorliste")
desmenu.add_command(label="Suche",command=Suche)
# Verwaltung
vermenu = Menu(menu)
menu.add_cascade(label="Verwaltung", menu=vermenu)
vermenu.add_command(label="einfuegen", command=NewDeskriptor)
vermenu.add_command(label="loeschen")
vermenu.add_command(label="bearbeiten")


def main():
    app = App()
    app.addpanel ("desmenu", Suche)
    app.addpanel ("vermenu", NewDeskriptor)

root.mainloop()