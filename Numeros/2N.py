nums = [[2,5,1,3,4,7],[1,2,3,4,4,3,2,1],[1,1,2,2]]
input()
count,contador,n = 0,0,0
list,out = [],[]
while True:
    while count<= n:
        while count <= len(nums):
            for lista in nums:
                if contador == nums.index(lista):
                    n= len(lista)/2
                    count+=1
        for lista in nums:
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
        

