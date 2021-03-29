# includes
from tkinter import *

# funcies
def btwbereken(prijs, btw):
    pass


# scherm maken
class scherm():
    def __init__(self):
        self.root = Tk()
        self.root.title("Rekenhulp")
        self.root.geometry("600x300+100+100")

        # Menu maken
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Menu items maken
        mainmenu = Menu(menubar)
        mainmenu.add_command(label="Oppervlakte berekenen", command=self.oppervlakte)
        mainmenu.add_command(label="BTW Berekenen", command=self.btwbrekenen)
        mainmenu.add_command(label="Omtrek & diameter cirkel berekenen", command=self.cirkel)
        mainmenu.add_separator()
        mainmenu.add_command(label="Exit", command=self.root.quit)
        # Menu toevoegen aan menubar
        menubar.add_cascade(label="Menu", menu=mainmenu)

        self.hoofdmenu()

        self.root.config(menu=menubar)
        self.root.mainloop()

    def oppervlakte(self):
        try:
            self.btw_frame.pack_forget()
        except:
            pass
        try:
            self.home_frame.pack_forget()
        except:
            pass
        try:
            self.cirkel_frame.pack_forget()
        except:
            pass
            
        self.ov_frame = Frame(borderwidth=10)
        label_1 = Label(self.ov_frame, text="oppervlakte", bg="red", fg="white")
        label_1.pack()
        self.ov_frame.pack()

    def btwbrekenen(self):
        try:
            self.cirkel_frame.pack_forget()
        except:
            pass
        try:
            self.home_frame.pack_forget()
        except:
            pass
        try:
            self.ov_frame.pack_forget()
        except:
            pass
        
        self.btw_frame = Frame(borderwidth=10)

        label_1 = Label(self.btw_frame, text="BTW Berekenen", font=("Courier", 20))
        prijsL = Label(self.btw_frame, text="Prijs ex. BTW:", font=("Courier", 12))
        prijsE = Entry(self.btw_frame)

        btwL = Label(self.btw_frame, text="BTW tarief:", font=("Courier", 12))
        btwE = Entry(self.btw_frame)

        berekenbtn = Button(self.btw_frame, text="Berkenen")

        label_1.pack()
        prijsL.pack()
        prijsE.pack()
        btwL.pack()
        btwE.pack()
        berekenbtn.pack()

        self.btw_frame.pack()

    def cirkel(self):
        try:
            self.ov_frame.pack_forget()
        except:
            pass
        try:
            self.home_frame.pack_forget()
        except:
            pass
        try:
            self.btw_frame.pack_forget()
        except:
            pass
        
        self.cirkel_frame = Frame(borderwidth=10)
        label_1 = Label(self.cirkel_frame, text="Cirkel", bg="red", fg="white")
        label_1.pack()
        self.cirkel_frame.pack()

    def hoofdmenu(self):
        self.home_frame = Frame(borderwidth=10)
        label_1 = Label(self.home_frame, text="Welkom bij onze applicatie", font=("Courier", 25))
        label_2 = Label(self.home_frame, text="Klik in het Menu om te beginnen", font=("Courier", 15))
        label_1.pack()
        label_2.pack()
        self.home_frame.pack()

        def test(sef):
            pass
scherm = scherm()