#Kommentar-Vorlage
#--------------------_____--------------------
#----------------------------------------------------------------------------------------------------




#--------------------Modulimport--------------------
from easygui import *
from time import *
from random import *
#----------------------------------------------------------------------------------------------------




#--------------------erstellen von Variablen--------------------
richtige_loesungen = 0
#----------------------------------------------------------------------------------------------------




#--------------------Definition der Startseite--------------------
def startseite():
    pass
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

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
    ergebnis = nummer_1 + nummer_2

    for i in range(0,2):
        

        msg = str(nummer_1) + " + " + str(nummer_2) + " = "
        title = "Addition"


        while True:
            
            try:
                eingabe = int(enterbox(msg,title))
                break
            
            except ValueError:
                msgbox("Sorry da was bei deiner Eingabe falsch (z.B. falsche Zahlenart)")        
        
        
        if eingabe == ergebnis:
            msgbox("Sehr gut, das war richtig!")
        
        else:
            
            if i == 0:
                msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                richtige_loesungen -= 0.5
                
            else:
                msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                richtige_loesungen -= 0.5
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Subtraktion(min_zahl,max_zahl):
    global richtige_loesungen

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
    ergebnis = nummer_1 - nummer_2

    for i in range(0,2):
        

        msg = str(nummer_1) + " - " + str(nummer_2) + " = "
        title = "Subtraktion"


        while True:
            
            try:
                eingabe = int(enterbox(msg,title))
                break
            
            except ValueError:
                msgbox("Sorry da was bei deiner Eingabe falsch (z.B. falsche Zahlenart)")        
        
        
        if eingabe == ergebnis:
            msgbox("Sehr gut, das war richtig!")
        
        else:
            
            if i == 0:
                msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                richtige_loesungen -= 0.5
                
            else:
                msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                richtige_loesungen -= 0.5
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Multiplikation(min_zahl,max_zahl):
    global richtige_loesungen

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
    ergebnis = nummer_1 * nummer_2

    for i in range(0,2):
        

        msg = str(nummer_1) + " x " + str(nummer_2) + " = "
        title = "Multiplikation"


        while True:
            
            try:
                eingabe = int(enterbox(msg,title))
                break
            
            except ValueError:
                msgbox("Sorry da was bei deiner Eingabe falsch (z.B. falsche Zahlenart)")        
        
        
        if eingabe == ergebnis:
            msgbox("Sehr gut, das war richtig!")
        
        else:
            
            if i == 0:
                msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                richtige_loesungen -= 0.5
                
            else:
                msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                richtige_loesungen -= 0.5
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Division(min_zahl,max_zahl):
    global richtige_loesungen

    richtige_loesungen += 1

    nummer_1 = randint(min_zahl, max_zahl)
    nummer_2 = randint(min_zahl, max_zahl)
    ergebnis = nummer_1 / nummer_2

    for i in range(0,2):
        

        msg = str(nummer_1) + " : " + str(nummer_2) + " = "
        title = "Division"


        while True:
            
            try:
                eingabe = int(enterbox(msg,title))
                break
            
            except ValueError:
                msgbox("Sorry da was bei deiner Eingabe falsch (z.B. falsche Zahlenart)")        
        
        
        if eingabe == ergebnis:
            msgbox("Sehr gut, das war richtig!")
        
        else:
            
            if i == 0:
                msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                richtige_loesungen -= 0.5
                
            else:
                msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                richtige_loesungen -= 0.5    
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


Addition(1,10)
