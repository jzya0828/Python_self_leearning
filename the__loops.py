#--------------------Loops-------
#----the while loops
count = 0
while count<10:
    print(count,'Programingis fun')
    count = count+1

##Controlling a loop with User Confirmation
x=1
continueLoop = 'Y'
while continueLoop=='Y':
    print('now x is : ',x)
    x=x+1
    continueLoop=input('Enter Y to contnue and N to quit '),

data=eval(input('enter an interger (the iinput ends '+'if it is 0:)'))
sum = 0
while data!=0:
    sum+=data
    data=eval(input('enter aninterger'+' if it is 0: '))

print('the sum is ',sum)

data= Sentine
sum = 0
while data!=0:
    sum+=data
    data=eval(input('enter aninterger'+' if it is 0: '))

#---------------for loops-------------
#statemet：for i in range(a,b,c)
#i>=a and a<b,every time a = a+c，if not exists c，a = a+1
for i in range(0,30):
   print(i)
print('\n')

for j in range(0,20,5):
    print(j)
print('\n')

for k in range(-1,16,2):
    print(k)

#------break and continue------
break
sum = 0
number = 0

while number < 20:
    number+=1
    sum += number
    if sum >= 100:
        break

print('the number is:  ',number)
print('the sum is:  ',sum)

sum = 0
number = 0
while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number

print('the sum is: ',sum)

#example：the smallest factor
__ways:1
n = eval(input('enter an inter >=2'))
factor = 2
while factor <= n:
    if n % factor == 0:
        break
    factor += 1
print("the smallest factor other than 1 for ",n,' is ',factor)

#__ways:2
n = eval(input('enter an interger >2 :'))
found = False
factor = 2
while factor <= n and not found:
    if n % factor == 0:
        found = True
    else:
        factor += 1
print("the smallest factor other than 1 for ",n,' is ',factor)

