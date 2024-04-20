import re

# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.rain|train.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

y = re.findall("ai", txt)
print(y)

z = re.sub("rain", "plane", txt)
print(z)
