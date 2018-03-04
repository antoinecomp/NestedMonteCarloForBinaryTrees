#define NULL 0
#include <vector>
#include <cstdlib>

using namespace std;

// this is program that try to apply the Nested MonteCarlo Algorithm to try to find the best output of a scored binary tree.
// The binary tree is composed of nodes which have key_values.

struct node
{
  int key_value;
  node *left;
  node *right;
};

//it's an array of possible moves. It takes node left and node right from a given node in a Board
struct Move{
		vector<node> moves[2];
};

class btree
{
    public:
        btree();
        ~btree();

        void insert(int key);
        node *search(int key);
        void destroy_tree();

    private:
        void destroy_tree(node *leaf);
        void insert(int key, node *leaf);
        node *search(int key, node *leaf);

        node *root;
};

btree::btree()
{
  root=NULL;
}

btree::~btree()
{
  destroy_tree();
}

void btree::destroy_tree(node *leaf)
{
  if(leaf!=NULL)
  {
    destroy_tree(leaf->left);
    destroy_tree(leaf->right);
    delete leaf;
  }
}

void btree::insert(int key, node *leaf)
{
  if(key< leaf->key_value)
  {
    if(leaf->left!=NULL)
     insert(key, leaf->left);
    else
    {
      leaf->left=new node;
      leaf->left->key_value=key;
      leaf->left->left=NULL;    //Sets the left child of the child node to null
      leaf->left->right=NULL;   //Sets the right child of the child node to null
    }  
  }
  else if(key>=leaf->key_value)
  {
    if(leaf->right!=NULL)
      insert(key, leaf->right);
    else
    {
      leaf->right=new node;
      leaf->right->key_value=key;
      leaf->right->left=NULL;  //Sets the left child of the child node to null
      leaf->right->right=NULL; //Sets the right child of the child node to null
    }
  }
}
void btree::insert(int key)
{
  if(root!=NULL)
    insert(key, root);
  else
  {
    root=new node;
    root->key_value=key;
    root->left=NULL;
    root->right=NULL;
  }
}
node *btree::search(int key, node *leaf)
{
  if(leaf!=NULL)
  {
    if(key==leaf->key_value)
      return leaf;
    if(key<leaf->key_value)
      return search(key, leaf->left);
    else
      return search(key, leaf->right);
  }
  else return NULL;
}

node *btree::search(int key)
{
  return search(key, root);
}

void btree::destroy_tree()
{
  destroy_tree(root);
}



// Display the current state of a game
class Board{

    public:
        Board();
        ~Board();

		//a Board is made from a binary tree. Furthermore he has a score, a length
		Board(btree,node);
		Move getLegalMoves(node);
		//Move moves = getLegalMoves(node);
		//And he has possible blows
		int legalMoves(Move); // where we can go from node

    private:
		//member variables
		int length;
		int score;
		node n; // Where we are at the moment of the board
		// Instnatiation moves ? Array of the following possibilities : left/right ? Or none if we reached the end
		// Move moves; // error: redeclaration of ‘Move Board::moves’
		

};

Board::Board(){
	length = 0;
	score = 0;

}; 

Board::~Board(){

}; 

Board::Board(btree b, node n){
	length = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

	score = n.key_value; //DONE? : number on the current node FROM node
	Move moves[2];
	if(n->*left != NULL)
		moves[0] = n->*left;//DONE? array of the left and right positions from current state 	//node *left; and node *right;
		moves[1] = n->*right;
	
}; 

// gives the number of leaves we can play : either 2 or 0 in the binary-tree case.
int Board::legalMoves(Move moves){
	//If there is leaves there is at least two moves.
	if(n->*left != NULL){// wrong we have to take move into account
		return 2;	
	}//otherwise there is no possibilities
	else{
		return 0;
	}
	
};

// gives the number of leaves we can play : either 2 or 0 in the binary-tree case.
Move Board::getLegalMoves(node n){
	if(n->*left != NULL)
		moves[0] = n->*left;//DONE? array of the left and right positions from current state 	//node *left; and node *right;
		moves[1] = n->*right;
};



/**/
double playout (Board * board) {
	Move moves [2];
	//Move moves [MaxLegalMoves];
	while (true) {
		int nb = board->legalMoves (moves);
		if ((nb == 0) || board->terminal ())
			return board->score ();
			int n = rand () % nb;
			board->play (moves [n]);
		if (board->length >= MaxPlayoutLength - 20) {
			return 0;
		}
	}
};


#include <float.h>

double bestScoreNested = -DBL_MAX;

int lengthBestRollout [10];
double scoreBestRollout [10];
Move bestRollout [10] [MaxPlayoutLength];

Board bestBoard;

// What is int n ?
double nested (Board & board, int n) {
	int nbMoves = 0;
	Move moves [2]; // are we creating an object Move ? Why isn't it Move(...) ?
	Move moves [MaxLegalMoves]; // are we creating an object Move ? Why isn't it Move(...) ?

	lengthBestRollout [n] = -1;
	scoreBestRollout [n] = -DBL_MAX;
	float res;
	while (true) {
		// if there is no more moves to play ?
		if (board.terminal ())
			return 0.0;
			//return board.score();
		// if there is still things to play
		nbMoves = board.legalMoves(moves); // BUT moves is empty at the beginning ???
		for (int i = 0; i < nbMoves; i++) {
			Board b = board;
			b.play(moves[i]);
		  	if (n == 1)
				playout (&b);
		  	else
				nested (b, n - 1);     
				double score = b.score ();
		    if (score > scoreBestRollout [n]) {
				scoreBestRollout [n] = score;
				lengthBestRollout [n] = b.length;
				for (int k = 0; k < b.length; k++)
		  			bestRollout [n] [k] = b.rollout [k];
				// what is n ?
				if (n > 3) {
					for (int t = 0; t < n - 1; t++)
						fprintf (stderr, "\t");
				  	fprintf (stderr, "n = %d, progress = %d, score = %f\n", n, board.length, scoreBestRollout [n]);
					int depth = 0;
					b.print (stderr);
					fprintf (stderr, "\n");
				}
				if ((n > 1) && (score > bestScoreNested)) {
					bestScoreNested = score;
					fprintf (stderr, "best score = %f\n", score);
					b.print (stderr);
					fprintf (stderr, "\n");
					bestBoard = b;
				}
			}
		}
		board.play (bestRollout [n] [board.length]);
	}
  return 0.0;
};

/**/

int main(int argc, char *argv []) {
    btree b;
    b.insert(5);
    b.insert(6);
    b.insert(8);
    b.insert(10);
    b.insert(11);
    b.insert(14);
    b.insert(18);

	// create board with b 
	board boa(b)
	
    nestedSimple(b, 3);
    bestBoard.print (stderr);
    fprintf (stderr, "best score %lf\n", bestBoard.score ());

	return(0);
}
