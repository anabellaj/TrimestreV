#Print n terms of the fibonacci sequence
#In fibonacci, the n term is the sum of the two previous terms. The first term is 0 and the second 1.

n = input('How many terms of the Fibonacci sequence do you wish to show?\n>> Please enter an integer number: ')
while not  n.isnumeric():
    n = input('>> Please enter an integer number: ')
n = int (n)
term1 = 0
term2 = 1
count = 0
fibonacci = []
while count < n:
    fibonacci.append(term1)
    new_term = term1 + term2
    term1 = term2
    term2 = new_term
    count += 1
print (fibonacci)    