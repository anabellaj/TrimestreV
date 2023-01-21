print ('Hello! This program can help you calculate your final grade.')

while True:
    try:
        test_one = float(input('Please enter the grade of your first midterm: \n>>'))
        if (test_one)>20:
            print('\nPlease enter a valid number between 0 and 20.')
            continue
        else:
            test_one = float(test_one)*0.3 
            break
    except:
        print('\nPlease enter a valid number between 0 and 20.')
        continue 
while True:
    try:
        test_two = float(input('\nPlease enter the grade of your second midterm: \n>>'))
        if (test_two)>20:
            print('\nPlease enter a valid number between 0 and 20.')
            continue
        else:
            test_two = float(test_two)*0.3 
            break
    except:
        print('\nPlease enter a valid number between 0 and 20.')
        continue 
while True:
    try:
        quiz_one = float(input('\nPlease enter the grade of your first quiz: \n>>'))
        if (quiz_one)>20:
            print('\nPlease enter a valid number between 0 and 20.')
            continue
        else:
            quiz_one = float(quiz_one)*0.05 
            break
    except:
        print('\nPlease enter a valid number between 0 and 20.')
        continue 
while True:
    try:
        quiz_two = float(input('\nPlease enter the grade of your second quiz: \n>>'))
        if (quiz_two)>20:
            print('\nPlease enter a valid number between 0 and 20.')
            continue
        else:
            quiz_two = float(quiz_two)*0.05
            break
    except:
        print('\nPlease enter a valid number between 0 and 20.')
        continue
while True:
    try:
        proyect = float(input('\nPlease enter the grade of your final proyect: \n>>'))
        if (proyect)>20:
            print('\nPlease enter a valid number between 0 and 20.')
            continue
        else:
            proyect = float(proyect)*0.3
            break
    except:
        print('\nPlease enter a valid number between 0 and 20.')
        continue

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