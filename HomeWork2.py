class House:
    def __init__(self):
        self.name = 'House'
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, Floors):
        print(f'This house is {Floors} floors')


my_house = House()
my_house.setNewNumberOfFloors(10)
