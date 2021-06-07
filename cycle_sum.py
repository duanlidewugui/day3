#
#
#使用while编程实现求n-m以内的数的和！
sum = 0
print("可以求出n到m以内所有数的和")
n = int(input("请输入n"))
m = int(input("请输入m"))
while n<m+1:
    sum = sum+n
    n+=1
if sum == 0:
    print("n不能大于m")
else:
    print("最后求和为",sum)


