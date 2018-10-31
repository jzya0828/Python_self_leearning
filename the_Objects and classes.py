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

