#--------------------------selection--------------------------

radius = eval(input('please radius'))#if else selection
if radius <0:
    print("incorrect input")
else:
    print('radius is \n',+radius)

radius =  1#boolean types ,values,...
print(radius>0)

light = True
print(light)

print(int(True))
print(int(False))


print(bool(0))#not 0 use print(bool())is True
print(bool(1))
print(bool(4))
print(bool(-1))

import random
number1 = random.randint(0,9)
number2 = random.randint(0,9)
answer = eval(input('what is '+str(number1)+'+'+str(number2)+'?'))
print(number1,'+',number2,'+','=',answer,'is',number1+number2==answer)
import random
print(random.random())
print(random.randint(0,1))
print(random.randint(0,10))
print(random.randrange(0,11))#randint(a,b+1)is
# equivalent to randrange(a,b)

#----------------if statement------
radius = eval(input("please input radius"))#if statement
if radius>0:
    print('area is ',radius*radius)
else:
    print('your input is incorrect')


SS = eval(input("plesae input a int: "))
if SS>90:
    print('A\n')
else:
    if SS>80:
        print("b\n")
    else:
        if SS>70:
            print('c\n')

if SS>90: #when SS stisfied with 'if SS>90 'then end，
    # do not match next statement

    print('a\n')
elif SS>80:
    print('b\n')
elif SS>70:
    print('c\n')


enumber = 10
if enumber%2==0:  #this if-else statement is
    #  equailen to even = number %2==0
    even=True
else:
    even==False
print(even)

import random

number = random.randint(0,99)
number2 = random.randint(10,20)
if number>20 and number2<15:
    print('random is',number,"\t",number2)
else:
    print('number and number2 is ',number,'\t',number2)

print('hello')

#------------------logical operators---------------
number=eval(input('please input'))
if number %2==0and number%3==0:#and
    print(number,'is divisible by 2 and3')
if number %2==0 or number % 3==0:#or
    print(number,'is divisile by 2or 3')
if (number % 2 ==0 or number % 3==0)and \
       not (number % 2 == 0 and number % 3 == 0 ):#not statement ,is equa with
    #  (number % 2 != 0 or number % 3 != 0 )
    print(number,'is disvisable by 2 or 3 ,but not both')

#------------------Condition Expressions-------------
the syntax is:expression_1 if booean-expression else expression_2
x=eval(input('input x'))
if x>0:
    y=1
else:
    y=-1
print(y)
the up statement is equaly to the blow statement
x=eval(input('input x'))
# y = 1 if x>0 else -1
# print(y)
number = eval(input('input number'))
print('number is even' if number % 2==0 else 'number is odd')


