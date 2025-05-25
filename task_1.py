class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг обновлён до {self.rating}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating, flavors):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors

    def show_flavors(self):
        print(f"Сорта мороженого в {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Ice Cream", "мороженое", 4.5, ["Ванильное", "Шоколадное", "Клубничное"])
ice_cream_stand.show_flavors()