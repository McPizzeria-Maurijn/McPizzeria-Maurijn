# Vul hier de naam van je programma in:
#
#
#Maurijn:
#
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------
def MaakTabellenAan():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzas(
            gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
            gerechtNaam TEXT NOT NULL,
            gerechtPrijs REAL NOT NULL);""")
    print("Tabel 'tbl_pizzas' aangemaakt")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klanten(
        klantNr INTEGER PRIMARY KEY AUTOINCREMENT, klantAchternaam TEXT) ;""")
    print("Tabel 'tbl_klanten' aangemaakt.")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)
    opgehaalde_gegevens = cursor.fetchall()
    print("Tabel" + tabel_naam + ":", opgehaalde_gegevens)

def voegPizzatoe(naam_nieuwe_pizza, prijs_nieuwe_pizza):
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ?)", (naam_nieuwe_pizza, prijs_nieuwe_pizza))
    db.commit()
    print("Pizza toegevoegd:")
    printTabel("tbl_pizzas")

def verwijderPizza(gerechtNaam):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
    print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam)
    db.commit()
    printTabel("tbl_pizzas")

def pasGerechtAan(gerechtID, nieuweGerechtNaam, nieuwePrijs):
    cursor.execute("UPDATE tbl_pizzas SET gerechtNaam = ?, gerechtPrijs = ? WHERE gerechtID = ?", (nieuweGerechtNaam, nieuwePrijs, gerechtID ))
    db.commit()
    print("Gerecht aangepast")
    printTabel("tbl_pizzas")

def voegKlantToe(naam_nieuwe_klant):
 cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (naam_nieuwe_klant,))
 db.commit()
 print("Klant toegevoegd:")
 printTabel("tbl_klanten")


### --------- Hoofdprogramma  ---------------
#MaakTabellenAan()
#printTabel("tbl_pizzas")
#voegPizzatoe("Margarita", 9.50)
#voegPizzatoe("Hawaii", 12.25)
#voegPizzatoe("Salami", 10.00)
#verwijderPizza("Hawaii")
#pasGerechtAan(3, "Salamiiii", 19.25)
#voegKlantToe("Janssen")
#voegKlantToe("Smit")