#
#有以下一个列表，求其中是5的倍数的和
#a = [1,5,21,30,15,9,30,24]

a = [1,5,21,30,15,9,30,24]
sum = 0
i = 0
while i<len(a):
    if a[i] % 5 == 0:
        sum = sum + a[i]
    i+=1
print("列表中是5倍数的数的和为",sum)


