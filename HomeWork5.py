class Car:
    price = 1000000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return print(horse_powers)


class Nissan(Car):
    price = 1500000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return print(horse_powers)


class Kia(Car):
    price = 2000000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return print(horse_powers)


car = Car()
nissan = Nissan()
kia = Kia()

print(car.price)
car.horse_powers(100)
print(nissan.price)
nissan.horse_powers(150)
print(kia.price)
kia.horse_powers(200)
