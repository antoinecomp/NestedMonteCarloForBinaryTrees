#ifndef DEF_BOARD
#define DEF_BOARD

struct Board{

    public:
        btree();
        ~btree();

        void insert(int key);
        node *search(int key);
        void destroy_tree();
    	void legalMoves(Move moves);

    private: // why having put the same ones
        void destroy_tree(node *leaf);
        void insert(int key, node *leaf);
        node *search(int key, node *leaf); //
        
        node *root;

};


#endif
