#
#实现输入10个数字，并打印10个数的求和结果
#
nums=["0"]
i = 0
k = 0
print("请输入你想要输入的次数")
leng = int(input())
while i<leng:
    print("请输入你要输入的数字，还需要输入",leng-i,"次")
    sum = int(input())
    if i == 0:
       nums[0] = sum
    else:
        nums.append(sum)

    i+=1
i = 0
while i<len(nums):
    k = k + nums[i]
    i+=1
print("总和为",k)