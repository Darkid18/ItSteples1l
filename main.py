#
# def print_hi(name):
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# if __name__ == '__main__':
#     print_hi('PyCharm')\




# Lesson 3 Sims
class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_name(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"There are no passengers in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
Kira = Human("Kira")
Hakita = Human("Hakita")

car = Auto("Mercedes")

car.add_passenger(nick, kate, kira, Hakita)


car.print_passengers_name()