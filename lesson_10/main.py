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
print(OBJ.total_profit())

