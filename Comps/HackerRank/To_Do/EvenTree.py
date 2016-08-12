"""
@author: David Lei
@since: 25/07/2016
@modified: 

"""

class TreeNode:
    def __init__(self, data):
        self.root = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


no_nodes, no_edges = [int(c) for c in input().split(' ')]
for i in range(no_edges):
    n1, n2 = [int(c) for c in input().split(' ')]

