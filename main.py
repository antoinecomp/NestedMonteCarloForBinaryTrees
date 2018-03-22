# Attempt to apply a Nested Monte Carlo Algorithm to binary trees

import random
from random import randint
import numpy as np

MaxPlayoutLength = 20 # what ?


# global variables
bestScoreNested = -9999
DBL_MAX = -9999

arraySize = 10

lengthBestRollout = np.zeros(10) # array of size 10
scoreBestRollout = np.zeros(10) # array of size 10

bestRollout =np.zeros((10,MaxPlayoutLength)) # 2 dimensional array of size 10*MaxPlayoutLength

# Class for construct the nodes of the tree. (Subtrees)
class Node:
	def __init__(self, key, parent_node = None):
		self.left = None
		self.right = None
		self.key = key
		if parent_node == None:
		    self.parent = self
		else:
		    self.parent = parent_node

# Class with the  structure of the tree. 
# I'm not sure if this Tree is balanced.
class Tree:
	def __init__(self):
		self.root = None

	# Insert a single element
	def insert(self, x):
		if(self.root == None):
		    self.root = Node(x)
		else:
		    self._insert(x, self.root)

	# place it at the right palce
	def _insert(self, x, node):
		if(x < node.key):
		    if(node.left == None):
		        node.left = Node(x, node)
		    else:
		        self._insert(x, node.left)
		else:
		    if(node.right == None):
		        node.right = Node(x, node)
		    else:
		        self._insert(x, node.right)

	# Given a element, return a node in the tree with key x. 
	def find(self, x):
		if(self.root == None):
		    return None
		else:
		    return self._find(x, self.root)

	def _find(self, x, node):
		if(x == node.key):
		    return node
		elif(x < node.key):
		    if(node.left == None):
		        return None
		    else:
		        return self._find(x, node.left)
		elif(x > node.key):
		    if(node.right == None):
		        return None
		    else:
		        return self._find(x, node.right)

	# Given a node, return the node in the tree with the next largest element.
	def next(self, node):
		if node.right != None:
		    return self._left_descendant(node.right)
		else:
		    return self._right_ancestor(node)

	def _left_descendant(self, node):
		if node.left == None:
		    return node
		else:
		    return self._left_descendant(node.left)

	def _right_ancestor(self, node):
		if node.key <= node.parent.key:
		    return node.parent
		else:
		    return self._right_ancestor(node.parent)

	# Delete an element of the tree
	def delete(self, x):
		node = self.find(x)
		if node == None:
		    print(x, "isn't in the tree")
		else:
		    if node.right == None:
		        if node.left == None:
		            if node.key < node.parent.key:
		                node.parent.left = None
		                del node # Clean garbage
		            else:
		                node.parent.right = None
		                del Node # Clean garbage
		        else:
		            node.key = node.left.key
		            node.left = None
		    else:
		        x = self.next(node)
		        node.key = x.key
		        x = None

# a tree with a selected node at a given time
class Board:
	'''a Board is a tree with a node selected which gives a score'''
	def __init__(self, btree):
		self.tree = btree
		self.root = btree.root
		self.root.left = btree.root.left
		self.root.right = btree.root.right
		self.length = 0 # length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?
		self.rollout = [btree.root.key]# selected nodes
		self.moves = np.zeros(2)
		self.scoreBoard = btree.root.key 

		print("Board initialized")
		print("root :")
		print(self.scoreBoard)

		if(btree.root.left is not None):
			self.moves[0] = btree.root.left.key

		if(btree.root.right is not None):
			self.moves[1] = btree.root.right.key




	def legalMoves(self):
		moves = np.zeros(2)# shoudln't we get them from the board ?
		'''Assign the number of legal moves from root and gives the number of legal Moves'''
		numberLegal = 0
		# we assign the array of possible moves
		if(self.root.left is not None):
			moves[0] = self.root.left.key
		if(self.root.right is not None):
			moves[1] = self.root.right.key

		# we get the number of legalMoves
		for i in range(0,len(moves)):
			if(moves[i] != 0):
				numberLegal = numberLegal+1

		# and we give back the number of possible moves and the moves theselves
		return numberLegal, moves

	def terminal(self):
		'''Test wether we reached the end of a branch of a tree'''
		if((self.root.left == None) and (self.root.right  == None)):
			return True
		else:
			return False

	def score(self):
		'''Gives the value of the root'''
		return self.root.key

	def play(self,key):
		'''chose the next node we dive into, if legal :
		- node : next node the player wants to dive into
		'''
		# no test for the moment, let's see if it can make it
		node = self.tree.find(key)
		print("key we try to play : ",key)
		if(node is not None):
			self.length = self.length +1
			self.rollout.append(key)
			print("where we went : ",self.rollout)
			self.root = node
			self.root.left = node.left
			self.root.right = node.right
			print("BOARD HAS CHANGED")
		else:
			#print("Trying to play a key which doesn't belong to the tree")
			#print(key)
			print("")

		# length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

def playout(board):
	'''from Tristan Cazenave's algorithm'''
	while(True):
		nb,moves = board.legalMoves()
		if((nb == 0) or board.terminal()):
			return board.score()
		n = random.randint(0, nb) # chose a number between 0 and the number of legal move
		print("play a random move",moves[n])
		board.play(moves[n]) # play a random move
		if(board.length >= MaxPlayoutLength -20):
			return 0



def nested(board, n):
	'''Nested Monte Carlo algorithm
	a general name for a broad class of algorithms that use random sampling to obtain numerical results.
	It is used to solve statistical problems by simulation.'''
	bestScoreNested = -9999
	nbMoves = 0
	lengthBestRollout[n] -1
	scoreBestRollout[n] -9999
	res = -9999
	while(True):
		# we test wether we reached the bottom of the tree
		if(board.terminal()):
			print("***Tentative terminée***")
			return 0.0 # but why should it be 0.0 ?
		# we get the number of moves and moves we can go from the selected nodes
		nbMoves,moves = board.legalMoves()
		# ???
		for i in range(0,nbMoves):
			moves = list(filter (lambda a: a != 0.0, moves))
			print("moves : ")
			print(moves)
			b = board
			b.play(moves[i])
			if(n==1):
				playout(board)
			else:
				nested (board, n-1)
			score = board.score()
			if(score > scoreBestRollout [n]):
				scoreBestRollout [n] = score
				lengthBestRollout [n] = board.length
				for k in range(0,board.length):
					bestRollout[n][k]=board.rollout[k]
				if(n>3):
					for i in range(0,t<n-1):
						print("n =", n,"progress =", board.length, "score =", scoreBestRollout [n])
						depth = 0
						# board.print(stderr) # what 
						print("")
						bestBoard = board
				if ((n > 1) and (score > bestScoreNested)):
					bestScoreNested = score
					print("best score = ", score)
					print("")
					bestBoard = board
		# unsure about what the following one does :
		board.play(bestRollout[n][board.length])
		#board.play(5)
		print()
	return 0.0
			
if __name__ == "__main__":
	# tests
	t = Tree()
	compteur = 0
	t.insert(10)
	t.insert(11)
	t.insert(14)
	t.insert(18)
	t.insert(5)
	t.insert(6)
	t.insert(8)

	b = Board(t)

	score = nested(b,2)
	#print("the algorithm score is ",score)

	# Remember: Find method return the node object. 
	# To return a number use t.find(nº).key
	# But it will cause an error if the number is not in the tree.
	# print(t.find(5)) 
	# print(t.find(8))
