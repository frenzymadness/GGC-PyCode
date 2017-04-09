def vigener(text, password, way):
    if way == 'crypt':
        smer = 1
    elif way == 'decrypt':
        smer = -1

    vysledek = ''
    for num, znak in enumerate(text):
        znak_z_hesla = password[num % len(password)]
        posun = ord(znak_z_hesla) * smer
        posunuty_znak = chr(ord(znak) + posun)
        vysledek += posunuty_znak

    return vysledek


txt = 'Hello, GEEK girls CARROTS'
crypted = vigener(txt, 'pepa', way='crypt')
decrypted = vigener(crypted, 'pepa', way='decrypt')

print('txt:', txt, '\ncrypted:', crypted, '\ndecrypted:', decrypted)
