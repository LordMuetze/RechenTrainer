#Kommentar-Vorlage
#--------------------_____--------------------
#----------------------------------------------------------------------------------------------------




#--------------------Modulimport--------------------
from easygui import *
from time import *
from random import *
#----------------------------------------------------------------------------------------------------




#--------------------erstellen von Variablen--------------------
richtige_loesungen = 0.0
aufgabenliste = []
nutzer_loesungsliste = []
rechenart = []
min_zahl1 = None
max_zahl1 = None
min_zahl2 = None
max_zahl2 = None
anzahl_aufgaben = None
#----------------------------------------------------------------------------------------------------




#--------------------Definition der Startseite--------------------
def startseite():

    msg = "Herzlich Willkommen beim Rechentrainer"
    title = "Willkommen"
    choices = ["Los gehts", "Verlassen"]

    start = buttonbox(msg, title, choices)

    return start
#----------------------------------------------------------------------------------------------------




#--------------------Definition, welche Rechenart trainiert werden soll--------------------
def rechenart_eingeben():

    global rechenart

    while rechenart == []:
        msg = "Welche Rechenarten willst du trainieren?"
        title = "Rechenart"
        choices = ["Addition","Subtraktion","Multiplikation","Division"]

        rechenart = multchoicebox(msg,title,choices)

#----------------------------------------------------------------------------------------------------




#--------------------Definition, welche Rechenart trainiert werden soll--------------------
def rechenart_abrufen():

    global rechenart

    rechentyp = SystemRandom().choice(rechenart)

    if rechentyp == "Addition":
        Addition()

    elif rechentyp == "Subtraktion":
        Subtraktion()

    elif rechentyp == "Multiplikation":
        Multiplikation()

    elif rechentyp == "Division":
        Division()

    else:
        msgbox("System-Error [1]")
        startseite



#----------------------------------------------------------------------------------------------------




#--------------------Anzahl der Aufgaben--------------------
def anzahl_aufgaben():

    global anzahl_aufgaben

    anzahl = integerbox("Wie viele Aufgabe willst du rechnen?","Anzahl",5,1,10**12)
    anzahl_aufgaben = anzahl

    if anzahl == None:
        anzahl_aufgaben()

    return anzahl
#----------------------------------------------------------------------------------------------------




#--------------------Definition der einzelnen Aufgabenstellung, rechenart-spezifisch, inhaltlich gleich--------------------
def Addition():

    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    global min_zahl1
    global max_zahl1
    global min_zahl2
    global max_zahl2

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl1, max_zahl1)
    nummer_2 = randint(min_zahl2, max_zahl2)
    ergebnis = nummer_1 + nummer_2

    aufgabenstellung = str(nummer_1) + " + " + str(nummer_2) + " = "
    aufgabenloesung = aufgabenstellung + str(ergebnis)
    title = "Addition"

    i = 0

    while i < 2:

        while True:

            try:
                eingabe = enterbox(aufgabenstellung,title)

                if eingabe == None:
                    break

                else:
                    eingabe_korrigiert = int(eingabe)
                    break

            except ValueError:
                msgbox("Sorry da was bei deiner Eingabe falsch\n(z.B. falsche Zahlenart oder Komma statt Punkt bei Kommazahlen)")


        if eingabe == None:
            break

        else:
            if eingabe_korrigiert == ergebnis:
                msgbox("Sehr gut, das war richtig!")
                i += 2

            else:

                if i == 0:
                    msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                    richtige_loesungen -= 0.5
                    i += 1

                else:
                    msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                    richtige_loesungen -= 0.5
                    i += 1

    if eingabe == None:
        startseite()
    else:
        aufgabenliste.append(aufgabenloesung)
        nutzer_loesungsliste.append(eingabe_korrigiert)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Subtraktion():
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    global min_zahl1
    global max_zahl1
    global min_zahl2
    global max_zahl2

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl1, max_zahl1)
    nummer_2 = randint(min_zahl2, max_zahl2)
    ergebnis = nummer_1 - nummer_2

    aufgabenstellung = str(nummer_1) + " - " + str(nummer_2) + " = "
    aufgabenloesung = aufgabenstellung + str(ergebnis)
    title = "Subtraktion"

    i = 0

    while i < 2:

        while True:

            try:
                eingabe = enterbox(aufgabenstellung,title)

                if eingabe == None:
                    break

                else:
                    eingabe_korrigiert = int(eingabe)
                    break

            except ValueError:
                msgbox("Sorry da war was bei deiner Eingabe falsch\n(z.B. falsche Zahlenart oder Komma statt Punkt bei Kommazahlen)")


        if eingabe == None:
            break

        else:
            if eingabe_korrigiert == ergebnis:
                msgbox("Sehr gut, das war richtig!")
                i += 2

            else:

                if i == 0:
                    msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                    richtige_loesungen -= 0.5
                    i += 1

                else:
                    msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                    richtige_loesungen -= 0.5
                    i += 1

    if eingabe == None:
        startseite()
    else:
        aufgabenliste.append(aufgabenloesung)
        nutzer_loesungsliste.append(eingabe_korrigiert)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Multiplikation():
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    global min_zahl1
    global max_zahl1
    global min_zahl2
    global max_zahl2

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl1, max_zahl1)
    nummer_2 = randint(min_zahl2, max_zahl2)
    ergebnis = nummer_1 * nummer_2

    aufgabenstellung = str(nummer_1) + " x " + str(nummer_2) + " = "
    aufgabenloesung = aufgabenstellung + str(ergebnis)
    title = "Multiplikation"

    i = 0

    while i < 2:

        while True:

            try:
                eingabe = enterbox(aufgabenstellung,title)

                if eingabe == None:
                    break

                else:
                    eingabe_korrigiert = int(eingabe)
                    break

            except ValueError:
                msgbox("Sorry da war was bei deiner Eingabe falsch\n(z.B. falsche Zahlenart oder Komma statt Punkt bei Kommazahlen)")


        if eingabe == None:
            break

        else:
            if eingabe_korrigiert == ergebnis:
                msgbox("Sehr gut, das war richtig!")
                i += 2

            else:

                if i == 0:
                    msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                    richtige_loesungen -= 0.5
                    i += 1

                else:
                    msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                    richtige_loesungen -= 0.5
                    i += 1

    if eingabe == None:
        startseite()
    else:
        aufgabenliste.append(aufgabenloesung)
        nutzer_loesungsliste.append(eingabe_korrigiert)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Division():
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    global min_zahl1
    global max_zahl1
    global min_zahl2
    global max_zahl2

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl1, max_zahl1)
    nummer_2 = randint(min_zahl2, max_zahl2)
    ergebnis = nummer_1 / nummer_2

    aufgabenstellung = str(nummer_1) + " : " + str(nummer_2) + " = "
    aufgabenloesung = aufgabenstellung + str(ergebnis)
    title = "Division"

    i = 0

    while i < 2:

        while True:

            try:
                eingabe = enterbox(aufgabenstellung+"\n[zwei Nachkommastellen]",title)

                if eingabe == None:
                    break

                else:
                    eingabe_korrigiert = float(eingabe)
                    break

            except ValueError:
                msgbox("Sorry da war was bei deiner Eingabe falsch\n(z.B. falsche Zahlenart oder Komma statt Punkt bei Kommazahlen)")


        if eingabe == None:
            break

        else:
            if round(eingabe_korrigiert,2) == round(ergebnis,2):
                msgbox("Sehr gut, das war richtig!")
                i += 2

            else:

                if i == 0:
                    msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                    richtige_loesungen -= 0.5
                    i += 1

                else:
                    msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                    richtige_loesungen -= 0.5
                    i += 1

    if eingabe == None:
        startseite()
    else:
        aufgabenliste.append(aufgabenloesung)
        nutzer_loesungsliste.append(eingabe_korrigiert)
#----------------------------------------------------------------------------------------------------




#--------------------Festlegung des Zahlenraums--------------------
def zahlenraum():

    global min_zahl1
    global max_zahl1
    global min_zahl2
    global max_zahl2


    while True:

        try:
            msg = "In welchem Bereich soll die erste Zahl liegen?"
            title = "Zahlenraum"
            fields = ["min. Zahl","max. Zahl"]
            values = [1,100]

            zahlenraum_1 = multenterbox(msg,title,fields,values)

            max_zahl1 = int(zahlenraum_1.pop())
            min_zahl1 = int(zahlenraum_1.pop())

            if max_zahl1 < min_zahl1 or max_zahl1 < 0 or min_zahl1 < 0:
                msgbox("Sorry, da war was bei deiner Eingabe falsch")
            else:
                break

        except ValueError:
            msgbox("Sorry, da war was bei deiner Eingabe falsch")



    while True:

            try:
                msg = "In welchem Bereich soll die zweite Zahl liegen?"
                title = "Zahlenraum"
                fields = ["min. Zahl","max. Zahl"]
                values = [1,100]

                zahlenraum_2 = multenterbox(msg,title,fields,values)

                max_zahl2 = int(zahlenraum_2.pop())
                min_zahl2 = int(zahlenraum_2.pop())

                if max_zahl2 < min_zahl2 or max_zahl2 < 0 or min_zahl2 < 0:
                    msgbox("Sorry, da war was bei deiner Eingabe falsch")
                else:
                    break

            except ValueError:
                msgbox("Sorry, da war was bei deiner Eingabe falsch")
#----------------------------------------------------------------------------------------------------




#--------------------erstellen der Abschlussuebersicht--------------------
def uebersicht():

    global aufgabenliste
    global nutzer_loesungsliste
    global anzahl_aufgaben
    global richtige_loesungen
    uebersicht = ""


    for i in range (0,anzahl_aufgaben):
        uebersicht = str(aufgabenliste.pop()) + "\t\t\t" + str(nutzer_loesungsliste.pop()) + "\n" + uebersicht

    uebersicht = "Aufgabe\t\t\tdeine Loesung\n" + uebersicht


    codebox("Hier ist die Uebersicht deiner Aufgaben\n\nDu hast "+str(richtige_loesungen)+" von "+str(anzahl_aufgaben)+" Punkten erreicht","Uebersicht",uebersicht)

    Dateiname = filesavebox(filetypes=[".txt"])

    if Dateiname == None:
        startseite()

    else:
        datei = open(Dateiname,"a")
        datei.write(uebersicht)
        datei.close()
#----------------------------------------------------------------------------------------------------




#--------------------Erstellen der main-Funktion--------------------
#--------------------Gesamtablauf und ZUsammenfuehren vorheriger Funktionen--------------------
def main():

    if startseite() == "Los gehts":

        rechenart_eingeben()
        zahlenraum()

        for i in range(0,anzahl_aufgaben()):
            rechenart_abrufen()
        uebersicht()




    elif startseite() == "Verlassen":
        quit()

    else:
        msgbox("System-Error")
#----------------------------------------------------------------------------------------------------




#--------------------Aufrufen der main-Funktion--------------------
while True:
    action = main()
    if action == "Verlassen":
        quit()
        break
    else:
        pass
quit()
#----------------------------------------------------------------------------------------------------