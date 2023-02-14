# Panagrama: que tenga todas las letras del abecedario
import string
alfabeto = set(string.ascii_lowercase)

def panagrama(word, alfabeto):
    panagram= False
    sobrantes = 0
    for letra in alfabeto:
        if letra not in word:
            sobrantes += 1
    if sobrantes == 0:
        panagram = True
    return panagram
            
    
def words():
    while True:
        try:
            word = input('Please enter your word:\n>> ')
            if word.isalnum():
                raise Exception
            break
        except:
            print('\nERROR - Please do not enter any numbers')
    return word.lower()

def main():
    alfabeto = set(string.ascii_lowercase)
    frase = words()
    panagram = panagrama(frase,alfabeto)
    if panagram:
        print('La frase', "'",frase,"'", 'es un panagrama.')
    else:
        print('La frase', "'",frase,"'", 'no es un panagrama.')    
main()