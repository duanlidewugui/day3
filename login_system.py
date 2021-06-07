#
#实现登陆系统的三次密码输入错误锁定功能
# （用户名：root,密码：admin）
#
print("已进入注册界面")
while 1==1 :
    print("请输入您要注册的用户名")
    root = input()
    print("请输入你的新密码")
    admin = input()
    print("请再输入您的新密码")
    admin_backup = input()
    if admin == admin_backup:
        print("已进入登陆界面")
        break
    else:
        print("密码输入错误，请重新注册")
        print("已进入注册界面")
key = 0
while key<3:
    print("\t\t\t登陆界面\t\t\t")
    root_backup = input("请输入您的用户名")
    admin_backup = input("请输入您的密码")
    if root == root_backup and admin ==admin_backup:
        print("用户名和密码输入成功，即将登陆")
        break
    elif root == root_backup:
        print("密码输入错误，即将重新进入登陆界面")
    elif admin ==admin_backup:
        print("用户名输入错误，即将重新进入登陆界面")
    else:
        print("用户名和密码输入错误,即将重新进入登陆界面")

    key +=1
    if key == 3:
        print("当日输入次数已达上限，系统已锁定")
    else:
        print("你还能输入",3-key,"次")


if key<3:
    print("已成功登陆系统",root,"欢迎您的回归")
else:
    print("系统锁定中，无法登陆")