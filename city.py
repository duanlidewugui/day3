#有一个列表，[“北京”,”上海”,”广东”]
#1)将中国所有省会城市添加到上述列表中
#2)广东成为第二大发达城市，将广东排在上海前面
#
#3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
#这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
#


citys = ["北京","上海","广东"]
capitals = (["兰州","西宁","西安","郑州","济南","太原","合肥","长沙","武汉","南京",
            "成都","贵阳","昆明","哈尔滨","长春","沈阳","石家庄","杭州","南昌",
             "广州","福州","台北","海口 "])
#将中国所有省会城市添加到上述列表中
i = 0
print(len(capitals))
while i < len(capitals):
    citys.append(capitals[i])
    i += 1

#可以将某个城市单独拿出来，再放到其他城市前面，被插队的城市位置全部往后挪一位
print(citys)
t = -1
take = "null"
while 1 == 1:
    take = input("请输入您想要拿出的城市")
    i = 0
    while i < len(citys):
        if take == citys[i]:
            t = i
            break
        i += 1
    if t == -1:
        print("输入字符错误，没有找到您想找的城市")
    else:
        break

m = -1
move = "null"
while 1 == 1:
    move = input("请输入您想将刚刚拿出的放到的那个城市前面")
    i = 0
    while i < len(citys):
        if move == citys[i]:
            m = i
            break
        i += 1
    if m == -1:
        print("输入字符错误，没有找到您想找的城市")
    else:
        break
#
if t < m:
    city = citys[t]
    del citys[t]
    citys.insert(m-1,city)
else:
    city = citys[t]
    del citys[t]
    citys.insert(m,city)

print(citys)
#这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
gdps = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
i = 0
gdp = 0
while i<len(gdps):
    gdp = gdp + gdps[i]
    i += 1
ave = gdp/len(gdps)
print("gdp总和",gdp)
print("平均gdp为",ave)






