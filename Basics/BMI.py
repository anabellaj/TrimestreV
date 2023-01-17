# Imprimir el BMI con dos decimales

height = input('Please enter your height in cm:\n>')
while not height.isnumeric() or len(height) < 2 or len(height) > 4:
    height = input('Please enter your height in cm:\n')
height = float(height)

weight = input('Please enter your weight in kg:\n>')
while not weight.isnumeric() or len(weight) > 4:
    weight = input('Please enter your weight in kg:\n')
weight = float(weight)

height = height/100
heightsquared = height**2
bmi = weight / heightsquared
roundedbmi = round(bmi, 2)

print (f'Your BMI is {roundedbmi}')