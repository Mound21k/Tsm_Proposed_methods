from random import randint as rnd
from random import shuffle

def _shuffle(lst):
    shuffle(lst)
    return lst

def init_population_r(n, m):
    population_list = [_shuffle([i for i in range(n)])+[None] for i in range(m)]
    return population_list