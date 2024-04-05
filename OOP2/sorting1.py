class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

fruits_list = [Fruit("Apple", 10), Fruit("Banana", 5), Fruit("Cherry", 15)]

sorted_list = sorted(fruits_list, key=lambda x: x.price)
for fruit in sorted_list:
    print(fruit.name, fruit.price)