class Counter:
    # 기본생성자
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


a = Counter()
a.increment()
print("카운터의 값=", a.count)


class Counter:
    # 매개변수 생성자
    def __init__(self, initValue=0):
        self.count = initValue

    def increment(self):
        self.count += 1


a = Counter(0)  # 계수기를 0으로 초기화한다.
b = Counter(100)  # 계수기를 100으로 초기화한다.
a.increment()
b.increment()
print(a.count)
print(b.count)

import math


# Circle 클래스를 정의한다.
class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    # Circle 객체를 생성한다.


c = Circle(10)
print("원의 면적", c.getArea())
print("원의 면적", c.getPerimeter())


class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60


myCar = Car(0, "blue", "E-class")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)

myCar.drive()
print("자동차의 속도는", myCar.speed)


class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel


# 텔레비전을 클래스로 정의한다. 
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)


# 전달받은 텔레비전의 음량을 줄인다.
def setSilentMode(t):
    t.volume = 2


# setSilentMode()을 호출하여서 객체의 내용이 변경되는지를 확인한다.
myTV = Television(11, 10, True);
setSilentMode(myTV)
myTV.show()


# 텔레비전을 클래스로 정의한다. 
class Television:
    serialNumber = 0  # 이것이 클래스 변수이다.

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1  # 클래스 변수를 하나 증가한다.
        # 클래스 변수의 값을 객체의 시리얼 번호로 한다.
        self.number = Television.serialNumber

    def show(self):
        print(self.channel, self.volume, self.on, self.number)


myTV = Television(11, 10, True);
myTV.show()


class Student:
    def __init__(self, name=None, age=0):
        self.__name = name  # __가 변수 앞에 붙으면 외부에서 변경 금지 (Private)
        self.__age = age  # __가 변수 앞에 붙으면 외부에서 변경 금지 (Private)


obj = Student()
print(obj.__age)  # 오류 발생!


class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name


obj = Student("Hong", 20)
obj.getName()

# csv 파일 읽고 for~each문으로 각 행의 4번째 항목 비교하여 가장 작은값 출력
import csv

f = open("chap10/weather.csv")  # CSV 파일을 열어서 f에 저장한다.
data = csv.reader(f)
header = next(data)
temp = 1000
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])
print('가장 추웠던 날은', temp, '입니다')
f.close()
