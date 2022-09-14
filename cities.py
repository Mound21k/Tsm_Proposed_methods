from random import randint as rnd


def city_randomizer(n, w, h):
    padding = 20
    locations = []
    for i in range(n):
        x=rnd(padding,w-padding)
        y=rnd(padding,h-padding)
        locations.append((x,y))
    return locations
