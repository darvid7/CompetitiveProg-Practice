"""
@author: David Lei
@since: 25/11/2016
@modified: 

Best complexity with a adjacency map

https://www.hackerrank.com/challenges/dijkstrashortreach?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

I'm assuming I should implement a multigraph (allow multiple edges b/w ndoes) rather than picking the smallest edge b/w two nodes and updating
Note:
- graph can be disconnected
- can't seem to import math.inf in hackerrank python3, fix with special cases in class comparators

Test case 7: Time out,  ~ 20s on mpb, everythign else works
"""
from sys import stdin, stdout

import heapq

class Node:
    def __init__(self, no):
        self.num = no
        self.edges = {}
        self.visited = False
        self.dist = "?"            # set all nodes to have infinity distance, can use >,<,== on .inf

    # class comparators for min_heap to work
    def __lt__(self, other):
        if self.dist == "?" and other.dist == "?":
            return False
        elif other.dist == "?":
            return True
        elif self.dist == "?":
            return False
        elif self.dist < other.dist:
            return True
        return False

    def __gt__(self, other):
        if self.dist == "?" and other.dist == "?":
            return False
        elif self.dist == "?":
            return True
        elif other.dist == "?":
            return False
        elif self.dist > other.dist:
            return True
        return False

    def __eq__(self, other):
        if self.dist == "?" and other.dist == "?":
            return True
        elif self.dist == "?" or other.dist == "?":
            return False
        elif self.dist == other.dist:                 # type error if comparing "?" and int
            return True
        return False

class Edge:
    def __init__(self, node_a, node_b, weight):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight



t = int(input())

import time
start = time.time()

for _ in range(t):
    # edge_value_mapping = {}                                         # map edge_key to weight
    adj_map = {}
    no_nodes, no_edges = [int(x) for x in input().split(' ')]
    for j in range(1, no_nodes + 1):
        adj_map[j] = Node(j)
    # edges are weighted bidirectional
    for i in range(no_edges):
        # note: can have multiple edges b/w a pair of the same nodes
        node_a, node_b, weight = [int(x) for x in input().split(' ')]
        # assume pick only smallest edge of all edges

        # 19 seconds
        if node_b in adj_map[node_a].edges.keys():                     # same edge seen before
            cur_weight = adj_map[node_a].edges[node_b].weight
            if cur_weight > weight:
                new_edge = Edge(adj_map[node_a], adj_map[node_b], weight)
                adj_map[node_a].edges[node_b] = new_edge
                adj_map[node_b].edges[node_a] = new_edge
            else:
                pass
        else:
            new_edge = Edge(adj_map[node_a], adj_map[node_b], weight)
            adj_map[node_a].edges[node_b] = new_edge
            adj_map[node_b].edges[node_a] = new_edge

    """
        # 23 seconds
        edge_key_forwards = str(node_a) + "-" + str(node_b)
        edge_key_backwards = str(node_b) + "-" + str(node_a)

        if edge_key_forwards in edge_value_mapping.keys():
            cur_weight = edge_value_mapping[edge_key_forwards]
            if cur_weight > weight:
                # update mapping
                edge_value_mapping[edge_key_forwards] = weight
                edge_value_mapping[edge_key_backwards] = weight
        else:
            edge_value_mapping[edge_key_forwards] = weight
            edge_value_mapping[edge_key_backwards] = weight

    # process edge value mapping to add only one of each edge to the graph rep
    edge_value_mapping_list = list(edge_value_mapping.items())
    for edge_key, weight in edge_value_mapping_list:
        node_a, node_b = [int(x) for x in edge_key.split('-')]
        new_edge = Edge(adj_map[node_a], adj_map[node_b], weight)
        adj_map[node_a].edges[node_b] = new_edge
    """

    start_node_key = int(input())

    # implement dijkstra
    start_node = adj_map[start_node_key]
    start_node.dist = 0                                                 # set start node dist to 9

    min_heap = []
    all_nodes_list = [pair[1] for pair in list(adj_map.items())]
    for node in all_nodes_list:                                         # add nodes to min_heap
        heapq.heappush(min_heap, node)
    changed = False
    while(min_heap):                                                    # node need to mark node visited, start with everything in min_heap, when nothing left end
        if changed:
            heapq.heapify(min_heap)
            changed = False
        visited_node = heapq.heappop(min_heap)
        visited_node.visited = True
        outgoing_edges = list(visited_node.edges.items())

        for k, edge in outgoing_edges:                                     # check all edges and neighbouring nodes

            if visited_node == edge.node_a:                             # should be able to handle loop to self
                to_node = edge.node_b
            else:
                to_node = edge.node_a
            # note: does if x or y
            # x evaluated first so if to_node.dist is "?" there will be no type error in the comparison

            if to_node.visited or visited_node.dist == "?":
                # print("Seen ya before")
                pass
            else:
                if ( (to_node.dist == "?") or ((visited_node.dist + edge.weight) < to_node.dist) ):        # edge relaxation
                    to_node.dist = visited_node.dist + edge.weight
                    # heapq.heapify(min_heap)
                    changed = True



    # at the end, if dist is  then the node is not reachable
    all_nodes = list(adj_map.items())
    all_nodes.sort(key = lambda t:t[1].num)
    for key, node in all_nodes:
        if node.num != start_node_key:
            if node.dist != "?":
                stdout.write(str(node.dist)+" ")
                # print(node.dist, end=" ")
            else:
                # print("-1", end=" ")
                stdout.write("-1 ")
    print()
print(start - time.time())