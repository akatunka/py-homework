from random import randrange

radek = '--------------------'
print(radek)

def vyhodnot(pole):
    if 'xxx' in pole:
        vysledek = 'x'
    elif 'ooo' in pole:
        vysledek = 'o'
    elif '-' not in pole:
        vysledek = '!'
    else:
        vysledek = '-'
    return vysledek


def tah(pole, cislo_policka, symbol):
    pole = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole

def tah_hrace(pole):
    pozice = int(input('Zadej, na kterou pozici chces umistit symbol: '))
    while True:
        if pozice < 0:
            print('Zadal jsi zaporne cislo. Zadej cislo v intervalu [0,19].')
            pozice = int(input('Zadej, na kterou pozici chces umistit symbol: '))
        elif pozice > 19:
            print('Zadal jsi vysoke cislo. Zadej cislo v intervalu [0,19].')
            pozice = int(input('Zadej, na kterou pozici chces umistit symbol: '))
        elif pole[pozice] != '-':
            print('Tah nelze umistit na obsazenou pozici. Zadej znova.')
            pozice = int(input('Zadej, na kterou pozici chces umistit symbol: '))
        else:
            pole = tah(pole, pozice, 'x')
            break
    return pole

def tah_pocitace(pole):
    pozice = randrange(0,20)
    while True:
        if pole[pozice] != '-':
            pozice = randrange(0,20)
        else:
            pole = tah(pole, pozice, 'o')
            break
    return pole


def piskvorkyd1(pole):
    vysledek = vyhodnot(pole)

    while vysledek == '-':
        pole = tah_hrace(pole)
        print(pole)

        vysledek = vyhodnot(pole)
        if vysledek == 'x':
            print('Vyhral jsi!')
            break
        pole = tah_pocitace(pole)
        print(pole)

        vysledek = vyhodnot(pole)
        if vysledek == 'o':
            print('Vyhral pocitac!')
            break
        if vysledek == '!':
            print('Remiza')
            break


piskvorkyd1(radek)
