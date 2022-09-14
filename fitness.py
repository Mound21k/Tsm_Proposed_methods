from math import sqrt

def transformer(cities, path):
    for i in range(len(path)):
        path[i]=cities[path[i]]
    return path
def distance(path):
    dis = 0
    for i in range(len(path)-1):
        dis+=sqrt(((path[i][0]-path[i+1][0])**2) + ((path[i][1]-path[i+1][1])**2))
    return dis
def fitness(population_list, cities_locations, n):
    length = len(population_list)
    for i in range(length):
        if population_list[i][n]==None:
            path = transformer(cities_locations, population_list[i][:n]+[population_list[i][0]])
            population_list[i][n]=distance(path)
    return population_list