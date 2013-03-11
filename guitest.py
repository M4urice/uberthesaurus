from Tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent, background="red")
        self.myContainer1.pack()

        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Datei", menu=filemenu)
        filemenu.add_command(label="Neu")
        filemenu.add_command(label="Import")
        filemenu.add_command(label="Export")
        filemenu.add_command(label="Oeffnen")
        filemenu.add_command(label="Speichern")
        filemenu.add_command(label="Schliessen", command=root.quit)
        # Deskrptor Menu
        desmenu = Menu(menu)
        menu.add_cascade(label="Deskritpor", menu=desmenu)
        desmenu.add_command(label="Deskriptorliste")
        desmenu.add_command(label="Suche")
        # Verwaltung
        vermenu = Menu(menu)
        menu.add_cascade(label="Verwaltung", menu=vermenu)
        vermenu.add_command(label="einfuegen")
        vermenu.add_command(label="loeschen")
        vermenu.add_command(label="bearbeiten")
        self.button1 = Button(self.myContainer1, command=self.button1Click)
        self.button1.configure(text="OK", background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()


        self.button2 = Button(self.myContainer1, command=self.button2Click)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=RIGHT)


    def button1Click(self):
        print "button1Click event handler"


    def button2Click(self):
        print "button2Click event handler"
        #self.myParent.destroy()
        self.myContainer1.destroy()



root = Tk()
myapp = MyApp(root)
root.mainloop()