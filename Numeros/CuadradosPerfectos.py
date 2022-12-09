# Resultado al elevar cualquier numero natural al cuadrado

num = input('Please enter a number: ')
while not num.isnumeric():
    num = input('Please enter a number: ')
num = int(num)

square = num**0.5

if square / int(square) == 1:
    print (f'{num} is a square number.')
else:
    print (f'{num} is not a square number.')
