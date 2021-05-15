#Zadanie 1 2.7
class Zadanie:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    def show_(self):
        return (f'All my tasks: Point1 {self.point1}, Point2 {self.point2}, Point3 {self.point3}')
c = Zadanie(30, 40, 50)

print(c.show_())

#Zadanie 2 2.7
class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree') 

exmpl1 = Monkey()
exmpl2 = Monkey()

print(exmpl1.max_age)
exmpl1.climb()
print(exmpl1.loves_bananas)
exmpl2.climb()

#Zadanie 3 2.7

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self):
        self.calculate_age = int(input(''))
        print(f' Через {self.calculate_age} лет John исполнится {self.calculate_age + self.age}')

p = Person('John', 23, 'male')

print(p.name)
print(p.age)
print(p.gender)
p.calculate_age()


