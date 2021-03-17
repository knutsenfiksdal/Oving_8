class Rektangel:
    def __init__(self, start_x, start_y, bredde, hoyde):
        self.start_x = start_x
        self.start_y = start_y
        self.hoyde = hoyde
        self.bredde = bredde

    def areal(self):
        return self.bredde*self.hoyde

    # Endrer høyde og bredde på en slik måte at areal forblir det samme
    def strekk(self, multiplikator):
        self.bredde *= multiplikator
        self.hoyde /= multiplikator

    def __str__(self):
        return f"Rektangel fra ({self.start_x},  {self.start_y}), " \
            f"bredde {self.bredde}, høyde {self.hoyde}"


# Kvadrat som bruker komposisjon og delegering
class Kvadrat:
    def __init__(self, start_x, start_y, storrelse):
        self.rektanglet = Rektangel(start_x, start_y, storrelse, storrelse)

    @property
    def bredde(self):
        return self.rektanglet.bredde

    @property
    def hoyde(self):
        return self.rektanglet.hoyde

    @bredde.setter
    def bredde(self, ny_bredde):
        self.rektanglet.bredde = ny_bredde
        self.rektanglet.hoyde = ny_bredde

    @hoyde.setter
    def hoyde(self, ny_hoyde):
        self.rektanglet.bredde = ny_hoyde
        self.rektanglet.hoyde = ny_hoyde

    def areal(self):
        return self.rektanglet.areal()


if __name__ == "__main__":
    rektanglet = Rektangel(5, 5, 10, 5)
    print(rektanglet)
    print(rektanglet.areal())
    rektanglet.strekk(0.5)
    print(rektanglet)
    print(rektanglet.areal())
    kvadrat = Kvadrat(2, 2, 6)
    print(kvadrat)
    print(kvadrat.areal())
    kvadrat.strekk(6)
    print(kvadrat)
    print(kvadrat.areal())
