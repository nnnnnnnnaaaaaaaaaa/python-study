numbers = [10,20,30]
numbers.append(40)
for i in numbers:
    print(i)
    
person = {"name": "Taro","age": 34}


print("名前は"+ person["name"] + "です")
print("年齢は"+ str(person["age"]) + "です")

abc = Python

print(abc.upper())
print(abc.replace("py","PY"))

import random
num = random.randint(1,10)
print(num)


try:
    num = int(input("入力して"))
    print(10/num)
except ValueError:
    print("fff")