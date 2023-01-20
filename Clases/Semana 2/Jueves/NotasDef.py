print ('Hello! This program can help you calculate your final grade.')

test_one = input('Please enter the grade of your first midterm: \n>>')
while test_one.isnumeric() == False or float(test_one)>20:
    test_one = input('\nPlease enter a valid number: \n>>')
test_one = float(test_one)*0.3

test_two = input ('Please enter the grade of your second midterm: \n>>')
while test_two.isnumeric() == False or float(test_two)>20:
    test_two = input('\nPlease enter a valid number: \n>>')
test_two = float(test_two)*0.3

quiz_one = input('Please enter the grade of your first quiz: \n>>')
while quiz_one.isnumeric() == False or float(quiz_one)>20:
    quiz_one = input('\nPlease enter a valid number: \n>>')
quiz_one = float (quiz_one)*0.05

quiz_two = input('Please enter the grade of your second quiz: \n>>')
while quiz_two.isnumeric() == False or float(quiz_two)>20:
    quiz_two = input('\nPlease enter a valid number: \n>>')
quiz_two = float(quiz_two)*0.05

proyect = input('Please enter the grade of your proyect: \n>>')
while proyect.isnumeric() == False or float(proyect)>20:
    proyect = input('\nPlease enter a valid number: \n>>')
proyect = float(proyect)*0.3

test_sums = test_one + test_two
final_grade = test_one + test_two + quiz_one + quiz_two + proyect

if test_sums >= 6:
    print ('Your final grade is', final_grade)
    if final_grade >= 6:
        print ('You have passed this course.')
    else:
        print ('You have failed this course.')
else:
    print ('Your final grade is', test_sums)
    print ('You have failed this course.')