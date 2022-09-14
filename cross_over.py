from random import randint as rnd

def _PMX1(s, t, r):
    lst = s.copy()
    for i in range(r):
        key = t[i]
        ind = lst.index(key)
        lst[i],lst[ind]=lst[ind],lst[i]
    return lst


def PMX1(population_list, n, m):
    for i in range(0,m,2):
        r = rnd(0,n-1)
        child1 = _PMX1(population_list[i], population_list[i+1], r)
        child2 = _PMX1(population_list[i+1], population_list[i], r)
        population_list.append(child1)
        population_list.append(child2)
    return population_list

def _rand(x,y):
    r1 = rnd(x,y-1)
    r2 = rnd(x,y-1)
    if r1>r2:
        r1,r2 = r2,r1
    elif r1==r2:
        if r2==y-1:
            r1-=1
        elif r1==x:
            r2+=1
        else:
            r2+=1
    return r1,r2

def PMX2(popualtion_list, n , m):
    for i in range(0,m,2):
        r1, r2 = _rand(0,n-1)
        seg1=popualtion_list[i][r1:r2]
        seg2=popualtion_list[i+1][r1:r2]
        unique_1 = [i for i in seg2 if i not in seg1]
        unique_map_1 = [seg1[seg2.index(i)] for i in unique_1]
        child1 = [None]*r1 + seg1 + [None]*(n-r2)
        for ind,item in enumerate(unique_1):
            j = unique_map_1[ind]
            place = popualtion_list[i+1].index(j) 
            if place not in range(r1,r2):
                child1[place]=item
            else:
                while j in seg2:
                    _ = seg2.index(j)
                    j = seg1[_]
                else:
                    place = popualtion_list[i+1].index(j)
                    child1[place]=item
        for _ in range(len(child1)):
            if child1[_]==None:
                child1[_]=popualtion_list[i+1][_]
        #print(child1)
        unique_1 = [i for i in seg1 if i not in seg2]
        unique_map_1 = [seg2[seg1.index(i)] for i in unique_1]
        child2 = [None]*r1 + seg2 + [None]*(n-r2)
        for ind,item in enumerate(unique_1):
            j = unique_map_1[ind]
            place = popualtion_list[i].index(j) 
            if place not in range(r1,r2):
                child2[place]=item
            else:
                while j in seg1:
                    _ = seg1.index(j)
                    j = seg2[_]
                else:
                    place = popualtion_list[i].index(j)
                    child2[place]=item
        for _ in range(len(child2)):
            if child2[_]==None:
                child2[_]=popualtion_list[i][_]        
        #print(child2)
        popualtion_list.append(child1+[None])
        popualtion_list.append(child2+[None])
    return popualtion_list
