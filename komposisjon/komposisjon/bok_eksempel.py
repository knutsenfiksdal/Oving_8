# Bok-eksemplet med delegering.
#
# Merk: Videoen tok bare starten av denne omskrivingen, merk at ved bruk
# av delegering forsvinner "fragile base class" problemet fra
# ArtikkelsamlingMedTeller, denne klassen bryr seg nå ikke
# om hvordan Artikkelsamling er implementert.

class Bok:
    def __init__(self, ISBN, tittel, beskrivelse, forfattere):
        self.ISBN = ISBN
        self.tittel = tittel
        self.beskrivelse = beskrivelse
        self.forfattere = forfattere

    def __str__(self):
        return f"Bok: {self.tittel}, ISBN: {self.ISBN}, skrevet av {self.forfattere}"

    def forfatterliste(self):
        resultat = "Forfattere: "
        for forfatter in self.forfattere:
            resultat += forfatter + ", "
        return resultat[0:len(resultat)-2]


class Fagbok:
    def __init__(self, ISBN, tittel, beskrivelse, forfattere, fagfelt, utgave):
        self.boka = Bok(ISBN, tittel, beskrivelse, forfattere)
        self.fagfelt = fagfelt
        self.utgave = utgave

    @property
    def tittel(self):
        return self.boka.tittel

    @property
    def ISBN(self):
        return self.boka.ISBN

    @property
    def beskrivelse(self):
        return self.boka.beskrivelse

    @property
    def forfattere(self):
        return self.boka.forfattere

    def __str__(self):
        return f"Fagbok: {self.tittel}, {self.utgave} utgave i fagfelt {self.fagfelt} " \
            f"ISBN: {self.ISBN}, skrevet av {self.forfattere}"

    def forfatterliste(self):
        return self.boka.forfatterliste()


class Fiksjonsbok:
    def __init__(self, ISBN, tittel, beskrivelse, forfattere, sjanger):
        self.boka = Bok(ISBN, tittel, beskrivelse, forfattere)
        self.sjanger = sjanger

    @property
    def tittel(self):
        return self.boka.tittel

    @property
    def ISBN(self):
        return self.boka.ISBN

    @property
    def beskrivelse(self):
        return self.boka.beskrivelse

    @property
    def forfattere(self):
        return self.boka.forfattere

    def forfatterliste(self):
        return self.boka.forfatterliste()

    def __str__(self):
        return str(self.boka)


class Artikkelsamling:
    def __init__(self, ISBN, tittel, beskrivelse, forfattere, fagfelt, utgave):
        self.fagboka = Fagbok(ISBN, tittel, beskrivelse, forfattere, fagfelt, utgave)
        self.artikler = []

    @property
    def tittel(self):
        return self.fagboka.tittel

    @property
    def ISBN(self):
        return self.fagboka.ISBN

    @property
    def beskrivelse(self):
        return self.fagboka.beskrivelse

    @property
    def forfattere(self):
        return self.fagboka.forfattere

    def __str__(self):
        return str(self.fagboka)

    def forfatterliste(self):
        return self.fagboka.forfatterliste()

    def legg_til_artikkel(self, artikkel):
        self.artikler.append(artikkel)

    def legg_til_artikler(self, artikler):
        for artikkel in artikler:
            self.legg_til_artikkel(artikkel)
#        self.artikler = self.artikler + artikler

    def innholdsfortegnelse(self):
        resultat = ""
        for indeks, artikkel in enumerate(self.artikler):
            resultat += f"{indeks}: {artikkel} \n"
        return resultat


class ArtikkelsamlingMedTeller:
    def __init__(self, ISBN, tittel, beskrivelse, forfattere, fagfelt, utgave):
        self.artikkelsamlingen = Artikkelsamling(ISBN, tittel, beskrivelse, forfattere, fagfelt, utgave)
        self.teller = 0

    @property
    def tittel(self):
        return self.artikkelsamlingen.tittel

    @property
    def ISBN(self):
        return self.artikkelsamlingen.ISBN

    @property
    def beskrivelse(self):
        return self.artikkelsamlingen.beskrivelse

    @property
    def forfattere(self):
        return self.artikkelsamlingen.forfattere

    def __str__(self):
        return str(self.artikkelsamlingen)

    def forfatterliste(self):
        return self.artikkelsamlingen.forfatterliste()

    def innholdsfortegnelse(self):
        return self.artikkelsamlingen.innholdsfortegnelse()

    def legg_til_artikkel(self, artikkel):
        self.artikkelsamlingen.legg_til_artikkel(artikkel)
        self.teller += 1

    def legg_til_artikler(self, artikler):
        self.artikkelsamlingen.legg_til_artikler(artikler)
        self.teller += len(artikler)


if __name__ == "__main__":
    boka = Bok("1-234-5678", "Testbok", "Test", ["Test forfatter"])
    print(boka)
    print(boka.forfatterliste())
    print()
    fagbok = Fagbok("5-2324-123", "Starting out with Python", "Programmering", ["Tony Gaddis"], "Programmering", 4)
    print(fagbok)
    print(fagbok.forfatterliste())
    print()
    fiksjonsbok = Fiksjonsbok("34535-35-1234", "Hobbiten", "There and back again", ["JRR Tolkien"], "Fantasy")
    print(fiksjonsbok)
    print(fiksjonsbok.forfatterliste())
    print()
    samling = ArtikkelsamlingMedTeller("345-32-124354", "Advanced database systems", "...",
                              ["Michael Stonebraker", "Tony Sellis"], "Databases", 2)
    samling.legg_til_artikkel("Test1")
    samling.legg_til_artikler(["Test2", "En artikkel til", "Tredje"])
    print(samling)
    print(samling.innholdsfortegnelse())
    print(samling.teller)
