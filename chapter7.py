#loops
#types of loops: for , while
'''for loop'''
#range; (start,stop,step)
'''range(stop) 0 upto stop-1 
range(start,stop) start upto stop-1
range(start,stop,step) start jumping by step'''
# 10 - 100
#23 - 56
#0 - 45
range(10,101,1)
range(23,57,1)
range(46)

for i in range(10,101,1):
    print(i)

for a in range(23,57):
    print(a)

for i in range(46):
    print(i)

#practice print table of 5
for r in range(5,51,5):
    print(r)    

n = int(input("please tell your number:-"))
for i in range(n,n * 10 + 1,n):
    print(i)

a = "students"
for i in  a:
    print(i)

for i in range(len(a)):
    print(f"{i} : {a[i]}")  

#break, continue and else 

#continue (it will skip that no. and move ahead)
for i in range(1,11):
    if i == 4 or i == 5 or i == 6:
        continue
    print(i)

#break (it won't move ahead of that no.)
for i in range(1,7):
    if i == 3:
        break
    print(i)

#else 
for i in range(1,11):
    if i == 89:
        break
    print(i)
else:
    print('no break was encountered')    