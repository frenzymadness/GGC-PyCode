def transpose(text, columns):

    tabulka = []

    for n in range((len(text) // columns) + 1):
        kus = text[n * columns: (n + 1) * columns]
        if kus:
            tabulka.append(list(kus))

    vysledek = ''

    for sloupec in range(columns):
        for radek in range(len(tabulka)):
            try:
                vysledek += tabulka[radek][sloupec]
            except IndexError:
                pass

    return vysledek, len(tabulka)


txt = 'Hello, we are Geek Girls Carrots Ostrava'

crypted, delka = transpose(txt, 3)
decrypted, _ = transpose(crypted, delka)

print('txt:', txt, '\ncrypted:', crypted, '\ndecrypted:', decrypted)
