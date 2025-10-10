import random

a = random.randint(0, 1000)
i = 0
print("请在 {} 到 {} 之间猜一个整数".format(0, 1000))

while True:
    b = input("请输入你猜的数字：")
    b = float(b)
    if b.is_integer():
            b = int(b)  
            if b < a:
                print("你猜的数字小了")
            elif b > a:
                print("你猜的数字大了")
            else:
                i += 1
                print("这是你猜的第 {} 次，猜对了，恭喜你！".format(i))
                break
            i += 1
    else:
            print("请输入一个整数！")



