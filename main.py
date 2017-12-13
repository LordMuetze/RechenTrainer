from easygui import *
from time import *



def startseite():
    pass



def rechenart():

    msg = "Welche Rechenarten willst du trainieren?"
    title = "Rechenart"
    choices = ["Addition","Multiplikation","Addition & Multiplikation"]

    rechenart = buttonbox(msg, title, choices)

    return rechenart



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




zahlenraum()