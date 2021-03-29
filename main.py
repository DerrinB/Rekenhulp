# includes
from tkinter import *

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

    def berekenOppervlakte(self, lengte, breedte, label):
        try:
            oppervlakte=int(lengte) * int(breedte)
        except:
            label.config(text="Vul geldige waardes in")
        #print(str(oppervlakte))
        label.config(text="Oppervlakte: " + str(oppervlakte))

    def btwbereken(self, prijs, btw):
        try:
            prijs = float(prijs)
            try:
                btw = int(btw)
                btw += 100
                totaal = round((prijs / 100 * btw), 2)
                self.totaalL['text'] = totaal
            except:
                self.totaalL['text'] = 'vul een geldig btw tarief in'
        except:
            self.totaalL['text'] = 'vul een geldige prijs in'


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
        label_1 = Label(self.ov_frame, text="Lengte")
        lengte_entry = Entry(self.ov_frame)
        breedte_entry = Entry(self.ov_frame)
        btn = Button(self.ov_frame, text="Volgende", command=lambda: self.berekenOppervlakte(lengte_entry.get(), breedte_entry.get(), output_label))
        #btn['command'] = berekenOppervlakte(lengte_entry.get(), breedte_entry.get())
        output_label = Label(self.ov_frame, text="")

        label_1.pack()
        lengte_entry.pack()
        breedte_entry.pack()
        btn.pack()
        output_label.pack()
        
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

        berekenbtn = Button(self.btw_frame, text="Berkenen", command=lambda: self.btwbereken(prijsE.get(), btwE.get()))

        self.totaalL = Label(self.btw_frame, text="", font=("Courier", 12))

        label_1.pack()
        prijsL.pack()
        prijsE.pack()
        btwL.pack()
        btwE.pack()
        berekenbtn.pack()
        self.totaalL.pack()

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