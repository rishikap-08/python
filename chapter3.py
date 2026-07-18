#unicode
a = 'g'
print(ord(a))

#indexing
a = "college"
print(a[0])
#-indexing last letter will be -1 and second last letter will be  -2
print(a[-2])
print(a[6],a[-1])

#string slicing
print(a[3:6:1])
print(a[0:7:2])
print(a[::2])#if i have not used any value for start and end then it will take default value as 0 and length of string respectively

#practice
b = "hello how are you" 
#how
print(b[6:10:1])
#you
print(b[14:18:1])
#hello
print(b[0:6:1])

#type conversion
a = "22"
b = int(a)
print(a)
print(b)
print(type(a))
print(type(b))  
#you can convert string if it holds valid integers
#you can convert float values to interger
a = 12
a = float(a)
print(type(a))
print(a)

a = 12
b = 12.5 
c = 12 +6j
d = True 
a = str(a)
b = str(b)
c = str(c)
d = str(d)
print(type(a))

a = 34 
b = 0 
c = 56.7
d = 0.0
e = ""
f = 'hello'
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

a = 12 
print(a/2) #float 
print(a//2) #int

