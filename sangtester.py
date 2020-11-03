from sang import Sang
from spilleliste import Spilleliste
import os

allMusikk = Spilleliste('Hele musikkbiblioteket')
albumer = [Spilleliste('Hele musikkbiblioteket')]
#sang1 = Sang("Lady Gaga and Bradley Cooper", "Shallow", "ode_to_joy.wav")

directory = os.getcwd()

# finner sanger (.wav filer) inni mapper og legger dem inni objektet 'allMusikk'
def finnMappeOgLegTilSanger(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            allMusikk.leggTilSang(Sang("", filename[:-4], directory + "\\" + filename))
            albumer[-1].leggTilSang(Sang("", filename[:-4], directory + "\\" + filename))
            print("Added: ", os.path.join(directory, filename))
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


def hovedprogram():

    print(allMusikk)
    print("ALBUMER: ",albumer)
    # Metoden spill
    print("Velg hvilken sang du vil spille")
    i = 0
    for x in allMusikk.returnSanger():
        print(f"{i + 1}. {allMusikk.returnSangI(i)}")
        i += 1
    choice = input("velg sang: ")
    i = 1
    for x in allMusikk.returnSanger():
        if choice == str(i):
            allMusikk.returnSangI(i - 1).spill() # indexen starter med 0 derfor i - 1
        i += 1
    input("Klikk enter for å avslutte: ")

    #hovedprogram()


hovedprogram()
