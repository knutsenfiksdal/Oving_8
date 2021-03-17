import math


class Punkt:
    #Konstruktør
    def __init__(self, start_x=0, start_y=0):
        self.x_koordinat = start_x
        self.y_koordinat = start_y

    def flytt(self, delta_x, delta_y):
        self.x_koordinat += delta_x
        self.y_koordinat += delta_y

    # Bruker en property for x-koordinat for å sørge for at koordinatet ikke kan være
    # negativt
    @property
    def x_koordinat(self):
        return self.__x_koordinat

    @x_koordinat.setter
    def x_koordinat(self, ny_x):
        if ny_x >= 0:
            self.__x_koordinat = ny_x
        else:
            raise ValueError("X-koorinatet i denne applikasjonen kan ikke være negativt!")

    # Properties uten en setter blir read-only, man kan lese dem men ikke sette dem
    # lik noe. R og Theta er også beregnete egenskaper siden de regnes ut
    # fra koordinatene.
    @property
    def r(self):
        return math.sqrt(self.x_koordinat**2 + self.y_koordinat**2)

    @property
    def theta(self):
        return math.acos(self.x_koordinat/self.r)

    def __str__(self):
        return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"

    def __eq__(self, other):
        if not isinstance(other, Punkt):
            return False
        if self.x_koordinat == other.x_koordinat and self.y_koordinat == other.y_koordinat:
            return True
        return False


# startpunkt og sluttpunkt er ment å være Punkt objekter
class Linjesegment:
    def __init__(self, startpunkt, sluttpunkt):
        self.startpunkt = startpunkt
        self.sluttpunkt = sluttpunkt

    def flytt(self, delta_x, delta_y):
        self.startpunkt.flytt(delta_x, delta_y)
        self.sluttpunkt.flytt(delta_x, delta_y)

    def __str__(self):
        resultat = "Linjesegment: \n"
        resultat += str(self.startpunkt) + "\n"
        resultat += str(self.sluttpunkt) + "\n"
        return resultat

    def grunn_kopi(self):
        return Linjesegment(self.startpunkt, self.sluttpunkt)

    def dyp_kopi(self):
        startpunkt_kopi = Punkt(self.startpunkt.x_koordinat, self.startpunkt.y_koordinat)
        sluttpunkt_kopi = Punkt(self.sluttpunkt.x_koordinat, self.sluttpunkt.y_koordinat)
        return Linjesegment(startpunkt_kopi, sluttpunkt_kopi)


def flytt_tall_til_midten(tall1, tall2):
    gjennomsnitt = (tall1 + tall2)/2
    tall1 = gjennomsnitt
    tall2 = gjennomsnitt


def flytt_punkt_til_midten(punkt1, punkt2):
    gjennomsnitt_x = (punkt1.x_koordinat + punkt2.x_koordinat)/2
    gjennomsnitt_y = (punkt1.y_koordinat + punkt2.y_koordinat)/2
    punkt1.x_koordinat = gjennomsnitt_x
    punkt2.x_koordinat = gjennomsnitt_x
    punkt1.y_koordinat = gjennomsnitt_y
    punkt2.y_koordinat = gjennomsnitt_y


if __name__ == "__main__":
    p1 = Punkt(2, 2)
    p2 = Punkt(10, 10)
    l1 = Linjesegment(p1, p2)
    print(l1)
    p3 = Punkt(17, 5)
    l2 = Linjesegment(p2, p3)
    print(l2)
    p2.x_koordinat = 13
    print(l1)
    print(l2)
    print()
    l1.flytt(0, 2)
    print(l1)
    print(l2)
    print()
    p4 = p1
    print()
    print(p1)
    print(p4)
    print()
    p1.flytt(2, 2)
    print(p1)
    print(p4)
    print()
    tall1 = 6
    tall2 = 12
    print(tall1)
    print(tall2)
    print()
    flytt_tall_til_midten(tall1, tall2)
    print(tall1)
    print(tall2)
    print()
    print(p1)
    print(p2)
    print()
    flytt_punkt_til_midten(p1, p2)
    print(p1)
    print(p2)
    print()
    grunn_kopi = l1.grunn_kopi()
    print("Grunn kopiering: ")
    print(l1)
    print(grunn_kopi)
    print()
    l1.startpunkt.x_koordinat = 15
    print(l1)
    print(grunn_kopi)
    print()
    l1.sluttpunkt = p3
    print(l1)
    print(grunn_kopi)
    print()
    print("Dyp kopiering")
    dyp_kopi = l1.dyp_kopi()
    print(l1)
    print(dyp_kopi)
    print()
    l1.startpunkt.x_koordinat = 5
    print(l1)
    print(dyp_kopi)
    print()
    l2 = None
    l1 = Linjesegment(Punkt(1, 1), Punkt(6, 7))
