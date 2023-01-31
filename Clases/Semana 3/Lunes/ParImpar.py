even, odd, numbers_list = [],[],[]
print ('Hello! Today you will separate numbers in odd and even.')
while True:
    numbers = input ('Please enter any integer number:\n>>')
    while not numbers.isnumeric():
        numbers = input ('Please enter any integer number:\n>>')
    numbers = int(numbers)
    numbers_list.append(numbers)
    run = input ('Do you wish to enter more numbers?\nPress 1 to continue or any key to exit\n>> ')
    if run != '1':
        break
    else:
        continue

for n in numbers_list:
    if int(n)%2 == 0:
        even.append(n)
    elif int(n)%2 != 0:
        odd.append(n)

print (f'The even numbers are {even} and the odd numbers are {odd}.')
