# Se lee igual al derecho y al reves

word = input('Please enter any number or word: ')
test = list(word)
test.reverse()
compare = str(test)

if compare == str(list(word)):
    print (f'{word} es palindromo.')
else:
    print(f'{word} no es palindromo.')
