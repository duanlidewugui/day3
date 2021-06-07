#
#一只青蛙掉在井里了，井高20米，
# 青蛙白天往上爬3米，晚上下滑2米，
# 问第几天能出来？请编程求出。
#

#掉下去的天数
day = 1
#距离井口的米数
meter = 20

while meter>0:
    meter -= 3
    if meter<=0:
        break
    meter += 2
    day += 1

print("青蛙跳出来了")
print("青蛙总共跳了",day,"天")
