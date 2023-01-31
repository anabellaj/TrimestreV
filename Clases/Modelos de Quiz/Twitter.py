# EJ: Quiz 1 / Ejercicio 1
# Censurar palabras
palabras_censuradas = ['racismo','terrorista', 'peligro', 'miedo', 'odio']
# Reemplazar las palabras censuradas por el caracter elegido por el usuario
tweet = input('Ingrese su tweet por favor:\n>>')
special_chr = input('Ingrese el caracter que desea utilizar para censurar su tweet\n>>')

for x in palabras_censuradas:
    tweet = tweet.replace(x, special_chr * len(x)) # Palabra a reemplazar, con que se reemplaza

print (tweet)