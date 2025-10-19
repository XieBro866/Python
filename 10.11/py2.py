x = int(input("请输入一个整数："))
y = int(input("请输入另一个整数："))
sum_xy = x + y
print("两个整数的和是：", sum_xy)
product_xy = x * y
print("两个整数的积是：", product_xy)
difference_xy = x - y
print("两个整数的差是：", difference_xy)
try:
        quotient = x / y
        print("两个整数的商是：", quotient)
except ZeroDivisionError:
        print("输入数字不支持求商")
