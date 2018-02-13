#include "Board.h"

// to simplify we fist consider a board as a binary tree.

Board::Board(){
	newLength = 0;
	newScore = 0;

}; 

Board::~Board(){

}; 

Board::Board(btree b){
	newLength = NULL; //TO-DO : number of nodes which have leaves BUT how to count them ?

	newScore = NULL; //TO-DO : number on the current node BUT we don't know from b which is the current tree.
	
	moves = NULL;//TO-DO array of the left and right positions from current state 	//node *left; and node *right;
	
}; 

// gives the number of leaves we can play : either 2 or 0 in the binary-tree case.
int board::legalMoves(moves) 
{

	return NULL;
	
};


