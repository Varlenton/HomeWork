class Vehicl:
    Vehicle_type = 'None'


class Car:
    price = 1000000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return print(horse_powers)


class Nissan(Vehicl, Car):
    Vehicle_type = "Vehicl"
    price = 1500000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return print(horse_powers)


nissan = Nissan()

print(nissan.Vehicle_type)
print(nissan.price)
