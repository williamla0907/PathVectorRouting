# Created by William La at 7:15 PM 11/22/2016
# Contact me at: williamla0907@gmail.com
# This program requires python 3.5.x to compile.
# This is an implementation for path vector routing algorithm popularly used
#   to create paths for data transmission by Internet Service Providers.
# More information about this algorithm at Behrouz A. Forouzan,
#   Data Communications and Networking 5ht Edition, page 610

# Structure for Nodes which consist the data of names, neighbour nodes, and reachable paths
class Node:
    def __init__(self, name, neighbours):
        self._name = name
        self._neighbours = neighbours
        self._paths = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def neighbours(self):
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value):
        self._neighbours = value

    @property
    def path(self):
        return self._paths

    @path.setter
    def path(self, value):
        self._paths = value

# Initialization for reachable paths for each Node
def initialization(N, node):
    for y in range(N):
        s = []
        if node._name == y:
            s.append(node._name)
            node._paths.append(s)
        elif str(y) in node._neighbours:
            s.append(node._name)
            s.append(y)
            node._paths.append(s)
        else:
            s.append("")
            node._paths.append(s)

def print_tree(tree):
    for node in tree:
        print("node name: {}".format(node._name))
        print("node neighbours: {}".format(node._neighbours))
        print("node paths: {}".format(node._paths))
        print("\n\n")


# Define main function
def main():

    # Prompt user to input # of nodes on the tree and check for error input
    while True:
        try:
            N = int(input("How many nodes in the tree? "))
            break
        except ValueError:
            print("Ops! That is no valid number! Try again...!")
    # If the input is 0 meaning there is no node on the tree, the program exit
    if(N == 0):
        print("Thank you!")
        pass
    else:
        tree = [] # Create a tree
        # Build the tree by prompt user input
        for i in range(N):
            s = input("Input neighbor nodes of node number {0!s}, "
                      "separately by a space: ".format(i)).split(" ")
            tree.append(Node(i, s)) # Add nodes to the tree
            initialization(N, tree[i])



main()
