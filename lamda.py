def adder(number):
    return lambda x: x + number


add_5 = adder(5)
add_10 = adder(10)

print(add_5(1))
print(add_10(1))
