from sang import Sang
from spilleliste import Spilleliste
import os

allMusikk = Spilleliste('Hele musikkbiblioteket')
albumer = [allMusikk]
#sang1 = Sang("Lady Gaga and Bradley Cooper", "Shallow", "ode_to_joy.wav")

directory = os.getcwd()

# finner sanger (.wav filer) inni mapper og legger dem inni objektet 'allMusikk'
def finnMappeOgLegTilSanger(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            allMusikk.leggTilSang(Sang("", filename[:-4], directory + "\\" + filename))
            # denne for løkken fikser problemet hvis mappen er mellom to .wav filer
            # som fører til at den siste .wav filen regnes som om den er i mappen
            for x in albumer:
                if x.returnNavn() == directory.split("\\")[-1]:
                    x.leggTilSang(Sang("", filename[:-4], directory + "\\" + filename))
                    print("Added: ", os.path.join(directory, filename))
            # istedenfor hele for løkken så var det:
            # albumer[-1].leggTilSang(Sang("", filename[:-4], directory + "\\" + filename))
        elif filename[-4] != ".":
            albumName = filename
            nyAlbum = Spilleliste(albumName) # legge til albumer
            albumer.append(nyAlbum) # legge til albumer
            print("Inside ", albumName)
            directoryNew = directory + "\\" + albumName
            finnMappeOgLegTilSanger(directoryNew)

# stack overflow code so i can loop true the directory and find .wav files
for filename in os.listdir(directory):
    if filename == "music": # if it's the music folder loop inside it
        albumer.append(Spilleliste(filename))
        directoryMusic = directory + '\\' + filename
        finnMappeOgLegTilSanger(directoryMusic)
        ## Old code made better using finnMappeOgLegTilSanger() function
        # for filename2 in os.listdir(directoryMusic):
        #     ##print(filename2, " -4 =", filename2[:-4])
        #     if filename2.endswith(".wav"): # or filename2.endswith(".mp3"): mp3 not supported
        #         allMusikk.leggTilSang(Sang("", filename2[:-4], directoryMusic + "\\" + filename2)) # filename2[:-4] + filename2[-4:]
        #         print("Added: ", os.path.join(directoryMusic, filename2))
        #     else: # hvis det ikke ender med .mp3 eller .wav er det en mappe
        #         albumName = filename2
        #         print("Inside ", albumName)
        #         for song in os.listdir(directoryMusic + "\\" + albumName):
        #             if song.endswith(".wav"): # or song.endswith(".mp3"): mp3 not supported
        #                 allMusikk.leggTilSang(Sang("", song[:-4], directoryMusic + "\\" + albumName + "\\" + song)) # song[:-4] + song[-4:]
        #                 print("Added: ", os.path.join(directoryMusic, song))

# ser sanger og lar brukeren velge en sang den vil spille i en spilleliste
def seSanger(spilleliste):
    print("Velg hvilken sang du vil spille")
    i = 0
    for x in spilleliste.returnSanger():
        print(f"{i + 1}. {spilleliste.returnSangI(i)}")
        i += 1

    # checks if the playlist/album has any songs in it
    if i == 0:
        print("ingen sanger i spillelisten/albumet :c")
    else:
        choice = input("velg sang: ")
        i = 1
        for x in spilleliste.returnSanger():
            if choice == str(i):
                spilleliste.returnSangI(i - 1).spill() # indexen starter med 0 derfor i - 1
                nowPlaying = spilleliste.returnSangI(i - 1)
            i += 1
        

        input("Klikk enter for å avslutte Sangen: ")
        nowPlaying.stop()

# viser alle albumene i 'albumer' variabelen, og lar brukeren 
def seAlbumer():
    i = 0
    for x in albumer:
        print(f"{i + 1}. {x.returnNavn()}")
        i += 1
    
    choice = input("velg sang: ")
    i = 1
    for x in albumer:
        if choice == str(i):
            seSanger(x) # ser sanger og lar brukeren velge en sang den vil spille i en spilleliste
        i += 1

def hovedprogram():

    #print(allMusikk) ## debug
    #print("ALBUMER: ",albumer) ## debug
    # Metoden spill
    print("\n\n\n")
    print("Velg om du vil spille en bestemt album eller se alle sanger, skriv 1 eller 2")
    print("1. Se alle sanger")
    print("2. Se alle albumer")
    print("3. Avlsutt")

    choice = input("")
    if choice == "1":
        print("\n\n\n")
        seSanger(allMusikk) # ser sanger og lar brukeren velge en sang den vil spille i en spilleliste 
    elif choice == "2":
        print("\n\n\n")
        seAlbumer()
    if choice != "3":
        hovedprogram()

hovedprogram()
