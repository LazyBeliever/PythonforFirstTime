s = "我想出去玩"
print(s)
for i in s:
    print(i, end="_")

food = {"奶茶", "苹果", "羊肉"}
for i, element in enumerate(food):
    print(i + 1, element)

for i, element in enumerate(food, start=1):
    print(i, element)

for i in food:
    print(i)

for i in range(1, 21, 2):
    print(i)

temp = list(range(1, 20, 2))
for i in temp:
    print(i)

i = 1
while i <= 30:
    print(i)
    i += 1
print("数够30只羊，睡觉！")
