# Created by William La at 7:15 PM 11/22/2016
# Contact me at: williamla0907@gmail.com
# This program requires python 3.5.x to compile.
# This is an implementation for path vector routing algorithm popularly used
#   to create paths for data transmission by Internet Service Providers.
# The program will create paths to reachable points from every node on an internet
# More information about this algorithm at Behrouz A. Forouzan,
#   Data Communications and Networking 5ht Edition, page 610
# Test case: An interconnection with 8 nodes named from 1 to 7, 6 and 7 are private and disconnected from
#            the rest
# To test: the command line will asked for the number of nodes on the tree, and follow by asking
#           each node's neighbors.
#           For example: When asked for neighbors of node 3, type in 2 4 5, then press enter
#                  0--1--2--3--4    6
#                         \ | /     |
#                           5       7

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
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, value):
        self._paths = value


# Initialization for reachable paths for each Node
def initialization(N, node):
    for y in range(N):
        s = []
        if node.name == y:
            s.append(node.name)
            node.paths.append(s)
        elif str(y) in node.neighbours:
            s.append(node.name)
            s.append(y)
            node.paths.append(s)
        else:
            s.append("")
            node.paths.append(s)


# Update the path from a node to it neighbour
def update(node, neighbour, tree):
    path_ys = neighbour.paths
    path_ws = node.paths
    origin = []
    for item in neighbour.paths:
        origin.append(item)
    for i in range(len(path_ys)):
        neighbour.paths[i] = best(path_ys[i], path_ws[i], neighbour)

    if neighbour.paths != origin:
        for i in neighbour.neighbours:
            update(neighbour, tree[int(i)], tree)
    return tree


# Find the better path to other nodes for a neighbour node
def best(path_y, path_w, neighbour):
    if path_w == ['']:
        return path_y
    else:
        path_new_w = []
        path_new_w.append(neighbour.name)
        for item in path_w:
            path_new_w.append(item)
        if neighbour.name in path_w:
            return path_y
        elif path_y == ['']:
            neighbour._changed = True
            return path_new_w
        elif len(path_new_w) < len(path_y):
            neighbour._changed = True
            return path_new_w
        else:
            return path_y


# Print the tree
def print_tree(tree):
    print("\nThe list of nodes, their neighbours and theirs reachable paths:")
    for node in tree:
        print("\nnode name: {}".format(node._name))
        print("node neighbours: {}".format(node._neighbours))
        print("node paths: {}".format(node._paths))


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
    if N == 0:
        print("Thank you!")
        pass
    else:
        tree = []  # Create a tree
        # Build the tree by prompt user input
        for i in range(N):
            s = input("Input neighbor nodes of node number {0!s}, "
                      "separately by a space: ".format(i)).split(" ")
            tree.append(Node(i, s))  # Add nodes to the tree
            initialization(N, tree[i])  # Initializing reachable paths for each node of the tree
        # Update paths in the tree
        for item in tree:
                for i in item.neighbours:
                    tree = update(item, tree[int(i)], tree)
        print_tree(tree)

# Call main()
main()
