num = input('Please enter a number: ')
while num.isnumeric() == False:
    num = input('Please enter a number: ')
num = int(num)

if (num%2) != 0:
    print(f'El numero {num} es impar.')
else:
    print(f'El numero {num} es par.')
