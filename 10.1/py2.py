import time
year = int(input("请输入一个年份："))
weightEarth = float(input("请输入你在地球上的体重(kg)："))
for i in range(1, year + 1):
    weight1 = weightEarth + 0.5 * i
    weight2 = weight1*0.165
    print("未来第{}年，你在地球上的体重是{:.2f}kg,在月球上的体重是{:.2f}kg".format(i, weight1, weight2))
    time.sleep(0.5)