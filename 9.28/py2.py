sum = 0
tmp = 1
n = int(input("请输入一个整数:"))
for i in range(1,n+1):
    tmp *= i
    sum += tmp
print("计算结果为{}".format(sum))