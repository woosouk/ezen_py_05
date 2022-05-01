# 대입 연산자 
from re import A


pi = 3.14
money = 12000
a = 3
b = a

print(b+money)

x = 100
y = 1
r = x > y
print(r)

print(10/3)
print(10//3)


#비교 연산과 논리 연산의 결합
a = 100 > 50
b = 20 > 10
print ( a and b)

c = 100 < 100 or 50 < 10
print(c)

# print( 100 > 1000 or 50 == 100)

# is 연산자
s1 = a is b
print(s1)

s2 = a is c
print(s2)

# is 연산과 == 연산의 차이
x = 100
y = 100.0

print(x == y)
print(x is y)

a = 101
b = y
x = ((a+b)*5//3)

# if b < a:
#     print(b)
# else:
#     print(a)



a = 1.3
b = 2.7
print(a+b)

