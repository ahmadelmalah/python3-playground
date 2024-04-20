import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

# Create a datetime object from a specific date
y = datetime.datetime(2020, 5, 17)
print(y)
print(y.strftime("%B"))
