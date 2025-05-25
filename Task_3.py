import tkinter as tk
from tkinter import messagebox

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Ресторан: {self.restaurant_name}\nТип кухни: {self.cuisine_type}"

    def open_restaurant(self):
        return f"Ресторан {self.restaurant_name} открыт!"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def add_flavor(self, flavor):
        if flavor and flavor not in self.flavors:
            self.flavors.append(flavor)
        else:
            raise ValueError("Вкус уже есть ")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def get_flavors(self):
        return self.flavors

iceCreamStand = IceCreamStand("Ice Cream", 'десерты', ["Ванильное", "Шоколадное", "Клубничное"])

def run_gui():
    def update_listbox():
        listbox.delete(0, tk.END)
        for flavor in iceCreamStand.get_flavors():
            listbox.insert(tk.END, flavor)

    def add_flavor():
        flavor = entry.get().strip()
        if flavor:
            try:
                iceCreamStand.add_flavor(flavor)
                update_listbox()
                entry.delete(0, tk.END)
            except ValueError as e:
                messagebox.showwarning("Ошибка", str(e))
        else:
            messagebox.showwarning("Ошибка", "Введите вкус.")

    def remove_flavor():
        selected = listbox.curselection()
        if selected:
            flavor = listbox.get(selected)
            iceCreamStand.remove_flavor(flavor)
            update_listbox()
        else:
            messagebox.showwarning("Ошибка", "Выберите вкус.")

    root = tk.Tk()
    root.title("Мороженое")

    info_label = tk.Label(root, text=iceCreamStand.describe_restaurant(), font=("Courier New", 14))
    info_label.pack(pady=10)

    open_label = tk.Label(root, text=iceCreamStand.open_restaurant(), fg= "purple", font=("Courier New", 10, "bold"))
    open_label.pack(pady=5)

    listbox = tk.Listbox(root, height=6, width=40)
    listbox.pack(pady=5)
    update_listbox()

    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    add_button = tk.Button(root, text="Добавить вкус", command=add_flavor)
    add_button.pack(pady=2)

    remove_button = tk.Button(root, text="Удалить выбранный вкус", command=remove_flavor)
    remove_button.pack(pady=2)

    root.mainloop()

run_gui()