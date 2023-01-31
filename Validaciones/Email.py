# Entre 0 y 50 caracteres
# 1 solo @, pero no puede empezar ni terminar en @
print ('Hello! Here you can validate your email address.')
while True:
    email = input('\nPlease enter your email address:\n>> ')
    if len(email) == 0 or len(email) > 50:
        print ('---------------------ERROR---------------------\n>> Remember that your email address must have between 1 and 50 characters.\nPlease try again.')
        continue
    email_list = []
    for letter in email:
        email_list.append(letter)
    if email_list [0] == '@' or email_list[0]== '/' or email_list[0] == '.':
        print ('\n\t---------------------ERROR---------------------\nRemember that your email address cannot start with @, . or /.\nPlease try again.')
        continue
    if email_list.count('@') != 1:
        print ('\n\t---------------------ERROR---------------------\nRemember that your email address must contain one "@".\nPlease try again.')
    else:
        print (f'{email} is a valid email address.')