# 题目1
ntxt = input("请输入4个数字（空格分隔）:")
nls = [str(n) for n in input().split()]

x0 = eval(nls[0])
y0 = eval(nls[1])
x1 = eval(nls[2])
y1 = eval(nls[3])
r = pow(pow(x1 - x0, 2) + pow(y1 - y0, 2), 0.5)
print("{:.2f}".format(r))

# 题目2
str1 = int(input("请输入："))
str2 = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
print(str2[(str1 % 12 + 9) % 12 - 1])

# 题目3
ID = input("请输入身份证：")
year = int(ID[6: 10])
month = int(ID[10: 12])
day = int(ID[12: 14])
print(str(year) + "年" + str(month) + "月" + str(day) + "日")
