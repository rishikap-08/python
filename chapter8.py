#for loop questions

#question 1
#print 'hello world' n times:

n = int(input("tell your number:-"))
for i in range(n):
    print('hello world')

#question 2
# print natural number from 1 to n: 

n = int(input("tell your number:-"))
for i in range(1,n+1):
    print(i) 

#question 3
# reverse for loop- print n down to 1.

n = int(input('tell your number:-'))
for i in range(n,0,-1):
    print(i)

#question 4
# print the multiplication table of a number 

n = int(input("which table you want:-"))
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")

#question 5
# sum of first n natural numbers

s = 0
n = int(input("till where you want your sum:-"))
for i in range(1,n+1):
    s = s + i
    print(s)

#question 6
#factorial of a number

n = int(input("till where you want the factorial:-"))
f = 1
for i in range(1,n+1):
    f = f * i
    print(f)

#question 7 
#print sum of all even and odd number in a range seperatly

n = int(input('tell your number:-'))
oddsum = 0
evensum = 0
for i in range(1,n+1):
    if i%2 == 0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i 
print(f"your evensum is {evensum} and oddsum is {oddsum}")        

#question 8
#print all factor of a number

n = int(input("tell your number :-"))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

#question 9
#check if a number is perfect (sum of factors = the number itself)

n = int(input("tell your number :-"))
s = 0
for i in range(1,n):
    if n % i == 0:
        s = s + i 
if s == n:
    print("perfect number")
else:
    print("not a perfect number")    

#question 10 
# check if the number is prime

n = int(input("tell your number :-"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1 
if count == 2:
    print("prime number")
else:
    print("composite number")       

#question 11
#reverse a string without using built in functions.

#with funtions
a = "python"
print(a[::-1])

#without functions
a = 'python'
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

print(rev)    

#question 12
#check if a string is palindrome

a = input("tell your string:-")
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

if rev == a:
    print("yes palindrome") 
else:
    print("no not a palindrime")

#question 13 
#count letters,digits,and special symbols in a string.

a = "P@#yn26at^&i5ve"

char = 0
spchar = 0 
digits = 0

for i in a:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        char = char + 1
    else: 
        spchar = spchar + 1 

print(f"characters -  {char} , special characters - {spchar} , digits - {digits}")           

"""different method"""

a = "P@#yn26at^&i5ve"

char = 0
spchar = 0
digits = 0
for i in a:
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        char += 1
    elif ord(i) >= 48 and ord(i) <= 90: 
        digits += 1
    else:
        spchar += 1    

print(f"characters - {char} , special characters - {spchar} , digits - {digits}")