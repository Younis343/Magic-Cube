


class MagicCube:
    def __init__(self):
        #Zauberwuerfel erstellen
        self.vorne = [["weiss", "weiss", "weiss"], ["weiss", "weiss", "weiss"], ["weiss", "weiss", "weiss"]]
        self.rechts = [["rot", "rot", "rot"], ["rot", "rot", "rot"], ["rot", "rot", "rot"]]
        self.links = [["orange", "orange", "orange"], ["orange", "orange", "orange"], ["orange", "orange", "orange"]] 
        self.oben = [["blau", "blau", "blau"], ["blau", "blau", "blau"], ["blau", "blau", "blau"]] 
        self.unten = [["gruen", "gruen", "gruen"], ["gruen", "gruen", "gruen"], ["gruen", "gruen", "gruen"]] 
        self.hinten = [["gelb", "gelb", "gelb"], ["gelb", "gelb", "gelb"], ["gelb", "gelb", "gelb"]]

    def show_cube(self):
        print("So sieht der Wuerfel aus: ")
        print()
        print("Vorne: ", self.vorne)
        print("Rechts: ", self.rechts)
        print("Links: ", self.links)
        print("Oben: ", self.oben)
        print("Unten: ", self.unten)
        print("Hinten: ", self.hinten)
        print()

    def create_cube(self, vorne, rechts, links, oben, unten, hinten):
        self.vorne = vorne
        self.rechts = rechts
        self.links = links
        self.oben = oben
        self.unten = unten
        self.hinten = hinten

    def drehen_cw(self, seite):
        #Seite im Uhrzeigersinn drehen

        temp_side = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        #Zeile 1 aktualisieren
        temp_side[0][0] = seite[2][0]
        temp_side[0][1] = seite[1][0]
        temp_side[0][2] = seite[0][0]

        #Zeile 2 aktualisieren
        temp_side[1][0] = seite[2][1]
        temp_side[1][1] = seite[1][1]
        temp_side[1][2] = seite[0][1]

        #Zeile 3 aktualisieren
        temp_side[2][0] = seite[2][2]
        temp_side[2][1] = seite[1][2]
        temp_side[2][2] = seite[0][2]

        return temp_side

    def drehen_ccw(self, seite):
        #Seite gegen den Uhrzeigersinn drehen

        temp_side = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        #Spalte 1 aktualisieren
        temp_side[2][0] = seite[0][0]
        temp_side[1][0] = seite[0][1]
        temp_side[0][0] = seite[0][2]

        #Spalte 2 aktualisieren
        temp_side[2][1] = seite[1][0]
        temp_side[1][1] = seite[1][1]
        temp_side[0][1] = seite[1][2]

        #Spalte 3 aktualisieren
        temp_side[2][2] = seite[2][0]
        temp_side[1][2] = seite[2][1]
        temp_side[0][2] = seite[2][2]

        return temp_side

    def kante_cw(self, kanten):
        placeholder = kanten.pop()
        kanten.insert(0, placeholder)
        return kanten

    def kante_ccw(self, kanten):
        placeholder = kanten.pop(0)
        kanten.append(placeholder)
        return kanten

    def vorne_cw(self):
        #Vorderseite im Uhrzeigersinn drehen
        
        self.vorne = self.drehen_cw(self.vorne)

        #Kanten aktualisieren
        kanten = [self.oben[0], self.rechts[0], self.unten[0], self.links[0]]
        kanten = self.kante_cw(kanten)
        self.oben[0] = kanten[0]
        self.rechts[0] = kanten[1]
        self.unten[0] = kanten[2]
        self.links[0] = kanten[3]

    def vorne_ccw(self):
        #Vorderseite gegen den Uhrzeigersinn drehen
        
        self.vorne = self.drehen_ccw(self.vorne)

        #Kanten aktualisieren
        kanten = [self.oben[0], self.rechts[0], self.unten[0], self.links[0]]
        kanten = self.kante_ccw(kanten)
        self.oben[0] = kanten[0]
        self.rechts[0] = kanten[1]
        self.unten[0] = kanten[2]
        self.links[0] = kanten[3]

    def unten_cw(self):
        #Unterseite im Uhrzeigersinn drehen
        
        self.unten = self.drehen_cw(self.unten)

        #Kanten aktualisieren
        kanten = [self.vorne[2], [self.rechts[0][0], self.rechts[1][0], self.rechts[2][0]],
                  [self.hinten[2][0], self.hinten[2][1], self.hinten[2][2]], [self.links[2][2], self.links[1][2], self.links[0][2]]]
        kanten = self.kante_cw(kanten)

        self.vorne[2] = kanten[0]
        self.rechts[0][0], self.rechts[1][0], self.rechts[2][0] = kanten[1]
        self.hinten[2][0], self.hinten[2][1], self.hinten[2][2] = kanten[2]
        self.links[2][2], self.links[1][2], self.links[0][2] = kanten[3]

        
        """self.oben[0] = kanten[0]
        self.rechts[0] = kanten[1]
        self.unten[0] = kanten[2]
        self.links[0] = kanten[3]

        placeholder = self.vorne[2]
        self.vorne[2] = [self.links[2][2], self.links[1][2], self.links[0][2]]
        
        self.links[2][2] = self.hinten[2][0]
        self.links[1][2] = self.hinten[2][1]
        self.links[0][2] = self.hinten[2][2]

        self.hinten[2][0] = self.rechts[0][0]
        self.hinten[2][1] = self.rechts[1][0]
        self.hinten[2][2] = self.rechts[2][0]

        self.rechts[0][0] = placeholder[0]
        self.rechts[1][0] = placeholder[1]
        self.rechts[2][0] = placeholder[2]"""

    def unten_ccw(self):
        #Unterseite gegen den Uhrzeigersinn drehen
        
        self.unten = self.drehen_ccw(self.unten)

        kanten = [self.vorne[2], [self.rechts[0][0], self.rechts[1][0], self.rechts[2][0]],
                  [self.hinten[2][0], self.hinten[2][1], self.hinten[2][2]], [self.links[2][2], self.links[1][2], self.links[0][2]]]
        kanten = self.kante_ccw(kanten)

        self.vorne[2] = kanten[0]
        self.rechts[0][0], self.rechts[1][0], self.rechts[2][0] = kanten[1]
        self.hinten[2][0], self.hinten[2][1], self.hinten[2][2] = kanten[2]
        self.links[2][2], self.links[1][2], self.links[0][2] = kanten[3]

    def oben_cw(self):

        self.oben = self.drehen_cw(self.oben)

        kanten = [[self.vorne[0][2], self.vorne[0][1], self.vorne[0][0]], [self.links[0][0], self.links[1][0], self.links[2][0]],
                  [self.hinten[0][2], self.hinten[0][1], self.hinten[0][0]], [self.rechts[2][2], self.rechts[1][2], self.rechts[0][2]]]
        kanten = self.kante_cw(kanten)

        self.vorne[0][2], self.vorne[0][1], self.vorne[0][0] = kanten[0]
        self.links[0][0], self.links[1][0], self.links[2][0] = kanten[1]
        self.hinten[0][2], self.hinten[0][1], self.hinten[0][0] = kanten[2]
        self.rechts[2][2], self.rechts[1][2], self.rechts[0][2] = kanten[3]

    def oben_ccw(self):

        self.oben = self.drehen_ccw(self.oben)

        kanten = [[self.vorne[0][2], self.vorne[0][1], self.vorne[0][0]], [self.links[0][0], self.links[1][0], self.links[2][0]],
                  [self.hinten[0][2], self.hinten[0][1], self.hinten[0][0]], [self.rechts[2][2], self.rechts[1][2], self.rechts[0][2]]]
        kanten = self.kante_ccw(kanten)

        self.vorne[0][2], self.vorne[0][1], self.vorne[0][0] = kanten[0]
        self.links[0][0], self.links[1][0], self.links[2][0] = kanten[1]
        self.hinten[0][2], self.hinten[0][1], self.hinten[0][0] = kanten[2]
        self.rechts[2][2], self.rechts[1][2], self.rechts[0][2] = kanten[3]

    def hinten_cw(self):

        self.hinten = self.drehen_cw(self.hinten)

        kanten = [self.oben[2], self.links[2], self.unten[2], self.rechts[2]]
        kanten = self.kante_cw(kanten)

        self.oben[2] = kanten[0]
        self.links[2] = kanten[1]
        self.unten[2] = kanten[2]
        self.rechts[2] = kanten[3]

    def hinten_ccw(self):

        self.hinten = self.drehen_ccw(self.hinten)

        kanten = [self.oben[2], self.links[2], self.unten[2], self.rechts[2]]
        kanten = self.kante_ccw(kanten)

        self.oben[2] = kanten[0]
        self.links[2] = kanten[1]
        self.unten[2] = kanten[2]
        self.rechts[2] = kanten[3]

    def rechts_cw(self):

        self.rechts = self.drehen_cw(self.rechts)

        kanten = [[self.vorne[2][2], self.vorne[1][2], self.vorne[0][2]], [self.oben[0][0], self.oben[1][0], self.oben[2][0]],
                  [self.hinten[0][0], self.hinten[1][0], self.hinten[2][0]], [self.unten[2][2], self.unten[1][2], self.unten[0][2]]]
        kanten = self.kante_cw(kanten)

        self.vorne[2][2], self.vorne[1][2], self.vorne[0][2] = kanten[0]
        self.oben[0][0], self.oben[1][0], self.oben[2][0] = kanten[1]
        self.hinten[0][0], self.hinten[1][0], self.hinten[2][0] = kanten[2]
        self.unten[2][2], self.unten[1][2], self.unten[0][2] = kanten[3]

    def rechts_ccw(self):

        self.rechts = self.drehen_ccw(self.rechts)

        kanten = [[self.vorne[2][2], self.vorne[1][2], self.vorne[0][2]], [self.oben[0][0], self.oben[1][0], self.oben[2][0]],
                  [self.hinten[0][0], self.hinten[1][0], self.hinten[2][0]], [self.unten[2][2], self.unten[1][2], self.unten[0][2]]]
        kanten = self.kante_ccw(kanten)

        self.vorne[2][2], self.vorne[1][2], self.vorne[0][2] = kanten[0]
        self.oben[0][0], self.oben[1][0], self.oben[2][0] = kanten[1]
        self.hinten[0][0], self.hinten[1][0], self.hinten[2][0] = kanten[2]
        self.unten[2][2], self.unten[1][2], self.unten[0][2] = kanten[3]

    def links_cw(self):

        self.links = self.drehen_cw(self.links)

        kanten = [[self.vorne[0][0], self.vorne[1][0], self.vorne[2][0]], [self.unten[0][0], self.unten[1][0], self.unten[2][0]],
                  [self.hinten[2][2], self.hinten[1][2], self.hinten[0][2]], [self.oben[2][2], self.oben[1][2], self.oben[0][2]]]
        kanten = self.kante_cw(kanten)

        self.vorne[0][0], self.vorne[1][0], self.vorne[2][0] = kanten[0]
        self.unten[0][0], self.unten[1][0], self.unten[2][0] = kanten[1]
        self.hinten[2][2], self.hinten[1][2], self.hinten[0][2] = kanten[2]
        self.oben[2][2], self.oben[1][2], self.oben[0][2] = kanten[3]

    def links_ccw(self):

        self.links = self.drehen_ccw(self.links)

        kanten = [[self.vorne[0][0], self.vorne[1][0], self.vorne[2][0]], [self.unten[0][0], self.unten[1][0], self.unten[2][0]],
                  [self.hinten[2][2], self.hinten[1][2], self.hinten[0][2]], [self.oben[2][2], self.oben[1][2], self.oben[0][2]]]
        kanten = self.kante_ccw(kanten)

        self.vorne[0][0], self.vorne[1][0], self.vorne[2][0] = kanten[0]
        self.unten[0][0], self.unten[1][0], self.unten[2][0] = kanten[1]
        self.hinten[2][2], self.hinten[1][2], self.hinten[0][2] = kanten[2]
        self.oben[2][2], self.oben[1][2], self.oben[0][2] = kanten[3]

        
