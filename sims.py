import random

class Human:
    def __init__(self, name="Human",job = none, home = none, car = none):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job

        def get_home(self):
            pass

        def get_job(self):
            pass

        def get_car(self):
            pass

        def eat(self):
            pass

        def  work(self):
            pass

        def shopping(self):
            pass

        def chill(self):
            pass

        def clean_house(self):
            pass

        def to_repair(self):
            pass

brands_of_car = {
    "BMW": {"fuel":100, "strength": 100, "consumption": 6},
    "Lada": {"fuel":50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel":7, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

class Auto:
    def __init__(self, brand_list):
        self.brand_list = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]