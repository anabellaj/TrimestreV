#traducir palabras espanol-ingles

diccionario= {}
words = input('Ingrese el diccionario en el siguiente formato <palabra>:<traducción> divididas por comas: \n>> ')
translate = words.split(',')
for pair in translate:
    values = pair.split(':')
    keys = values[0]
    value_dict = values[1]
    diccionario[keys]= value_dict
    
phrase_input = input ('Please enter a phrase to translate: \n>>')
word_list= phrase_input.split(' ')
result_words= ''
for word in word_list:
    result_words += diccionario.get(word,word)
    result_words += ' '

print (result_words)