# Convertir vocales en mayuscula y consonantes en minuscula

word = input('Enter any word, please do not use numbers or special characters: ')
while not word.isalpha():
    word = input('Enter any word, please do not use numbers or special characters: ')
vowels = ['a','e','i','o','u']
finalword = []
for letter in word:
    if letter in vowels:
        may = letter.upper()
        finalword.append(may)
    else:
        min = letter.lower()
        finalword.append(min)

palabra = ''
for letter in finalword:
    palabra += letter
print (palabra)