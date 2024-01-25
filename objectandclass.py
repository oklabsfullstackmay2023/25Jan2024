#1 class defination is one time process
class Student():
    #1. property/variable/state
    name=""
    age=""
    color=''
    gender=""
    #2. constructor/esp.function
    def __init__(self,gender,color,age,name):
        self.name=name
        self.age=age
        self.color=color
        self.gender=gender
        pass
    #3. function/behaviour/method
    # function definate
    def eat(self):
        return f"{self.name} is eating"
        pass
    def run(self):
        msg=f'{self.name} is running'
        return msg            
        pass
    def sleep(self):
        return f''' {self.name} is sleeping'''
        pass
    def learn(self):
        msg=f"{self.name} is learning"
        return msg
        pass
    pass

#2 create class external object is many time process
std1=Student(name="vishal",age=15,color="fair",gender='male')
print(f'{std1.name} {std1.age} {std1.color} {std1.gender}')
#2. calling()
msg1=std1.eat()
print(msg1)
msg2=std1.run()
print(msg2)
msg3=std1.sleep()
print(msg3)
print(std1.learn())