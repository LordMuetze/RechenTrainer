from easygui import *



def startseite():
    pass

def rechenart():
    msg = "Welche Rechenarten möchtest du üben?"
    title = "Rechenart"
    choices = ["Addition","Multiplikation","Addition & Multiplikation"]
    rechenart = buttonbox(msg, title, choices)
    return rechenart

rechenart()
