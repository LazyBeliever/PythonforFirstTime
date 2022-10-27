a = int(input())
b = int(input())

i = 0
j = 1
while i <= min(a, b):
    print("a", j, "  b", i)
    i += 1
    if i == min(a, b) + 1:
        j = j + 1
        i = 1
    if i + j == a and i * j == b:
        print("Yes")
        break
    if j > max(a, b):
        print("No")
        break
