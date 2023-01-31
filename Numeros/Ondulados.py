# Siguen la estructura ababab, por ej. 13131 o 545
while True:
    try:
        number = int(input('Please enter an integer number to check if it is ondulated:\n>>'))
        break
    except:
        print ('\nEnter a valid integer numbers. Remember no letters or special characters.')
        continue
ondulado = True
count = 0
even_index = list(str(number))[0]
odd_index = list(str(number))[1]

if number < 100:
    print(f'The number {number} is an ondulated number.')
elif even_index == odd_index:
    print (f'The number {number} is not an ondulated number.')
else:
    for x in str(number):
        if (count+2)%2 == 0:
            if x != even_index:
                ondulado = False
            count +=1
        elif (count+2) %2 !=0:
            if x != odd_index:
                ondulado = False
            count += 1
    if ondulado == True:
        print(f'The number {number} is an ondulated number.')
    else:
        print (f'The number {number} is not an ondulated number.')