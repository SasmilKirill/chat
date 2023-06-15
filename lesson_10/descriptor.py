
class NonNegative:


    def __init__(self, my_attr):

        self.my_attr = my_attr

    def __get__(self, instance, owner):

        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):

        if value < 0:
            raise ValueError("Не может быть отрицательным")

        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]


class Worker:


    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate


OBJ = Worker('Антон', 'Макеев', 12, 160)
print(OBJ.total_profit())

OBJ.hours = 10
OBJ.rate = 100
print(OBJ.__dict__)
print(OBJ.total_profit())
del OBJ.rate
print(OBJ.__dict__)