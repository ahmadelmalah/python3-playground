class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(x):
        return x.price

fruits_list = [Fruit("Apple", 10), Fruit("Banana", 5), Fruit("Cherry", 15)]

sorted_list = sorted(fruits_list, key=Fruit.sort_priority)
for fruit in sorted_list:
    print(fruit.name, fruit.price)

print(fruits_list[0].sort_priority())