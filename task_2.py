class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.working_time = working_time
        self.types = {
            'на палочке': [],
            'мягкое': [],
            'трубочка': []
        }

    def describe_stand(self):
        self.describe_restaurant()
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_time}")

    def display_flavors(self):
        print('Вкусы:')
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Добавлен вкус: {flavor}")
        else:
            print(f"Вкус уже есть: {flavor}")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            for ice_type in self.types:
                if flavor in self.types[ice_type]:
                    self.types[ice_type].remove(flavor)
            print(f"Вкус удалён: {flavor}")
        else:
            print(f"Вкус не найден: {flavor}")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Вкус {flavor} есть")
        else:
            print(f"Вкус {flavor} отсутствует")

    def add_flavor_to_type(self, flavor, ice_type):
        if ice_type in self.types:
            if flavor not in self.types[ice_type]:
                if flavor not in self.flavors:
                    self.flavors.append(flavor)
                    print(f"Добавлен вкус: {flavor}")
                self.types[ice_type].append(flavor)
                print(f"{flavor} добавлен в категорию '{ice_type}'")
            else:
                print(f"{flavor} уже есть в категории '{ice_type}'")
        else:
            print(f"Категория '{ice_type}' не существует")

    def show_types(self):
        print('Список вкусов по типам:')
        for ice_type, flavors in self.types.items():
            print(f"{ice_type.title()}:")
            if flavors:
                for flavor in flavors:
                    print(f" - {flavor}")
            else:
                print(" - Нет вкусов")

    def add_popsicle(self, flavor):
        self.add_flavor_to_type(flavor, "на палочке")

    def add_soft_serve(self, flavor):
        self.add_flavor_to_type(flavor, "мягкое")

    def add_tube_ice_cream(self, flavor):
        self.add_flavor_to_type(flavor, "трубочка")

iceCreamStand = IceCreamStand(
    "Ice Cream", "мороженое", ["Ванильное", "Шоколадное", "Клубничное"],
    "Центральная набережная", "10:00-22:00"
)

iceCreamStand.describe_stand()
print()
iceCreamStand.display_flavors()
iceCreamStand.open_restaurant()
print()
iceCreamStand.add_flavor("Фисташковое")
iceCreamStand.remove_flavor("Шоколадное")
iceCreamStand.check_flavor("Ванильное")
iceCreamStand.check_flavor("Мятное")
print()
iceCreamStand.add_popsicle("Клубничное")
iceCreamStand.add_soft_serve("Фисташковое")
iceCreamStand.add_tube_ice_cream("Мятное")
iceCreamStand.show_types()