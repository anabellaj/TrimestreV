# numeros = [ 1,2,34,86,4,5,99,890,45]
# pares = [num for num in numeros if num % 2== 0]
# print (pares)

squares = [x**2  if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)