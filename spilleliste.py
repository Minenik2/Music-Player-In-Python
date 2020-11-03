from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    # Frivillig (nyttig!) utvidelse: Implementere __str__ metoder
    def __str__(self):
        return f"Sanger: '{self._sanger}'\nNavn: {self._navn}"

    def lesFraFil(self, filnavn):
        fil = open(filnavn)
        for linje in fil:
            data = linje.strip().split(";")
            self._sanger.append(Sang(data[1], data[0]))  # Sang(artist, tittel)

        fil.close()  # lukker filen

    def leggTilSang(self, nySang):
        # går utifra at bare et objekt kommer in som argument for nySang
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        i = 0
        for x in self._sanger:
            if sang == x:
                self._sanger.pop(i)
            i += 1

    def spillSang(self, sang):
        sang.spill()  # bruker __str__metoden i spill() funksjonen
        # return sang

    def spillAlle(self):  # spiller hver enkelt sang i listen
        for x in self._sanger:
            x.spill()  # bruker __str__metoden i spill() funksjonen
        # man kan også putte dem i en liste og returnere listen hvis vi ikke vil ha print statements i klasser

    def finnSang(self, tittel):
        for x in self._sanger:
            if x.sjekkTittel(tittel):
                return x

    # Metoden går gjennom alle sanger i spillelisten og tar vare på de som har en eller flere navn fra parameteren artistnavn i navnet på artisten.
    #  Disse returneres i en liste med sanger
    def hentArtistUtvalg(self, artistnavn):
        liste = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                liste.append(x)
        return liste

    def returnSangI(self, i):
        return self._sanger[i]
    
    def returnSanger(self):
        return self._sanger
