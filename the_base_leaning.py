print('AAA',end='')
print('BBB',end='  ')
print('CCC','**')

import math
radius = 3
print('the area is',radius*radius*math.pi,end=' ')
print('and the perimeter is',2*radius,end=' ')

x = 3.4
s = str(x)#Convert a folat(interger) to string
print(s,end='\n')

#--------------string operrator----------------
string concatenation(zi fu chuan pin jie)
message='sxl '+'is'+' a good boy '
print(message)
message+=message
print(message)
ss=3.4
message=message+str(ss)
print(message)

s1=input('enter FIRST string : ')
s2=input('enter SECOND string : ')
s3=input('enter THIRD string : ')
print('s1 is'+s1)
print('s2 is'+s2)
print('s3 is'+s3,end='\n')


ord:take uppercase/lowercase to  ASCII
chr:take ASCII to uppercase/lowercase
xx = 'a'
print(ord(xx))
print(chr(98))

id() :get **'s id  type():get **'s type
n=3
print(id(n))
print(type(n))

#str.lower() or upper()  :to set uppercase to lowercase or on the contrary
s = 'welcome'
print(s.upper())
a = 'WELCOME'
print(a.lower())

strip()method is remove the whitespace form string head and end
s = '\twel co me  \n'
print(s.strip())
#------------------------------------------------------------



#------formatting numbers and string-----------
amount = 12618.98
intersestRate = 0.0013
interest = amount*intersestRate
print('interest is ',interest)
print('interest is ',round(interest,2))
print('interest is ',format(interest,'.2f'))

print(format(57.467657,'10.2f'))#float
print(format(12345678.923,'10.2f'))
print(format(57.4,'10.2f'))
print(format(57,'10.2f'))

print(format(57.467657,'10.2e'))#scientific notation
print(format(0.0033923,'10.2e'))
print(format(57.4,'10.2e'))
print(format(57,'10.2e'))


print(format(0.53457,'10.2%'))#percentage
print(format(0.0033923,'10.2%'))
print(format(7.4,'10.2%'))
print(format(57,'10.2%'))


print(format(57.467657,'10.2f'))#mo ren you duiqi
print(format(57.467657,'<10.2f'))#< zuo dui qi

print(format(59832,'10d')) #d decimal  x hexadecimal
print(format(59832,'<10d'))
print(format(59832,'10x'))
print(format(59832,'<10x'))

print(format('welcome to python','20s'))#string mo ren zuo duiqi
print(format('welcome','<20s'))
print(format('welcome','>20s'))
#-------------------------------------------------------------

