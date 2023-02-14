nums = [[2,5,1,3,4,7],[1,2,3,4,4,3,2,1],[1,1,2,2]]
input()
contador,n = 0,0
list,out = [],[]
for lista in nums:
    n = len(lista)/2
    contador =0
    list = []
    while contador < n:
        num = lista[contador]
        ind = int(contador+n)
        num2 = lista[ind]
        list.append(num)
        list.append(num2)
        contador += 1
    out.append(list)
print(out)


