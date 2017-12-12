from easygui import *
from time import *



def startseite():
    pass



def rechenart():
    
    msg = "Welche Rechenarten möchtest du üben?"
    title = "Rechenart"
    choices = ["Addition","Multiplikation","Addition & Multiplikation"]

    rechenart = buttonbox(msg, title, choices)
    
    return rechenart



def zahlenraum():
    
    msg = "In welchem Bereich soll die erste Zahl liegen?"
    title = "Zahlenraum"
    fields = ["kleinste Zahl","größte Zahl"]
    values = [1,100]

    zahlenraum_1 = multenterbox(msg,title,fields,values)
    zahl1_max = zahlenraum_1.pop()
    zahl1_min = zahlenraum_1.pop()


    msg = "In welchem Bereich soll die zweite Zahl liegen?"
    title = "Zahlenraum"
    fields = ["kleinste Zahl","größte Zahl"]
    values = [1,100]

    zahlenraum_2 = multenterbox(msg,title,fields,values)
    zahl2_max = zahlenraum_2.pop()
    zahl2_min = zahlenraum_2.pop()

