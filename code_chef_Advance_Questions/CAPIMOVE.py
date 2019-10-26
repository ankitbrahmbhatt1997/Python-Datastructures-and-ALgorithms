from sys import stdin
from heapq import heappop,heappush
from collections import defaultdict




t = int(stdin.readline())
for _ in range(t):
    N = int(stdin.readline())
    planets_population = list(map(int,stdin.readline().strip().split(" ")))
    planets=[]
    for i in range(1,N+1):
        planets.append((planets_population[i-1],i))

    
    planets.sort()
    infected_planets_dict = defaultdict(list)
    infected_planets= []
   
    for i in range(N-1):
        infected_planets.append(tuple(map(int,stdin.readline().strip().split(" "))))
    for v,u in infected_planets:
        if v in infected_planets_dict:
            ne = infected_planets_dict[v]
            ne.add(u)
            infected_planets_dict[v] = ne
        else:
            infected_planets_dict[v] = set([v,u])

        if u in infected_planets_dict:
            ne = infected_planets_dict[u]
            ne.add(v)
            infected_planets_dict[u] = ne
        else:
            infected_planets_dict[u] = set([u,v])
    
    ans=[]
    for v in range(1,N+1):
        connected_planets = infected_planets_dict[v]

        k = len(planets)
        while k > 0 :
            current_planet = planets[k-1]
            if  current_planet[1] not in connected_planets:
                ans.append(current_planet[1])
                break
            k-=1


    for i in ans:
        print(i,end=" ")
        

        