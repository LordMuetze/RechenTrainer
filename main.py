#Kommentar-Vorlage
#--------------------_____--------------------
#----------------------------------------------------------------------------------------------------




#--------------------Modulimport--------------------
from easygui import * #Grafische Oberfläche, Dokumentation: http://easygui.sourceforge.net
from random import * #Zufallsgenerator
import sys
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
# wird bei einer Box (Element der GUI) der Cancel-Button gedrückt, wird ein NoneType ausgegeben,
# was später zur Überprüfung genutzt wird, ob dieser Button gedrückt wurde
#----------------------------------------------------------------------------------------------------


#--------------------initialisieren von globalen Variablen, die später im Programm verwendet werden--------------------
#----------benötigte globale Variablen werden mit "global Variablenname" in die einzelnen Funktionen importiert----------
richtige_loesungen = 0.0
aufgabenliste = []
nutzer_loesungsliste = []
rechenart = []
min_zahl1 = None
max_zahl1 = None
min_zahl2 = None
max_zahl2 = None
anzahl_aufgaben = 0
#----------------------------------------------------------------------------------------------------





#--------------------Definition der Startseite--------------------
def startseite():

    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    global rechenart
    global min_zahl
    global max_zahl1
    global min_zahl2
    global max_zahl2
    global anzahl_aufgaben


    choices = ["Los gehts", "Verlassen"] #Festlegen der Buttons
    start = buttonbox("Herzlich Willkommen beim Rechentrainer", "Willkommen", choices, "zahlenbild.gif") #angeklickten Button an Variable binden


    #Reset der wichtigsten globalen Variablen mit jeder neuen Runde
    richtige_loesungen = 0.0
    aufgabenliste = []
    nutzer_loesungsliste = []
    rechenart = []
    min_zahl1 = None
    max_zahl1 = None
    min_zahl2 = None
    max_zahl2 = None
    anzahl_aufgaben = 0
    
    return start #angeklickten Button als Funktionswert ausgeben
#----------------------------------------------------------------------------------------------------




#--------------------Definition, welche Rechenart trainiert werden soll--------------------
def rechenart_eingeben():

    global rechenart

    while rechenart == []: #Schleife läuft, solange keine Rechenart ausgewählt wurde

        choices = ["Addition","Subtraktion","Multiplikation","Division"] #wählbare Rechenarten festlegen
        rechenart = multchoicebox("Welche Rechenarten willst du trainieren?","Rechenart",choices) #Liste aus ausgewählte(n) Rechenart(en) erstellen
    return rechenart #ausgewählte Rechenarten als Funktionswert zurückgeben
#----------------------------------------------------------------------------------------------------




#--------------------Definition, welche Rechenart trainiert werden soll--------------------
def rechenart_abrufen():

    global rechenart

    rechentyp = SystemRandom().choice(rechenart) #zufälliges Rechenart von Liste auswählen

    #abhängig von der gewählten Rechenart "Rechunung(operator)" mit Operator der jeweiligen Rechenart als Parameter aufrufen
    if rechentyp == "Addition":
        eingabe = Rechnung("+")

    elif rechentyp == "Subtraktion":
        eingabe = Rechnung("-")

    elif rechentyp == "Multiplikation":
        eingabe = Rechnung("*")

    elif rechentyp == "Division":
        eingabe = Rechnung("/")

    #wird keine möglichen Rechenart ausgewählt, wird ein SystemError ausgegeben und "eingabe" als NoneType gesetzt
    else:
        msgbox("System-Error [1]")
        eingabe = None
    
    return eingabe #"eingabe" als Funktionswert ausgeben
#----------------------------------------------------------------------------------------------------




#--------------------Anzahl der Aufgaben--------------------
def anzahl_aufgaben_eingeben():

    global anzahl_aufgaben
    
    #Anzahl der zu rechnenden Aufgaben an "anzahl_aufgaben" binden, automatische Prüfung auf natürliche Zahl, maximal: 10**12
    anzahl_aufgaben = integerbox("Wie viele Aufgabe willst du rechnen?","Anzahl",5,1,10**12)

    return anzahl_aufgaben #Anzahl als Funktionswert ausgeben
#----------------------------------------------------------------------------------------------------




#--------------------Definition der einzelnen Aufgabenstellung, rechenart-spezifisch, inhaltlich gleich--------------------
def Rechnung(operator):

    global richtige_loesungen
    global aufgabenliste
    global nutzer_loesungsliste
    global min_zahl1
    global max_zahl1
    global min_zahl2
    global max_zahl2

    richtige_loesungen += 1 #Punktzahl um 1 erhöhen

    nummer_1 = randint(min_zahl1, max_zahl1) #erste Zahl für die Rechnung mit kleinster & größter Zahl zufällig festlegen
    nummer_2 = randint(min_zahl2, max_zahl2) #zweite Zahl für die Rechnung mit kleinster & größter Zahl zufällig festlegen
    aufgabe = str(nummer_1) + " " + str(operator) + " " + str(nummer_2) #Aufgabe in der Form "1 + 1" erstellen
    ergebnis = eval(aufgabe) #zuvor erstellte Aufgabe berechnen

    aufgabenloesung = aufgabe + " = " + str(ergebnis) #Aufgabe mit Lösung in der Form "1 + 1 = 2" zusammensetzen

    i = 0 #Zählervariable für Versuchs-Schleife initialisieren

    while i < 2: #Schleife mit Maximalwert i<2 für Versuche


        while True: #Endlosschleife
            
            try: #try-Teil wird ausgeführt, bis ein Fehler auftritt
                #Aufgabenstellung mit Eingabefeld wird angezeigt, Form "1 + 1 = {Tabulator} (2 Nachkommastellen)"
                eingabe = enterbox(aufgabe+" = \t(2 Nachkommastellen)")

                if eingabe == None: #Cancel-Button wurde gedrückt
                    break #Endlosschleife wird unterbrochen

                else:
                    eingabe_korrigiert = float(eingabe) #Fehler wird ausgegeben, wenn sich die Eingabe nicht in einen Float umwandeln lässt (Text,Zeichen,...)
                    break #Endlosschleife wird unterbrochen

            #tritt ein Fehler auf, wird der except-Teil ausgeführt
            except:
                msgbox("Sorry da was bei deiner Eingabe falsch\n(z.B. falsche Zahlenart oder Komma statt Punkt bei Kommazahlen)")
                #Zurückspringen zum Schleifenanfang


        if eingabe == None: #Cancel-Button wurde gdedrückt
            break #Abbruch der Schleife, welche die Anzahl der Versuche zählt und in der die Aufgabenstellung angezeigt wird

        else:
            if eingabe_korrigiert == ergebnis: #Eingabe ist richtig
                msgbox("Sehr gut, das war richtig!")
                i += 2 #Zähler der Schleife auf 2 erhöhen und dadurch die Schleife beenden

            else: #Eingabe ist falsch

                if i == 0: #prüfen, ob es der erste Versuch ist
                    msgbox("Schade, das war falsch. Probiere es noch einmal.\nWenn du es dieses mal richtig machst, gibt es einen halben Punkt.")
                    richtige_loesungen -= 0.5 #einen halben Punkt abziehen --> 0,5 Punkte
                    i += 1 #Zähler der Schleife um 1 (auf 1) erhöhen

                else: #zweiter (letzter) Versuch
                    msgbox("Schade, das war falsch.\nDas gibt leider keine Punkte.")
                    richtige_loesungen -= 0.5 #einen weiteren halben Punkt abziehen --> 0 Punkte
                    i += 1 #Zähler der Schleife um 1 (auf 2) erhöhen

    if eingabe == None: #Cancel-Button wurde gdedrückt
        pass
    else:
        aufgabenliste.append(aufgabenloesung) #Aufgabe mit Lösung zur Liste für die Übersicht hinzufügen
        nutzer_loesungsliste.append(eingabe_korrigiert) #Lösung des Nutzers zur Liste für die Übersicht hinzufügen
    
    return eingabe #"eingabe" als Funktionswert ausgegeben
#----------------------------------------------------------------------------------------------------




#--------------------Festlegung des 1. Zahlenraums--------------------
def zahlenraum1():

    global min_zahl1
    global max_zahl1


    while True: #Endlosschleife

        try: #try-Teil wird ausgeführt, bis ein Fehler auftritt
            fields = ["min. Zahl","max. Zahl"] #Namen der Felder festlegen
            values = [1,100] #Standardwerte für die Felder festlegen

            zahlenraum_1 = multenterbox("In welchem Bereich soll die erste Zahl liegen?","Zahlenraum",fields,values)


            if zahlenraum_1 == None: #Cancel-Button wurde gedrückt
                break #Endlosschleife abbrechen

            else:
                max_zahl1 = int(zahlenraum_1.pop()) #letzten Wert der Liste als Maximalwert festlegen und von der Liste entfernen
                min_zahl1 = int(zahlenraum_1.pop()) #letzten Wert der Liste als Minimalwert festlegen und von der Liste entfernen
                #wird ein nicht-Integer (Float,Text,...) eingegeben, wird ein Fehler auftreten


                #prüfen, ob der Maximalwert größer als der Minimalwert ist
                #oder ob eine der beiden Zahlen kleiner als 0 ist (keine natürliche Zahl)
                if max_zahl1 < min_zahl1 or max_zahl1 < 0 or min_zahl1 < 0:
                    msgbox("Sorry, da war was bei deiner Eingabe falsch")
                
                else: #Zahlen sind ok
                    break #Endlosschleife abbrechen

        except: #tritt ein Fehler auf, so wird der except-Teil ausgeführt
            msgbox("Sorry, da war was bei deiner Eingabe falsch")
    
    return zahlenraum_1 #die Liste "zahlenraum_1" wird als Funktionswert ausgegeben
#----------------------------------------------------------------------------------------------------




#--------------------Festlegung des 2. Zahlenraums--------------------
def zahlenraum2():

    global min_zahl2
    global max_zahl2


    while True: #Endlosschleife

            try: #try-Teil wird ausgeführt, bis ein Fehler auftritt
                fields = ["min. Zahl","max. Zahl"] #Namen der Felder festlegen
                values = [1,100] #Standardwerte für die Felder festlegen

                zahlenraum_2 = multenterbox("In welchem Bereich soll die zweite Zahl liegen?","Zahlenraum",fields,values)


                if zahlenraum_2 == None: #Cancel-Button wurde gedrückt
                    break #Endlosschleife abbrechen

                else:
                    max_zahl2 = int(zahlenraum_2.pop()) #letzten Wert der Liste als Maximalwert festlegen und von der Liste entfernen
                    min_zahl2 = int(zahlenraum_2.pop()) #letzten Wert der Liste als Minimalwert festlegen und von der Liste entfernen
                    #wird ein nicht-Integer (Float,Text,...) eingegeben, wird ein Fehler auftreten

                    #prüfen, ob der Maximalwert größer als der Minimalwert ist
                    #oder ob eine der beiden Zahlen kleiner als 0 ist (keine natürliche Zahl)
                    if max_zahl2 < min_zahl2 or max_zahl2 < 0 or min_zahl2 < 0:
                        msgbox("Sorry, da war was bei deiner Eingabe falsch")
                        
                    else: #Zahlen sind ok
                        break #Endlosschleife abbrechen

            except: #tritt ein Fehler auf, so wird der except-Teil ausgeführt
                msgbox("Sorry, da war was bei deiner Eingabe falsch")

    return zahlenraum_2 #die Liste "zahlenraum_2" wird als Funktionswert ausgegeben
#----------------------------------------------------------------------------------------------------




#--------------------erstellen der Abschlussuebersicht--------------------
def uebersicht():

    global aufgabenliste
    global nutzer_loesungsliste
    global anzahl_aufgaben
    global richtige_loesungen
    uebersicht = "" #"uebersicht" als leeren String initialisieren


    for i in range (0,anzahl_aufgaben): #Schleife mit so vielen Durchläufen wie Aufgaben
        #bei jedem Durchlauf werden das letzte Element der Aufgabenliste & das letzte Element der Nutzerlösungsliste
        #mit drei Tabulatoren Abstand und einer neuen Zeile am Ende an den Anfang der Übersicht gesetzt
        uebersicht = str(aufgabenliste.pop()) + "\t\t\t" + str(nutzer_loesungsliste.pop()) + "\n" + uebersicht

    uebersicht = "Aufgabe\t\t\tdeine Loesung\n" + uebersicht #Überschriften für die beiden SPalten an den Anfang der Übersicht ergänzen

    #Übersicht in einer Scrollbaren Codebox ausgeben
    ausgabe = codebox("Hier ist die Uebersicht deiner Aufgaben\n\nDu hast "+str(richtige_loesungen)+" von "+str(anzahl_aufgaben)+" Punkten erreicht","Uebersicht",uebersicht)

    #Übersicht als Datei speichern
    Dateiname = filesavebox(filetypes=[".txt"]) #Speicherort und Dateiname festlegen

    if Dateiname == None: #Cancel-Button gedrückt
        pass #nicht tun & nicht speichern

    else:
        datei = open(Dateiname,"w") #Datei mit obigem Namen erstellen/öffnen und leeren
        datei.write(uebersicht) #"uebersicht" in Datei einfügen
        datei.close() #Datei schließen
    
    return ausgabe #"ausgabe" als Funktionswert ausgeben
#----------------------------------------------------------------------------------------------------




#--------------------Erstellen der main-Funktion--------------------
#--------------------Gesamtablauf und Zusammenfuehren vorheriger Funktionen--------------------
def main():

    while True: #Endlosschleife

        start = startseite() #Startseite aufrufen

        if start == "Los gehts": #"Los gehts"-Button gedrückt
            

            rechenart_testen = rechenart_eingeben()
            if rechenart_testen == None: #Cancel-Button wurde in dieser Funktion gedrückt
                break #Endlosschleife und damit weiteren Programmablauf abbrechen 
            else:
                pass
            
            
            zahlenraum1_testen = zahlenraum1()
            if zahlenraum1_testen == None: #Cancel-Button wurde in dieser Funktion gedrückt
                break #Endlosschleife und damit weiteren Programmablauf abbrechen
            else:
                pass
            

            zahlenraum2_testen = zahlenraum2()
            if zahlenraum2_testen == None: #Cancel-Button wurde in dieser Funktion gedrückt
                break #Endlosschleife und damit weiteren Programmablauf abbrechen
            else:
                pass
            
            
            anzahl_aufgaben_testen = anzahl_aufgaben_eingeben()
            if anzahl_aufgaben_testen == None: #Cancel-Button wurde in dieser Funktion gedrückt
                break #Endlosschleife und damit weiteren Programmablauf abbrechen
            else:
                pass


            for i in range(0,anzahl_aufgaben): #untere Funktion sooft aufrufen, wie Aufgaben gerechnet werden sollen
                rechenart_abrufen_testen = rechenart_abrufen()
                if rechenart_abrufen_testen == None: #Cancel-Button wurde in dieser Funktion gedrückt
                    break #Endlosschleife und damit weiteren Programmablauf abbrechen
                else:
                    pass

            try: #try-Teil wird solange ausgeführt bis ein Fehler auftritt
                uebersicht_testen = uebersicht()
                if uebersicht_testen == None: #Cancel-Button wurde in dieser Funktion gedrückt
                    break #Endlosschleife und damit weiteren Programmablauf abbrechen
                else:
                    pass
            except: #tritt ein Fehler auf, wird der except-Teil ausgeführt
                break #Endlosschleife und damit weiteren Programmablauf abbrechen

        elif start == "Verlassen": #"Verlassen"-Button wurde gedrückt
            break #Endlosschleife und damit weiteren Programmablauf abbrechen

        else: #es wurde keiner der beiden Buttons gedrückt aber es entsteht trotzdem eine Eingabe
            msgbox("System-Error")
    
    if start == "Verlassen": #"Verlassen"-Button wurde gedrückt
        sys.exit() #Programm schließen
    else:
        main() #Programm von Anfang an starten
#----------------------------------------------------------------------------------------------------




#--------------------Aufrufen der main-Funktion--------------------
main()
#----------------------------------------------------------------------------------------------------