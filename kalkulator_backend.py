def leggSammen():
    tall1 = input("Skriv inn det første tallet: ") 
    tall2 = input("Skriv inn det andre tallet: ")
    sum = int(tall1) + int(tall2)  #tar tall1 og tall2 og plusser de sammen
    print(f'{tall2} + {tall2} = {sum}')


def trekkFra():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    diff = int(tall1) - int(tall2)
    print(f'{tall2} - {tall2} = {diff}')  #tar tall1 minus tall 2


''' Her er noen påbegynte tanker til utvidelse
def gange():
    produkt = 3*3
    TODO: Gjøre ferdig '''


def divisjon():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    if tall2 != 0:                      #gjør sånn at det andre tallet ikke kan være 0
        kvotient = int(tall1) / int(tall2)
        print(f'{tall2} / {tall2} = {kvotient}')  #tar tall1 dividert på tall2
    else:
        print("Ugyldig division, det andre tallet kan ikke være 0.")