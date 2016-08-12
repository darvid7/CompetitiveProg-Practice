"""
@author: David Lei
@since: 25/07/2016
@modified: 

"""

class Node:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.connections = []
    def add_connection(self, anotherNode):
        self.connections.append(anotherNode)
    def get_val(self):
        return self.val
    def get_connections(self):
        return self.connections

# use a queue

import heapq

t = int(input())

def find_node(nodes, find_this):
    for i in nodes:
        if i.get_val() == find_this:
            return i

def to_next_node(cur, next):
    connections = cur.get_connections()
    if next in connections:
        return 6
    else:
        return -1

for i in range(t):
    no_nodes, no_edges = [int(c) for c in input().split(' ')]
    nodes = []
    for k in range(1,no_nodes+1):
        new_node = Node(k)
        nodes.append(new_node)
    for j in range(no_edges):
        n1, n2 = [int(c) for c in input().split(' ')]
        node1 = find_node(nodes, n1)
        node2 = find_node(nodes, n2)
        node1.add_connection(n2)
        node2.add_connection(n1)

    starting = int(input())
    node_vals = [o+1 for o in range(no_nodes)]
    st_idx = node_vals.index(starting)
    del node_vals[st_idx]
    start = find_node(nodes, starting)
    for l in range(no_nodes-1):
        distance = to_next_node(start, node_vals[l])
        print(distance, end= " ")
    print('\n', end="")
