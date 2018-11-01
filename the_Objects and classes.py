#------Objects AND Classes--
#template
class TV:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_data(self):
        print(self.name,self.score)
    def get_data(self):
        return self.name,self.score

bar = TV('SXL',20)
print(bar.name)
bar.print_data()
print(bar.get_data())

class Count:
    def __init__(self,count=0):
        self.count = count

def increment(c,times):
    c.count += 1
    times += 1

def main():
    c = Count()
    times = 0
    for i in range(100):
        increment(c,times)

    print('count is ',c.count)
    print('times i s ',times)

main()

#-------Hiding Data Fields---
#--preve clien directly use varia from class object

class Circle:
    def __init__(self,radius = 1,wtf = 0):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return self.__radius * self.__radius

    def setWtf(self,wtf):
        self.__wtf = wtf

    def getWtf(self):
         return self.__wtf
c = Circle(5,20)
print(c.getArea(),'  ',c.getRadius())
##print(c.radius):directly use c.radius is wrong ,only by use getRadius
c.setWtf(15)
print(c.getWtf())


