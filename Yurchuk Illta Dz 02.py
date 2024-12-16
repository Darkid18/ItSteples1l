# Life of Cat

# Cat class V1
class Cat:
    def __init__(self, name = "Odri", age = 3, hunger = 0, ill = "false", stamina = 100, love_to_owner = 100):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.ill = ill
        self.stamina = stamina
        self.love_to_owner = love_to_owner
        def hungry():
            if hunger >= 1:
                print("Odri wants something to eat!")

        def sleepy():
            if stamina <= 0:
                print("Odri sleeping right now!")

        def break_cup_or_vase():
            if stamina > 0 and love_to_owner < 30:
                print("Ooops Odri breaked a vase!")

        def play(playness):
            if playness > 0 and stamina > 40 and love_to_owner > 50:
                print("Odri plays with you")

