# NestedMonteCarlo

I used https://www.cprogramming.com/tutorial/lesson18.html to design Binary Trees

this is program that try to apply the Nested MonteCarlo Algorithm to try to find the best output of a scored binary tree.

# Classes

## Node

Is a node of the binary tree, can be composed of either two leaves or none if we are at the end of the tree

## btree
The binary tree is composed of nodes linked together two with one cascading and growing.
For instance :

                       10
                     /    \
                    6     14
                   / \    /  \
                  5   8  11  18

## Board
The game at a given time is displayed by a Board which is composed by a node from which we get moves, which are nothing but the leaves in which we can go from this node.

We have a function, legalMove(moves). It gives back an int : the number of admissible moves from the given Board, and therefore from the current node of the Board.
