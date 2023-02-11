def oblongos(number):
    number = int(number)
    suma = False
    x, y = 1, 0
    for n in range(1, number+1):
        if n*(n + 1) == number:
            suma = True
    if suma == True:
        return x
    else:
        return y
        
def perfectos (number):
    number = int(number)
    x, y = 1,0
    suma = 0
    for divisor in range(1, number):
        if (number % divisor) == 0:
            suma += divisor
    if number == suma:
        return x
    else:
        return y
def abundantes(number):
    number = int(number)
    x, y = 1,0
    suma = 0
    for divisor in range(1, number):
        if (number % divisor) == 0:
            suma += divisor
    if number < suma:
        return x
    else:
        return y
def deficientes (number):
    number = int(number)
    x, y = 1,0
    suma = 0
    for divisor in range(1, number):
        if (number % divisor) == 0:
            suma += divisor
    if number > suma:
        return x
    else:
        return y
def palindromo(number):
    x,y= 1,0
    if str(number) == str(number)[::-1]:
        return x
    else:
        return y

def main():
    numeros = {
    'a': ([126, 306, 832, 264], [777, 592, 280, 562, 25], [918, 984, 251], [490, 13, 822], [454,
    495, 633, 357, 186], [949], [926, 940, 215, 725], [21, 18, 467, 660, 370], [915], [132, 437,
    467], [], [530, 304, 345, 398, 466], [256, 899], [], [925], [45], [824, 245, 447, 981, 84], [468,
    364], [158, 15], [704, 367, 812, 46], [], [], [601, 717, 423, 212]),
    'b': ([854], [633], [279], [741], [601, 258, 917], [522, 72, 848], [138, 558, 707, 708, 86], [91,
    63, 855, 205], [555, 152, 159], [211, 175, 570, 620], [589, 95, 373], [856, 100, 788], [990,
    544, 266], [619, 312, 106, 205], [223, 139, 893, 35, 921], [379, 129, 836, 948], [86, 593,
    897], [342, 734, 942, 210, 839], [486], [124], [777, 764, 852, 235], [947, 922], [993, 918,
    387]),
    'c': ([426, 804, 806], [978, 963], [986, 156, 53], [755, 238], [106, 803, 5, 747, 317], [126],
    [964, 832, 132, 904, 599], [], [740, 797, 784], [523, 551], [172], [487, 347], [255, 438, 464,
    450], [835], [], [619, 24], [256, 264, 985, 240], [554, 135, 260, 383, 183], [953, 882, 877],
    [607, 156, 106, 536], [677, 516], [701], [128]),
    'd': ([348, 768], [721, 832, 637, 477], [29], [973, 407], [107, 447], [], [970], [994, 534], [],
    [482, 399, 389, 788], [], [], [956, 87], [480], [86, 937], [], [143, 868, 596], [639, 434, 150, 462,
    651], [908, 551, 195, 454], [83, 245, 901], [538, 525, 83], [53], [6])
    }
    perf,abun,defici,palind,oblong = 0,0,0,0,0
    for key, value in numeros.items():
        for lists in value:
            for number in lists:
                perf += perfectos(number)
                abun += abundantes(number)
                defici += deficientes(number)
                palind += palindromo(number)
                oblong += oblongos(number)
    print('Numeros perfectos:',perf,'\nNumeros abundantes:',abun,'\nNumeros deficientes:', defici,'\nNumeros palindromos:', palind, '\nNumeros oblongos:',oblong)
main()

