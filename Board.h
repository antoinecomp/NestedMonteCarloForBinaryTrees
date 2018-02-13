#include <iostream> //usefull ?
#include <string> //usefull ?
#include <vector>

#ifndef DEF_BOARD
#define DEF_BOARD

class Board{

    public:
        board();
        ~board();

		//a Board is made from a binary tree. Furthermore he has a score, a length
		board(btree);

		//And he has possible blows
		legalMoves(moves)

    private:
		//member variables
		int length;
		int score;
		// create move ? Array of the following possibilities : left/right ? Or none if we reached the end
		vector<int> tableau(2,NULL);
		

};


#endif
