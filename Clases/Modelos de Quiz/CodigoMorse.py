traductor={'---':'o',
'.-..':'l',
'-..':'d',
'--.':'g',
'.-':'a',
'.-.':'r',
}
input()
frase='.-1.s.  -7-8-  -x-9.  .-0.  .f-  -m..  -q-i-'
frase = frase.split()
decifrado = []
fr = ''
for d in frase:
    for letter in d:
        if letter == '.' or letter == '-':
            fr += letter 
    decifrado.append(fr)
    fr = ''
final = ''
for codigo in decifrado:
    if codigo in traductor.keys():
        final += traductor[codigo]
print (final)