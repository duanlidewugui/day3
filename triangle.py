#
#从键盘输入任意三边，判断是否能形成三角形，
# 若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
#
i = 0
sides = [0,0,0]
while i<3:
    print("请输入三角形的第",i+1,"个边的长度,只能输入数字")
    sides[i]=int(input())
    i+=1
#接下来的循环时对数组的数字进行从小到大的排列
i = 0
while i<2:
    k = 0
    while k<2:
        if sides[k]>sides[k+1]:
            t = sides[k]
            sides[k] = sides[k+1]
            sides[k+1] = t
        k+=1
    i+=1

print(sides)

if sides[0]+sides[1]<=sides[2]:
    print("不能组成三角形")
elif sides[0]==sides[1] and sides[1]==sides[2]:
    print("能组成等边三角形")
elif sides[0]==sides[1] or sides[1]==sides[2]:
    if sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2]:
        print("是等腰直角三角形")
    else:
        print("是等腰三角形")
elif sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2]:
    print("是直角三角形")
else:
    print("是普通三角形")