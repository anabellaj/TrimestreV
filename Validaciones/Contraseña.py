# Validate password


max = False
min = False
num = False
special = False
run = True

while run == True:
    password = input('Please enter your password: \n>>')

    # 8 caracteres
    if len(password) >= 8:
        pass
    else:
        print ('The password needs to have at least 8 characters.')
        continue

    # uppercase and lowercase
    for letter in password:
        if letter.isupper() == True:
            max = True
        if letter.islower() == True:
            min = True
    if max and min == True:
        pass
    else:
        print('The password needs to have at least one uppercase and one lowercase letter.')
        continue

    # Numeros y letras
    for letter in password:
        if letter.isalnum():
            num = True
        if letter == '@' or letter == '_' or letter == '$':
            special = True
    if num and special == True:
        pass
    else: 
        print('The password has to contain letter, numbers and a special character ("@", "_", "$")')
        continue
    
    if max and min and num and special == True:
        print (f'{password} is a valid password.')
        run = False
    else:
        continue