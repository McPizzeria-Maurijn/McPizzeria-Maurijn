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

def zoekKlantInTabel(ingevoerde_klantnaam):
    cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?", (ingevoerde_klantnaam,))
    zoek_resultaat = cursor.fetchall()
    if zoek_resultaat == []:
        print("Geen klant gevonden met achternaam", ingevoerde_klantnaam)
        print("Klant wordt nu toegevoegd.")
        cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ? )", (ingevoerde_klantnaam, ))
        db.commit() #gegevens in de database zetten
        print("Klant toegevoegd aan 'tbl_klanten':" + ingevoerde_klantnaam )
        printTabel("tbl_klanten")
        cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?",(ingevoerde_klantnaam,))
        zoek_resultaat = cursor.fetchall()
    return zoek_resultaat

def zoekPizzaInTabel(ingevoerde_pizzanaam):
    cursor.execute("SELECT * FROM tbl_pizzas WHERE pizzaNaam = ?", (ingevoerde_pizzanaam,))
    zoek_resultaat = cursor.fetchall()
    if zoek_resultaat == []:
        print("Geen pizza gevonden met naam")
        print("Pizza wordt nu toegevoegd")
        cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?)", (ingevoerde_pizzanaam,))
        db.commit()
        print("Pizza toegevoegd aan 'tbl_pizzas':" + ingevoerde_pizzanaam)
        printTabel("tbl_pizzas")
        cursor.execute("SELECT * FROM tbl_pizzas WHERE pizzaMaa, = ?", (ingevoerde_pizzanaam))
        zoek_resultaat = cursor.fetchall()
    return zoek_resultaat

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