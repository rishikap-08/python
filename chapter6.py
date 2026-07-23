#conditional statment
if 12<=12:
    print("hello how are you")

"""you have to take the input of age and 
tell the person can vote or not"""

age = int(input("please tell your age:-"))
if age >= 18:
    print("hello brother you can vote")
else:
    print("sorry brother you cannot vote")   


rupees = int(input("give money-"))
if rupees == 10:
    print("i will buy a chocobar")
elif rupees == 50:
    print("i will have noodles")    
elif rupees == 100:
     print("i will go to mcd")
elif rupees == 500:
    print("5 star dhaba")
else:
    print("bhuki rahungi!")        

#practice
#question 1 
#accept two number and print the greater one
num1 = int(input("please give me first number:-"))
num2 = int(input("please give me second number:-"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
elif num1 == num2:
    print('both the numbers are equal')
   
   

#question 2
#accept gender from individual and greet them
print("Hello" < "hello")
print(ord('h'))
print(ord('H'))

gen = input("please tell your gender in (M or F ):-" )
if gen == "M" or gen == "m":
    print('hello! sir')
elif gen == "F" or gen == "f" :
    print('hello! mam')
else:
   print('i dont know your gender')

#question 3 
#accept an integer and check if it is even or odd
a = int(input("please tell your number :-"))
if a %2 == 0:
    print('even')
else:
    print('odd')


#question 4
#accept name and age- check if the user is valid voter(18+)
name = input('please tell your name:-')
age = int(input ('please tell your age:-'))
if age >= 18:
    print(f"hello {name} you are a valid voter")
else:
    print(f"hello {name} you can vote after {18 - age} years")

#question 5 
#accept a year and check if it is a leap year
year = int(input("please tell us the year:-"))
if year %100 == 0 and year %400 ==0:
    print(f"{year} is a leap year")
elif year % 100 != 0 and year %4 == 0:
    print("leap year")
else:
    print(f"sorry {year} is not a leap year")

#question 6 
# temprature ladder
#accept tem in celious and print a description. 
tem = int(input('please tell your temprature:-'))
if  -5 < tem < 5:
    print(' very cold')
elif 6 < tem  < 18:
    print('cold')
else:
    print('hot')
