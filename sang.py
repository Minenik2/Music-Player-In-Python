import simpleaudio as sa


class Sang:  # lager klasse
    def __init__(self, artist, tittel, filnavn):  # konstruktør
        self._artist = artist
        self._tittel = tittel
        self._filnavn = filnavn

    # Frivillig (nyttig!) utvidelse: Implementere __str__ metoder
    def __str__(self):
        return f"{self._artist} - {self._tittel}"

    def spill(self):  # spiller av musikken i sangen den kalles for
        print("setter inn:", self._filnavn)
        wave_obj = sa.WaveObject.from_wave_file(self._filnavn)
        play_obj = wave_obj.play()
        #play_obj.wait_done()

        # print(f"Spiller: {self}")  # ! bruk av __str__metode
        # return f"Spiller: {self._artist} - {self._tittel}"

    # returnerer true dersom ett eller fler av navnene i strengen navn finnes i _artist, ellers False
    def sjekkArtist(self, navn):
        splitNavn = navn.split(" ")
        splitArtist = self._artist.split(" ")
        for x in splitNavn:
            for y in splitArtist:
                if x == y:  # man kan legge til .lower() men obligen spør ikke
                    return True
        return False

    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False

    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkTittel(tittel) and self.sjekkArtist(artist):
            return True
        else:
            return False
