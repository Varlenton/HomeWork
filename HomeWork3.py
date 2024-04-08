class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building = Building(10, "house")
his_building = Building(10, "house")
print(my_building == his_building)
