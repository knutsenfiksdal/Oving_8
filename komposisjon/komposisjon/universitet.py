class Foreleser:
    def __init__(self, navn, kontor, emne=None):
        self.navn = navn
        self.kontor = kontor
        self.emne = emne

    @property
    def emne(self):
        return self.__emne

    @emne.setter
    def emne(self, nytt_emne):
        self.__emne = nytt_emne
        if nytt_emne is not None and nytt_emne.foreleser != self:
            nytt_emne.foreleser = self

    def __str__(self):
        if self.emne is None:
            emnestreng = "har ikke noe emne enda"
        else:
            emnestreng = "emne: " + self.emne.kode
        return f"Foreleser: {self.navn}, kontor {self.kontor}, {emnestreng}"


class Emne:
    def __init__(self, kode, navn, foreleser=None):
        self.kode = kode
        self.navn = navn
        self.foreleser = foreleser

    @property
    def foreleser(self):
        return self.__foreleser

    @foreleser.setter
    def foreleser(self, ny_foreleser):
        self.__foreleser = ny_foreleser
        if ny_foreleser is not None and ny_foreleser.emne != self:
            ny_foreleser.emne = self

    def __str__(self):
        if self.foreleser is None:
            foreleserstreng = "har ingen foreleser enda"
        else:
            foreleserstreng = f"foreleses av {self.foreleser.navn}"
        return f"Emne: {self.kode} {self.navn} {foreleserstreng}"


if __name__ == "__main__":
    foreleser = Foreleser("Erlend Tøssebro", "KE E-442")
    emne = Emne("DAT110", "Grunnleggende Programmering")
    print(foreleser)
    print(emne)
    foreleser.emne = emne
    print(foreleser)
    print(emne)
