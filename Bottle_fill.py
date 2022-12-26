class Bottle:
    def __init__(self, color, contains=0):
        self.color = color
        self.contains = contains

    def fill(self, volume):
        self.contains += volume


bottle1 = Bottle('red')
bottle2 = Bottle('blue')

list_of_bottles = [bottle1, bottle2]

print("Before filling volumes: ")
for bottle in list_of_bottles:
    print(f"Color: {bottle.color} contains: {bottle.contains}")

print("\nFilling red with 100 ml, blue - with 500 ml")
bottle1.fill(100)
bottle2.fill(500)
for bottle in list_of_bottles:
    print(f"Color: {bottle.color} contains: {bottle.contains}")