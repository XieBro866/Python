s = float(input("请输入你的成绩："))
level ="A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "E"
print("你的成绩等级是：", level)