class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self, flavors):
        if flavors in self.flavors:
            print("Такое уже есть")
        else:
            self.flavors.append(flavors)
        print(f"В продаже: {self.flavors}")

newIceCreamStand = IceCreamStand("Мороженница", "Российская", "эскимо")

newIceCreamStand.show_flavors("Эскимо")
newIceCreamStand.show_flavors("на палочке")
