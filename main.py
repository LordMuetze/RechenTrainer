#Kommentar-Vorlage
#--------------------_____--------------------
#----------------------------------------------------------------------------------------------------



#--------------------Modulimport--------------------
from easygui import *
from time import *
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




#--------------------Definition der einzelnen Aufgabenstellung, rechenart-spezifisch, inhaltlich gleich--------------------
def Addition(nummer1,nummer2,min_zahl,max_zahl):
    


    enterbox(msg,title)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Subtraktion(nummer1,nummer2,min_zahl,max_zahl):
    pass
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Multiplikation(nummer1,nummer2,min_zahl,max_zahl):
    pass
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
def Division(nummer1,nummer2,min_zahl,max_zahl):
    pass
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



zahlenraum()