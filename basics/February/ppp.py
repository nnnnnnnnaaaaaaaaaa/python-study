a = 5
b = 3
print(a + b)

age = 34
print("私は" + str(age) + "です")

score = 75
if score >= 60:
    print("合格")
else:
    print("不合格")

x = 1

while x < 6:
    print(x)
    x += 1

def add(a,b):
    return a + b
print(add(3,4))

def multiply(a,b):
    return a * b
print(multiply(3,5))

def is_even(a):
    return a % 2 == 0
print(is_even(4))

def big(a,b):
    if a > b :
        return a
    else:
        return b
print(big(3,8))