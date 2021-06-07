#
#从键盘依次输入10个数，最后打印最大的数，10个数的和，和平均数
#
num=["0"]
i = 0
k = 0
print("请输入你想要输入的次数")
leng = int(input())
while i<leng:
    print("请输入你要输入的数字，还需要输入",leng-i,"次")
    sum = int(input())
    if i == 0:
       num[0] = sum
    else:
        num.append(sum)
    i+=1
i = 0
max = 0
while i<leng-1:
    if num[i] <= num[i+1]:
        max = num[i+1]
    else:
        max = num[i]
    i+=1
i = 0
while i<leng:
    k = k + num[i]
    i+=1
avg = k/leng


print("最大值为",max)
print("总和为",k)
print("平均值为",avg)


