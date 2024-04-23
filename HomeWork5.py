class Car:
    price = 1000000

    def horse_powers(self):
        horse_powers = 150
        return horse_powers


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        horse_powers = 200
        return horse_powers


class Kia(Car):
    price = 2000000

    def horse_powers(self):
        horse_powers = 250
        return horse_powers


car = Car()
nissan = Nissan()
kia = Kia()

print(car.price)
print(car.horse_powers())
print(nissan.price)
print(nissan.horse_powers())
print(kia.price)
print(kia.horse_powers())
