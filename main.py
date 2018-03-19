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
# This Tree is not balanced.
class Tree:
	def __init__(self):
		self.root = None

	# Insert a single element
	def insert(self, x):
		if(self.root == None):
		    self.root = Node(x)
		else:
		    self._insert(x, self.root)

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
	
class Board:
	def __init__(self, btree, node):
		self.root = node

		# length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

		moves = np.zeros(2) 
		if(node.left != None):
			moves[0] = node.left #/DONE? array of the left and right positions from current state 	//node *left; and node *right;
			moves[1] = node.right
			score = node.key

	def legalMoves(self, moves):
		if(move != None):
			return 2
		else:
			return 0

	def terminal(self):
		if(self.root.left == None):
			return True
		else:
			return False

	def score(self):
		return node.key

	def getLegalMoves(self,node):
		if(node.left != None):
			moves[0] = node.left
			moves[1] = node.right
			return moves

		# length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

def playout(board):
	moves[2]
	while(True):
		nb = board.legalMoves(moves)
		if((nb == 0) or board.terminal()):
			return board.score()
		n = rand() * nb # chose a number between 0 and the number of legal moves
		board.play(moves[n]) # play a random move
		if(board.length >= MaxPlayoutLength -20):
			return 0

bestScoreNested = -9999
DBL_MAX = -9999

arraySize = 10

mm = np.matrix([])

lengthBestRollout = np.zeros(10) # array of size 10
scoreBestRollout = np.zeros(10) # array of size 10

bestRollout =np.zeros((10,MaxPlayoutLength)) # 2 dimensional array of size 10*MaxPlayoutLength

def nested(board, n):
	nbMoves = 0
	moves = np.zeros(2)

	lengthBestRollout[n] -1
	scoreBestRollout[n] - DBL_MAX
	res = -DBL_MAX
	while(True):
		# if it's over
		if(board.terminal()):
			return 0.0
		nbMoves = board.legalMoves(moves)
		# otherwise
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

	b = Board(t,Node(5))

	score = nested(b,3)
	print("the algorithm score is ",score)

	# Remember: Find method return the node object. 
	# To return a number use t.find(nº).key
	# But it will cause an error if the number is not in the tree.
	# print(t.find(5)) 
	# print(t.find(8))
