# Remplazar G por G, () por O y (al) por al
# Usar .replace()
def goal_parser(word):
    sub = {'G': 'G', '()': 'o', '(al)': 'al'}
    for char in sub.keys():
        word = word.replace(char, sub[char])
    return word

def main():
    word = input('Please enter the word you wish to replace: ')
    print (goal_parser(word))
main()
