from kalkulator_backend import *

#printer en meny som vises på oppstart av kalkulatoren
def printMeny():
    print("------------------- Kalkulator -------------------")
    print("| 1. Legg sammen (pluss)                         |")
    print("| 2. Trekk fra   (minus)                         |")
    print("| 3. Gange       (gange)                         |")
    print("| 4. Dele        (deling)                        |")
    print("| 5. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Velg operasjon fra menyen: ")
    utfoerMenyvalg(menyvalg)
# utfører en funksjon som ser hva brukeren har valgt fra menyen


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        leggSammen()
        pause_og_fortsett()
    elif valgtTall == "2":
        trekkFra()
        pause_og_fortsett()
    elif valgtTall == "3":
        gange()
    elif valgtTall == "4":
        divisjon()
        # kjører funskjoner basert på hvilket tall som er valgt
    elif valgtTall == "5":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j" or bekreftelse == "Y" or bekreftelse == "y"):
            exit()
            # bekrefter om du vil avslutte kalkulatoren
        else:
            printMeny()
    else:
        nyttForsoek = input("*** Ugyldig valg."
                            "Velg et tall mellom 1-4."
                            " Trykk for å fortsette *** ")
        printMeny()
        # hvis den ikke ser et gyldig tall vil den reprinte menyen og si ugyldig valg


def pause_og_fortsett():
    input("-- Trykk en tast for å fortsette --")
    printMeny()


printMeny()