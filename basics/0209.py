"""#写経8-1
def greet():
    print("hello")
    
greet()

#写経8-2
def double(num):
    return num * 2

result = double(4)
print(result)

#演習15
def say_hi():  #下行を表示するために必要に定義する
    print("Hi Python")  #上行が実行されると表示される
say_hi()  #実行することで上行が表示される

#演習16
def triple(num):  #numが入っているtriple関数を定義する
    return num * 3  #引数のnumを取り出し×3にする
result = triple(5)  #result変数にtriple関数を入れる（前行で×3にしてる）
print(result)  #5×3で15の結果が入る

#写経9
def print_items(items):
    for item in items:
        print(item)
        
fruits = ["apple","banana","orange"]
print_items(fruits)

#演習17
def a(ab):
    for ac in ab:
        print(ac)
        
b = ["taro","koharu","kinako"]
a(b)

#演習18
def aa(bb):
    for cc in bb:
        print(cc * 2)
        
zz = [2,4,6]
aa(zz)

#写経10
def add_one(num):
    return num + 1

result = add_one(5)
print(result)

#演習19
def a(friend):
    return friend *3
result = a(6)
print(result)

#演習20
def b(aa,bb):
    return aa + bb
result = b(6,6)
print(result)

#ルール2
#1
names = ["hanako","taro","jiro"]
for i in names:
    print(i)
    
#2
values = [10, 20, 30, 40]
for j in values:
    print(j)
    
#3
prices = [150, 300, 450]
for k in prices:
    print(k * 2)
    
#4
levels = [1, 4, 7]
for l in levels:
    print( l + 5)
    
#5
numbers = [6, 9, 12, 15]
for m in numbers:
    if m % 2 == 0:
        print(m)
        
#6
ages = [14, 18, 20, 16, 25]
for n in ages:
    if n >= 18:
        print(n)
        
#7
points = [2, 4, 6]
result = []
for o in points:
    result.append(o * 3)

print(result)

#8
scores = [5, 7, 9]
result = []
for p in scores:
    result.append(p + 10)
    
print(result)

#9
for q in range(5):
    print(q)
    
#10
for r in range(1,7):
    print(r)
    
#11
result = []
for s in range(1,5):
    result.append(s * 3)
print(result)
    
#12
result = []
for t in range(2,7):
    result.append(t + 10)
print(result)

#13
nums = [3, 10, 7, 15, 8]
result = []
for u in nums:
    if u >= 10:
        result.append(u)
print(result)

#14
scores = [1, 4, 6, 9, 12]
result = []
for v in scores:
    if v % 2 == 0:
        result.append(v)
print(result)

#15
def w():
    print("Hello World")
    
w()

#16
def x(y):
    return y * 2
result = x(5)
print(result)


#=================================
#1
items = ["pen","note","eraser"]
for item in items:
    print(item)
    
#1
numbers = [3, 5, 7]
for i in numbers:
    print(i * 3)
    
#2
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#2
x = 8
y = 2

print(x * y)
print(x - y)

#3
age = 20
if age >= 18:
    print("adult")
  
#3    
score = 12
if score >= 10:
    print("OK")
    
#4
def greet(name):
    print("Hello",name)
greet("Alice")

#4
def uuu(nnn):
    print(nnn * 2)
uuu(5)"""

#5
def add(a,b):
    return a + b
result = add(3,4)
print(result)

#5
def nnn(kkk):
    return kkk - 5
result = nnn(10)
print(result)

#6
numbers = [1,4,7,10]
for n in numbers:
    if n >= 5:
        print(n)
        
#6
values = [3, 6, 8, 11, 14]
for i in values:
    if i % 2 == 0:
        print(i)