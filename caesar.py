def caesar(text, way):
    if way == 'crypt':
        num = 1
    elif way == 'decrypt':
        num = -1

    return ''.join([chr(ord(znak) + num) for znak in text])


txt = 'Hello, we are Geek Girls Carrots Ostrava'
crypted = caesar(txt, way='crypt')
decrypted = caesar(crypted, way='decrypt')

print('txt:', txt, '\ncrypted:', crypted, '\ndecrypted:', decrypted)
