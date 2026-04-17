# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Maurijn:
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
#def zoekKlant():
    #gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    #print(gevonden_klanten)
    #invoerveldKlantnaam.delete(0, END)
    #invoerveldKlantNr.delete(0, END)
    #for rij in gevonden_klanten:
        #invoerveldKlantNr.insert(END, rij[0])
        #invoerveldKlantnaam.insert(END, rij[1])

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

#knopSluit = Button(venster, text="Close", width=22, command=venster.destroy)
#knopSluit.grid(row=17, column=4)

#labelIntro = Label(venster, text="Welkom!")
#labelIntro.grid(row=0, column=0, sticky="W") 

#labelKlantnaam = Label(venster, text="Klantnaam:")
#labelKlantnaam.grid(row=1, column=0)
 
#ingevoerde_klantnaam = StringVar() 
#invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam) 
#invoerveldKlantnaam.grid(row=1, column=1, sticky="W") 

#labelKlantNr = Label(venster, text="Klantnummer:")
#labelKlantNr.grid(row=2, column=0)

#invoerveldKlantNr = Entry(venster) 
#invoerveldKlantNr.grid(row=2, column=1, sticky="W") 

#zoekKnop = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
#zoekKnop.grid(row=1, column=4, sticky="W")

#TOON PIZZAS OPDRACHT

labelPizzanaam = Label(venster, text="Pizzanaam:")
labelPizzanaam.grid(row=0, column=0, sticky="W")

invoerveldPizzanaam = Entry(venster)
invoerveldPizzanaam.grid(row=0, column=1)

knopZoekOpPizzaNaam = Button(venster, text="Zoek Pizza")
knopZoekOpPizzaNaam.grid(row=0, column=3)

labelMogelijkheden = Label(venster, text="Mogelijkheden:")
labelMogelijkheden.grid(row=1, column=0, sticky="W")

listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid(row=1, column=1, rowspan=6, columnspan=2, sticky="W")

knopToonPizzas = Button(venster, text="Toon alle pizza's")
knopToonPizzas.grid(row=1, column=3)

#FUNCTIE DEFENITIES (TOON PIZZAS OPDRACHT)
def zoekPizza():
    gevonden_pizzas = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizzanaam.get())
    print(gevonden_pizzas)
    invoerveldPizzanaam.delete(0, END)
    for rij in gevonden_pizzas:
        invoerveldPizzanaam.insert(END, rij[1])

#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
