#Kommentar-Vorlage
#--------------------_____--------------------
#----------------------------------------------------------------------------------------------------




#--------------------Modulimport--------------------
from easygui import *
import easygui
from time import *
from random import *
#----------------------------------------------------------------------------------------------------




#--------------------erstellen von Variablen--------------------
richtige_loesungen = 0
aufgabenliste = []
nutzer_loesungsliste = []
#----------------------------------------------------------------------------------------------------




#--------------------Definition der Startseite--------------------
def startseite():
    msgbox("Hallo")
#----------------------------------------------------------------------------------------------------




#--------------------Definition, welche Rechenart trainiert werden soll--------------------
def rechenart():

    msg = "Welche Rechenarten willst du trainieren?"
    title = "Rechenart"
    choices = ["Addition","Subtraktion","Multiplikation","Division","verschiedene"]

    rechenart = buttonbox(msg, title, choices)

    return rechenart
#----------------------------------------------------------------------------------------------------




#--------------------Anzahl der Aufgaben--------------------
def anzahl_aufgaben():
    pass
#----------------------------------------------------------------------------------------------------




#--------------------Definition der einzelnen Aufgabenstellung, rechenart-spezifisch, inhaltlich gleich--------------------
def Addition(min_zahl,max_zahl):
    
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
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
def Subtraktion(min_zahl,max_zahl):
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
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
def Multiplikation(min_zahl,max_zahl):
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    
    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
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
def Division(min_zahl,max_zahl):
    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    
    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
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
                msgbox("Sorry da was bei deiner Eingabe falsch\n(z.B. falsche Zahlenart oder Komma statt Punkt bei Kommazahlen)")        
        
        
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

    while True:

        try:
            msg = "In welchem Bereich soll die erste Zahl liegen?"
            title = "Zahlenraum"
            fields = ["min. Zahl","max. Zahl"]
            values = [1,100]

            zahlenraum_1 = multenterbox(msg,title,fields,values)

            zahl1_max = int(zahlenraum_1.pop())
            zahl1_min = int(zahlenraum_1.pop())

            if zahl1_max < zahl1_min or zahl1_max < 0 or zahl1_min < 0:
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

                zahl2_max = int(zahlenraum_2.pop())
                zahl2_min = int(zahlenraum_2.pop())

                if zahl2_max < zahl2_min or zahl2_max < 0 or zahl2_min < 0:
                    msgbox("Sorry, da war was bei deiner Eingabe falsch")
                else:
                    break

            except ValueError:
                msgbox("Sorry, da war was bei deiner Eingabe falsch")
#----------------------------------------------------------------------------------------------------


Division(1,10)


print(aufgabenliste)
print(nutzer_loesungsliste)
