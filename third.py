for i in range(100):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(i)
"""
for number in range(11):
    if number % 3 != 0:
        print(number)
"""

"""
count = 0
for i in range(1,10):
    if i % 2 == 0:
        count += 1
print(count)

"""

age = int(input("你的年龄："))
money = 0
if age < 4:
    money = 0
elif age < 18:
    money = 25
elif age < 40:
    money = 40
elif age >= 65:
    money = 20
print("您的票价为：", money)

print("we", money, "family")
