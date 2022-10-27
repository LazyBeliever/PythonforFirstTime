fruit = {'apple': 6.5, 'banana': 3.5, 'origen': 3}
print(fruit)

# 用dict函数的话，key必须符合python的变量命名规则
# 下面的操作会覆盖上面的fruit
fruit = dict(gree=3)
print(fruit)

person = dict(name='lili', age=9, gender='female', height='150cm')
# 通过key获取value
print(person["age"])

print()
print("--------------------------------")
# 同一行中的if else ，
print("lili的体重是：", person["weight"] if "weight" in person else "字典里没有该项")
print("lili的身高是：", person["height"] if "height" in person else "字典里没有该项")

# get通过key获取value
print("lili的身高是：", person.get("height"))
print("lili的身高是：", person.get("weight"))
print("lili的身高是：", person.get("weight", "字典里没有该项"))

person["weight"] = 35  # 向字典中插入键值对
print("lili的体重是：", person.get("weight", "字典里没有该项"))

print()
print("--------------------------------")
person = {'firstName': "Believer", "lastName": "crazy", "age": 18, "city": "长垣"}
for i in person:
    print(i, end=" ")  # i遍历了key值
    print(person[i], end=" ")

print()
print("--------------------------------")
number = dict(crazyBeliever=271, aWei=2, binBin=7, jieGe=1)
for i in number:
    print(i + str(number[i]), end=" ")
    print(i, number[i], end=" ")

# 清空字典是clear()  清空后该对象仍然存在，但是里面没有数据了
# 删除字典是del
# del 后面跟字典名就把字典删了，跟person["weight"]就删除对应的键值对
# 字典被删除了，这个对象就不存在了

print()
print("--------------------------------")
# items()把键值对组成元组，把元组放在列表中返回

print(number.items())
for i in number.items():
    print(i)

print()
print("--------------------------------")
# str.title()所有单词的首字母都转化为大写
# str.upper() 所有字母都变成大写
firstname = {"zhang": "c", "li": "c++", "zhao": "java", "wu": "python"}
for s, language in firstname.items():  # 两个迭代遍历的话，key和value都会被迭代
    print(s, language)

for s, language in firstname.items():
    print(s.title() + " likes " + language.upper())

print()
print("--------------------------------")
# 一个键关联到多个值，可以在字典中嵌套列表
pizza = {"crust": "thick", "toppings": ["mushrooms", "cheese"]}
print(pizza)
print(pizza["crust"])
print(pizza["toppings"])

for topping in pizza["toppings"]:
    print(topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:" + str(languages))  # "\n" 是换行
    # for language in languages:
    # print(language.title())
    print(languages)

