mesice = ['leden', 'unor', 'brezen', 'duben', 'kveten', 'cerven',
          'cervenec', 'srpen', 'zari', 'rijen', 'listopad', 'prosinec']
dny = {'leden': 31, 'unor': 28, 'brezen': 31, 'duben': 30, 'kveten': 31,
       'cerven': 30, 'cervenec': 31, 'srpen': 31, 'zari': 30, 'rijen': 31,
       'listopad': 30, 'prosinec': 31}

mesic = input('Zadej mesic: ')
dny_v_mesici = dny[mesic]


def vypis_mesic(pocet_dni, posun=0):
    for den in range(1, pocet_dni + posun + 1):
        if den <= posun:
            print('  ', end=' ')
        elif den % 7 == 0:
            print(str(den - posun).zfill(2))
        else:
            print(str(den - posun).zfill(2), end=' ')

    return den % 7


print('## Varianta 1')

vypis_mesic(dny_v_mesici)

print('\n\n## Varianta 2')

posun = int(input('Zadej posun ve dnech: '))

vypis_mesic(dny_v_mesici, posun)

print('\n\n## Varianta 3')

cislo_mesice = mesice.index(mesic)

for m in range(cislo_mesice, cislo_mesice + 12):
    if m > 11:
        m -= 12

    jmeno_mesice = mesice[m]
    pocet_dni = dny[jmeno_mesice]

    print(jmeno_mesice)

    posun = vypis_mesic(pocet_dni, posun)

    print('\n\n')
