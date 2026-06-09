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

    def __init__(self, restaurant_name, cuisine_type, flavors, location, time_work):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        '''1)'''
        self.location = location
        self.time_work = time_work
        self.types_flavors = {
            "Пломбир": [],
            "На палочке": [],
            "Рожок": [],
        }
        
    def show_flavors(self, flavors):
        if flavors in self.flavors:
            print("Такое мороженное уже есть")
        else:
            self.flavors.append(flavors)
        print(f"Мороженное в продаже: {self.flavors}")

    def delete_flavors(self):
        icecream_delete = input("Какое мороженное вы хотите удалить")
        if icecream_delete in self.flavors:
            self.flavors.remove(icecream_delete)
        else:
            print("Такого мороженного и так нет")


    def have_flavors(self, flavors, name):
        name = input("Какое мороженное будете: ")
        flavors = input("Какой тип: ")
        if name in self.types_flavors[flavors]:
            print("Такое мороженное есть", name)
        else:
            self.types_flavors[flavors].append(name)
            print(self.types_flavors)

new = IceCreamStand("Мороженница", "Азиатская", "Пломбир", "Питер", "10:00-20:00")

new.have_flavors("Рожок", "Теремок")
