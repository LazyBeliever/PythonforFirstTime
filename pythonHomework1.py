# 题目1
favourite = 271
print(favourite)

# 题目2
name = "crazyBeliever"
print("Hello " + name + ", will you marry me?")

# 题目3
names = ["aWei", "jieGe", "binBin", "crazyBeliever"]
for n in names:
    print(n)

# 题目4
stepNumber = int(input("请输入当天行走步数："))
# kaLuLi = stepNumber*2
print("今天消耗卡路里" + str(stepNumber * 2))

# 题目5
customer = ["ymh", "earth", "thunder", "crazyBeliever"]
for s in customer:
    print(s + ",我想邀请您共进晚餐，可以吗？")

# 题目6
animal = ["老虎", "雪豹", "狮子", "兔狲"]
for i, s in enumerate(animal, start=1):
    print(i, s)
    print(s+" 是猫科动物")

# 题目7
list1 = ["黄焖鸡米饭", "豉汁蒸肠头", "酸菜炒大肠", "八珍豆腐", "荔枝肉", "坛烧八味", "紫薯豌豆派", "上校鸡块", "胡辣汤"]
print("The first three items in the list are:", list1[:3])
print("Three items from the middle of the list are:", list1[3:6])
print("The last three items in the list are:", list1[-3:])

# 题目8
food = ""
Food = []
print("请输入您需要向披萨中添加的配料：")
while True:
    food = input()
    if food != "quit":
        print("我们将向披萨中添加:" + food)
        Food.append(food)
    else:
        break
