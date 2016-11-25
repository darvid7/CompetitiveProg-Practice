"""
@author: David Lei
@since: 22/11/2016
@modified: 

https://www.hackerrank.com/challenges/bfsshortreach

Ideal to use an adjacency map, allows for O(1) operations and O(e/n) enum

Submission: all test cases passed
"""
class Node:
    def __init__(self, no, depth):
        self.num = no
        self.depth = depth
        self.chosen = False
        self.edges = {}
        self.visited = False
        self.enqueued = False

def get_direct_neighbouring_nodes(all_nodes, node_num):

    can_get_to = []
    reachable_nodes = all_nodes[node_num].edges
    reachable_nodes_list = list(reachable_nodes.items())
    for key, node in reachable_nodes_list:
        if not node.visited:
            if not node.enqueued:
                can_get_to.append(node)

    return can_get_to


# distances are uniform and are all 6 units
q = int(input())
for _ in range(q):
    out = []
    no_nodes, no_edges = [int(x) for x in input().split(' ')]   # this type of assignment works
    # note: nodes labeled 1,..,n

    all_nodes = {}
    for n in range(1, no_nodes+1):
        all_nodes[n] = Node(n, 0)
    # all_nodes = [Node(n, 0) for n in range(1, (no_nodes+1))]

    for i in range(no_edges):
        node_u_key, node_v_key = [int(x) for x in input().split(' ')]   # edge connecting node u to node v
        # add edge to adj matrix, -1 as nodes are numbered 1,..,n
        # matrix[node_u][node_v] = 1
        # matrix[node_v][node_u] = 1
        # node int key maps to another node
        all_nodes[node_u_key].edges[node_v_key] = all_nodes[node_v_key]
        all_nodes[node_v_key].edges[node_u_key] = all_nodes[node_u_key]

    start_node_key = int(input())

    start_node = all_nodes[start_node_key]                            # start node with depth = 0

    # do a bfs from start node
    # #print shortest distance from start node to each node, don't #print start node, if can't get to #print -1
    queue = [start_node]
    while(queue):
        node_out = queue.pop()

        if node_out != start_node:
            node_out.chosen = True

        node_out.visited = True

        direct_neighbours = get_direct_neighbouring_nodes(all_nodes, node_out.num)

        for node in direct_neighbours:
            node.depth = node_out.depth + 1
            queue.insert(0, node)           # maintain fifo order
            node.enqueued = True

    all_nodes_list = list(all_nodes.items())
    all_nodes_list.sort(key = lambda t:t[1].num)

    for pair in all_nodes_list:
        number = pair[0]
        node = pair[1]
        if number != start_node.num:
            if not node.chosen:
                print("-1", end=" ")
                #print(node.num, end="* ")
            else:
                # node = get_out_w_num(out, num)
                print(node.depth*6, end=" ")
                #print(node.num, end="* ")

    print()