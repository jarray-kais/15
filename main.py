#1/all integers from 0 to 150
for i in range(151):
    print(i)
#2/multiple of 5
#methode 1
for j in range(5,1001,5):
    print(j)
#methode 2
for k in range(5,1001):
    if k % 5==0:
        print(k)
#3//compting the dojo way
for c in range (1,101):
    if c % 5==0:
        print("coding")
    if c % 10==0:
        print("coding dojo")
#4 sum of odd integer
for n in range(0,500001):
    if n % 2 ==0:
        continue
    print(n)
#5 décompteur de 4 
#methode 1
for d in range(2018,0,-4):
    print(d)
#methode 2 loop control
w= 2018
while w>0:
    w= w-4
    print(w)
#6 flexible counter
low = 2
high = 9
mult = 3

for i in range(low,high + 1):
    if i % mult == 0:
        print(i)
def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

