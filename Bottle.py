class Bottle:
    color = 'green'
    volume = 1


list_of_bottles = []

bottle1 = Bottle()
bottle1.color = 'red'
bottle1.volume = 0.7
list_of_bottles.append(bottle1)

bottle2 = Bottle()
bottle2.color = 'white'
bottle2.volume = 0.3
list_of_bottles.append(bottle2)

bottle3 = Bottle()
bottle3.color = 'black'
bottle3.volume = 1.0
list_of_bottles.append(bottle3)

for bottle in list_of_bottles:
    print(f"Color: {bottle.color} Volume: {bottle.volume}")



