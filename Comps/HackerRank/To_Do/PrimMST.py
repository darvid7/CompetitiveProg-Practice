"""
@author: David Lei
@since: 25/07/2016
@modified:

use
- an adjacency matrix to keep track of edges and costs
- a priority queue to select edge with min weight
- array to keep track of visited nodes

Priority Queue
The heapq implements a min-heap sort algorithm suitable for use with Python's lists. The interesting property
of a heap is that its smallest element is always the root

import heapq

heap = []
heapq.heappush(heap, (1, 'one'))
heapq.heappush(heap, (10, 'ten'))
heapq.heappush(heap, (5,'five'))

heapq.heappop(heap)

# the smallest
print heap[0]
"""

import heapq

# read in N and M values
no_vertexes, no_edges = [int(d) for d in input().split(' ')]

# construct adjacency matrix
adjacency_matrix = [[0 for a in range(no_vertexes)] for b in range(no_vertexes)]

# read in each edge
for i in range(no_edges):
    vertex1, vertex2, cost = [int(d) for d in input().split(' ')]
    # set cost values in adjacency matrix for bi directional edge
    adjacency_matrix[vertex1 - 1][vertex2 - 1] = cost
    adjacency_matrix[vertex2 - 1][vertex1 - 1] = cost

# get starting vertex
starting_vertex = int(input())

# set up priority queue
priority_queue = []

visited = [starting_vertex]

# addes an edge to the pq
# goes through each edge from the current_vertex to another and adds it to the pq if not already in it
def add_adjacent_vertices(adjacency_matrix, current_vertex, priority_queue, visited):
    connected = adjacency_matrix[current_vertex - 1]            # array containing costs of edges
    for c in range(len(connected)):
        if connected[c] > 0:                                    # edge from current_vertex to c is valid
            edge_info = (connected[c], current_vertex, c+1)
            edge_info_rev = (connected[c], c+1, current_vertex)
            if edge_info not in priority_queue:     # push into pq
                if c+1 not in visited:
                    heapq.heappush(priority_queue, edge_info)

add_adjacent_vertices(adjacency_matrix, starting_vertex, priority_queue, visited)    # add all adjacent vertices to start to pq

all_vertices = [x+1 for x in range(no_vertexes)]

total_cost = 0
while priority_queue:
    lowest_cost_edge = heapq.heappop(priority_queue)

    cost = lowest_cost_edge[0]
    next_vertex = lowest_cost_edge[2]
    cur_vertex = lowest_cost_edge[1]
    if next_vertex not in visited:
        total_cost += cost
        add_adjacent_vertices(adjacency_matrix, next_vertex, priority_queue, visited)
        visited.append(next_vertex)

       ##print(total_cost)
#print(visited)
print(total_cost)

'''
failed last 2 test cases, re do when free
'''