#-------functions----

example1:write a function to exchange x1,x2
def exchange(x1,x2):
    print('x1 is ',x1,' x2 is ',x2)
    if x1 != x2:
        x1,x2=x2,x1
    print('after exchange x1 is ',x1,' x2 is ',x2)

def main():
    exchange(2,7)
    exchange('s','c')

main()#called main() method

def getGrade(score):
    if score >= 90:
        return 'a'
    else:
        return 'b'

def main():
    score = eval(input('input score'))
    print('the grade is ',getGrade(score))
main()

def printGrade(score):
    if score < 0 or score > 100:
        print('invalid sore')
        return#return None

    if score > 90:
        print('a')
    else:
        print('b')


score = 98
print('you score is',printGrade(score))

#positional and keyword arguements
def enroll(name,score,adress='beijing'):
    print('name',name)
    print('score',score)
    print('adress',adress)

enroll('sxl',90)
enroll('sxl1',78,adress='xian')
#the positional arguement cannot after any keywords arguements

#Default Arguments
def printArea(width = 1,height = 2):
    area= width * height
    print('width:',width,'\theight',height,'\tarea:',area)

printArea()
printArea(4,2.5)
printArea(height = 5,width = 3)
printArea(width = 1.2)
printArea(height = 6.2)

#---Returning Multiple Values

def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

n1,n2 = sort(3,2)
print('n1 is ',n1)
print('n2 is ',n2)

def f(x,y):
    return x+y,x-y,x*y,x/y

t1,t2,t3,t4=f(9,5)
print(t1,t2,t3,t4)

