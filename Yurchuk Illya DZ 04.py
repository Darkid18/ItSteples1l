class Fight_epoch_machine:
    def __init__(self):
        self.height = 140
        self.armor = 50

class civilizated_epoch_machine(Fight_epoch_machine):
    def __init__(self):
        super().__init__()

        # print(self.height)
        # print(self.armor)
V1 = Fight_epoch_machine()
V2 = civilizated_epoch_machine()
print(V1.height)
print(V1.armor)

print(V2.height)
print(V2.armor)