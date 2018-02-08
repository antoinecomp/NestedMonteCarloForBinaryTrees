//#include "nestedSH.c"
//#include "nestedSimple.c"
//#include "nrpa.c"
//#include "beamnrpa.c"
#include "Board.h"
#include "Node.h"

int main(int argc, char *argv []) {
  if (argc > 1)  {
    seed = atoi (argv [1]);
    srand (seed);
  }

  while (true) {
    Board b;
	b.insert(5);
	b.insert(6);
	b.insert(8);
	b.insert(10);
	b.insert(11);
	b.insert(14);
	b.insert(18);
    //nestedSimple(b, 3);
    //bestBoard.print (stderr);
    //fprintf (stderr, "best score %lf\n", bestBoard.score ());
    break;
  }
}

