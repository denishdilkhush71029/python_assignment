class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, percent):
        discount_amount = (self.price * percent) / 100
        self.price -= discount_amount
        print(f"Final Price after {percent}% discount: {self.price}")

# Usage
my_car = Car("Tata", "Nexon", 1000000)
my_car.apply_discount(10)


