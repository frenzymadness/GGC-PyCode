def vykresli(pole):
    for radek in sorted(pole.keys()):
        for bunka in pole[radek]:
            print(bunka, end=' ')
        print()


def tah(herni_pole, radek, sloupec):
    string = ''.join([''.join(herni_pole[nazev]) for nazev in herni_pole])
    if string.count('X') > string.count('O'):
        symbol = 'O'
    else:
        symbol = 'X'
    herni_pole[radek][sloupec] = symbol
    return herni_pole


def tah_hrace(herni_pole):
    while True:
        pozice = input('Zadej pismeno sloupce a cislo radku (napr. A0): ')
        radek, sloupec = pozice
        sloupec = int(sloupec)
        if sloupec > 2 or sloupec < 0:
            print('Neplatne cislo sloupce')
            continue
        if radek not in ['A', 'B', 'C']:
            print('Neplatny radek')
            continue

        if herni_pole[radek][sloupec] != '-':
            print('Pole je obsazene')
            continue

        return tah(herni_pole, radek, sloupec)


def vyhodnot(herni_pole):
    for symbol in ['X', 'O']:
        # Radky
        for radek in herni_pole.keys():
            if symbol * 3 == ''.join(herni_pole[radek]):
                return symbol
        # Sloupce
        for sloupec in range(3):
            obsah_sloupce = ''.join(herni_pole[radek][sloupec] for radek in herni_pole.keys())
            if symbol * 3 == obsah_sloupce:
                return symbol
        # Diagonaly
        # Hlavni
        radky = sorted(list(herni_pole.keys()))
        sloupce = list(range(3))
        obsah_diagonaly = ''.join(herni_pole[radek][sloupec] for radek, sloupec in zip(radky, sloupce))
        if symbol * 3 == obsah_diagonaly:
            return symbol
        # Vedlejsi
        radky = sorted(list(herni_pole.keys()))
        sloupce = list(range(2, -1, -1))
        obsah_diagonaly = ''.join(herni_pole[radek][sloupec] for radek, sloupec in zip(radky, sloupce))
        if symbol * 3 == obsah_diagonaly:
            return symbol

    obsah_pole = ''.join(''.join(herni_pole[radek]) for radek in herni_pole.keys())
    if '-' not in obsah_pole:
        return '!'
    else:
        return '-'


def piskvorky():
    radky = ['A', 'B', 'C']
    herni_pole = {radek: ['-' for x in range(3)] for radek in radky}

    print('Start hry')

    while True:
        vykresli(herni_pole)
        herni_pole = tah_hrace(herni_pole)

        vyhodnoceni = vyhodnot(herni_pole)

        if vyhodnoceni == 'X' or vyhodnoceni == 'O':
            print('Vyhral hrac {}'.format(vyhodnoceni))
            break
        if vyhodnoceni == '!':
            print('Remiza!')
            break
        if vyhodnoceni == '-':
            print('Hrajeme dal')


if __name__ == '__main__':
    piskvorky()
