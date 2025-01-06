# lesson 1 was about gits and more

# Lesson 2
# class Student:
#
#     def __init__(self, name = None, height = 160):
#         self.name = name
#         self.height = height
#
#     height = 150
#
#     def printer(self):
#         self.name = 10
#         print(self.height)
#
#     def __del__(self):
#         print('ByBy')
#
#     def __bool__(self):
#         return self.name == None
#
#     def __len__(self):
#         return self.height
#
#
#
#
# Max = Student()
# Max.printer()
#
# print(Max.__len__())
# print(Max.__bool__())


# I wrote the task but pressed some shity button so it got destroyed (I used cntrl z, but it didn't help)







# Lesson 3 Sims
# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, *args):
#         for passenger in args:
#             self.passengers.append(passenger)
#
#     def print_passengers_name(self):
#         if self.passengers != []:
#             print(f"Name of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#
#         else:
#             print(f"There are no passengers in {self.brand}")
#
# nick = Human("Nick")
# kate = Human("Kate")
# Kira = Human("Kira")
# Hakita = Human("Hakita")
#
# car = Auto("Mercedes")
#
# car.add_passenger(nick, kate, kira, Hakita)
#
# car.print_passengers_name()









# lesson 4
#
# class Human:
#     height = 170

#     def __init__(self):
#         self.height = 150

# class Student(Human):
#     def __init__(self):
#         print(self.height)

#         super().__init__()
#         print(self.height)
#         print(super().height)
# class Worker(Human):
#     pass

# nick = Student()
# ann = Worker()

# print(nick.height)
# print(ann.height)
#
#
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * 2
#
# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#
# circle = Circle('red', 5)
# print("Circle area:", circle.area())
# rectangle = Rectangle('blue', 4, 6)
# print("Rectangle area:", rectangle.area())
#
#
#
#
# class Computer:
#     def calculate(self):
#         print("Calculating...")
#
# class Display:
#     def display(self):
#         print("Displaying...")
#
# class SmartPhone(Computer, Display):
#     pass
#
# iphone = SmartPhone()
#
# iphone.display()
# iphone.calculate()
#
#
#
#
#
# class AudioPlayer:
#     def play_audio(self):
#         print("Playing audio...")
#
# class VideoPlayer:
#     def play_video(self):
#         print("Playing video...")
#
# class MultiMediaPlayer(VideoPlayer, AudioPlayer):
#     def play(self):
#         print("Playing media...")
#
# player = MultiMediaPlayer()
# player.play_audio()
# player.play_video()
# player.play()




# Lesson 5











