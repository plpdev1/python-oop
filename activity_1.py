class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    def turn_on(self):
        print(f"{self.model} is now ON!")

    def call(self, phone_number):
        print(f"Calling {phone_number} from {self.model}...")

    def show_battery(self):
        print(f"Battery capacity: {self.battery_capacity}mAh")

# object of Smartphone
my_phone = Smartphone("Samsung", "Galaxy S21", 4000)

# Using methods
my_phone.turn_on()
my_phone.call("+254 746 789 840")
my_phone.show_battery()
