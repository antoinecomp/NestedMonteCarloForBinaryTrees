# Attempt to apply a Nested Monte Carlo Algorithm to binary trees

from random import *
import numpy as np

MaxPlayoutLength = 20 # what ?

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

		print("Board initialized")
		print("root :")
		print(self.root.key)
		print("btree.root.left")
		print(btree.root.left)
		print("btree.root.right")
		print(btree.root.right)

		# length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

		moves = np.zeros(2) 
		if(btree.root.left != None):
			self.moves[0] = btree.root.left #/DONE? 
			self.moves[1] = btree.root.right
			score = btree.root.key

	def legalMoves(self, moves):
		if(moves.all != None):
			return 2
		elif(moves.any != None):
			return 1
		else:
			return 0

	def terminal(self):
		if((self.root.left == None) and (self.root.right  == None)):
			print("board terminal")
			return True
		else:
			return False

	def score(self):
		return node.key

	def getLegalMoves(self,node):
		if(node.left != None):
			self.moves[0] = node.left
			self.moves[1] = node.right
			return moves

	def play(self,key):
		'''chose the next node we dive into, if legal :
		- node : next node the player wants to dive into
		'''
		# no test for the moment, let's see if it can make it
		node = self.tree.find(key)
		self.root = node
		self.root.left = node.left
		self.root.right = node.right

		# length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

def playout(board):
	moves[2]# shoudln't we get them from the board ?
	while(True):
		nb = board.legalMoves(self.moves)
		if((nb == 0) or board.terminal()):
			return board.score()
		n = random.randint(0, nb) # chose a number between 0 and the number of legal moves
		board.play(moves[n]) # play a random move
		if(board.length >= MaxPlayoutLength -20):
			return 0

bestScoreNested = -9999
DBL_MAX = -9999

arraySize = 10

lengthBestRollout = np.zeros(10) # array of size 10
scoreBestRollout = np.zeros(10) # array of size 10

bestRollout =np.zeros((10,MaxPlayoutLength)) # 2 dimensional array of size 10*MaxPlayoutLength

def nested(board, n):
	'''Nested Monte Carlo algorithm
	a general name for a broad class of algorithms that use random sampling to obtain numerical results.
	It is used to solve statistical problems by simulation.'''

	nbMoves = 0
	moves = np.zeros(2)

	lengthBestRollout[n] -1
	scoreBestRollout[n] - DBL_MAX
	res = -DBL_MAX
	while(True):
		# if it's over we've reached the bottom of the tree
		if(board.terminal()):
			return 0.0
		nbMoves = board.legalMoves(moves) # moves is full of 0s here ... what has bestRollout[n][board.length] then ?
		for i in range(0,nbMoves):
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
		board.play(bestRollout[n][board.length])
	return 0.0
			
if __name__ == "__main__":
	# tests
	t = Tree()
	t.insert(5)
	t.insert(6)
	t.insert(8)
	t.insert(10)
	t.insert(11)
	t.insert(14)
	t.insert(18)

	b = Board(t)

	score = nested(b,3)
	print("the algorithm score is ",score)

	# Remember: Find method return the node object. 
	# To return a number use t.find(nº).key
	# But it will cause an error if the number is not in the tree.
	# print(t.find(5)) 
	# print(t.find(8))
