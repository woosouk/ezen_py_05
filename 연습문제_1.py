#문제 1
daum = 89000
naver = 751000

my_daum = daum * 100
my_naver = naver * 20

all = my_daum + my_naver

print(all)

#모범답안
daum = 89000
naver = 751000
my = daum * 100 + naver * 20
print(my)

#문제 2
dch_stock = 0.05
nch_stock = 0.1
earn_minus = (my_daum*dch_stock)+(my_naver*nch_stock)

print(earn_minus)

#문제3
f = 50
c = (f-32)/1.8
print(c)

#문제4
s = "Daum Kakao"
a = s[:4]
b = s[5:]
print(s)
print(b+" "+a)

#모범답안
p = s.find(" ")
d = s[:p]
k = s[p+1:]
print(k + " " + d)