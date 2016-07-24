"""
@author: David Lei
@since: 26/06/2016
@modified:

Algorithms for All-Pairs Shortest Path
- Run Dijkstra |V| times for each source node   O(|V|3) with arrays
- DP approach = Floyd Warshall
    - rep graph in adjacency matrix

5 6
1 3 5
4 5 0
2 1 3
3 2 1
4 3 4
4 2 2

output: 1000100
"""

class BiDiRoad:
    def __init__(self, c1, c2, cost):
        self.city1 = c1
        self.city2 = c2
        self.cost = cost
        # 2 ^ C
    def check_cities(self, other_c_1, other_c_2):
        if int(self.city1) == int(other_c_1):
            if int(self.city2) == int(other_c_2):
                return True
            else:
                return False
        elif int(self.city1) == int(other_c_2):
            if int(self.city2) == int(other_c_1):
                return
            else:
                return False
        else:
            return False

    def get_cost(self):
        return 2**self.cost

class AdjacencyMatrix:
    def __init__(self, no_vert):
        self.size = no_vert
        self.array = [[0]*no_vert for _ in range(no_vert)]

    def get_rep(self):
        return self.array
    def get_size(self):
        return str(self.size) + 'x' + str(self.size)
max_edge_cost = 0
#Edges = []



# N = no cities
# M = no bidir roads
N, M = input().strip().split(' ')
N = int(N)
M = int(M)
#A = AdjacencyMatrix(N)
D = AdjacencyMatrix(N)  # matrix to hold costs
# A, B, C = city A to City B cost = 2^C
for i in range(M):
    road = input().strip().split(' ')
    a_city = int(road[0])-1
    b_city = int(road[1])-1
    cost_powern = int(road[2])
    # make edge
    a_road = BiDiRoad(a_city, b_city, cost_powern)
    #Edges.append(a_road)
    max_edge_cost += 2**cost_powern

    D.get_rep()[a_city][b_city] += 2**cost_powern
    D.get_rep()[b_city][a_city] += 2**cost_powern

# floyd warshall implementation
for k in range(0, N):
    for o in range(0, N):
        for j in range(0, N):
            if D.get_rep()[o][j] == 0 and o != j:
               D.get_rep()[o][j] = max_edge_cost
            if D.get_rep()[k][o] != 0 and D.get_rep()[k][j] != 0:
                if D.get_rep()[k][o] + D.get_rep()[k][j] < D.get_rep()[o][j]:
                    D.get_rep()[o][j] = D.get_rep()[o][k] + D.get_rep()[k][j]
                    #print(D.get_rep()[o][j])
            else:
                pass
cur_city = 1
sum_min_roads = 0
for n in range(N):
    for c in range(0, N-cur_city):
        shortest = D.get_rep()[n][c+cur_city]
        #print( str(n+1) + ", " + str(c+cur_city+1) + ': ' + str(shortest))
        sum_min_roads += shortest
    cur_city += 1

b = bin(sum_min_roads)
print(b[2:])
