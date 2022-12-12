# Cambiar domain a @unimet.edu.ve

email = input('Please enter your complete email address: \n>>')
while email.isnumeric():
    email = input('Please enter your complete email address: \n>>')
mail = list(email)
validate = mail.count('@')
while validate != 1:
    email = input('Please enter your complete email address: \n>>')

print(email[:email.find('@')] + '@unimet.edu.ve')
