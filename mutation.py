from random import randint as rnd
from random import shuffle

def swap(lst,x,y):
    lst[x],lst[y]=lst[y],lst[x]
    return lst

def mutation(population_list, n, m, r):
    choosen_ones = [i for i in range(m,m*2)]
    shuffle(choosen_ones)
    choosen_ones = choosen_ones[:int(m*r)]
    for i in choosen_ones:
        p1 =rnd(0,n-1)
        p2 =rnd(0,n-1)
        population_list[i]=swap(population_list[i],p1,p2)
    return population_list


def involved(population_list, n , m, r):
    choosen_ones = [i for i in range(m,m*2)]
    shuffle(choosen_ones)
    choosen_ones = choosen_ones[:int(m*r)]
    for i in choosen_ones:
        p1 =rnd(0,n-1)
        p2 =rnd(0,n-1)
        if p1>p2:
            p1,p2=p2,p1
        lst = population_list[i][:p1]+population_list[i][p2:n]
        segmen = population_list[i][p1:p2]
        place = rnd(0,len(lst)-1)
        for j in segmen:
            lst.insert(place,j)
            place+=1
        lst+=[None]
        population_list[i]=lst.copy()
    return population_list

