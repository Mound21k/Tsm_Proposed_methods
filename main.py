from params import *
from cities import city_randomizer
from init_population import init_population_r
from cross_over import PMX1, PMX2
from mutation import mutation, involved
from fitness import fitness, transformer
import matplotlib.pyplot as plt
import numpy as np
from visualization import city_drawer, path_drawer

img = np.full((WIDTH,HEIGHT,3),255,np.uint8)
cities_locations = city_randomizer(N, WIDTH, HEIGHT)
# cities_locations =[(335, 382), (444, 293), (52, 335), (363, 347), (451, 323), (209, 141), (239, 370), (99, 97), (428, 78), (321, 129), (334, 162), (397, 210), (311, 358), (353, 140), (322, 147), (281, 307), (248, 212), 
# (87, 293), (124, 139), (396, 83)]
#print(cities_locations)
current_population = init_population_r(N, MAX_POPULATION)
for i in range(1,EPOCH+1):
    current_population = PMX2(current_population, N, MAX_POPULATION)
    current_population = involved(current_population, N, MAX_POPULATION, MUTATION_RATE)
    current_population = fitness(current_population, cities_locations, N)
    current_population = sorted(current_population, key=lambda x:x[N])
    current_population = current_population[:MAX_POPULATION]
else:
    img = city_drawer(img, cities_locations, (255,0,0))
    current_path = transformer(cities_locations, current_population[0][:N])
    current_path.append(tuple(current_path[0]))
    img = path_drawer(img, current_path, (0,0,255))
    plt.imshow(img)
    plt.show()
    print("Best Found Solution:",current_population[0])
