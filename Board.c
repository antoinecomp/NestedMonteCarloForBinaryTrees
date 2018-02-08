#include "Board.h"


// to simplify we fist consider a board as a binary tree.


int board::legalMoves(moves) //pb c'est quoi moves, un tableau de Move et du coup il faut creer la classe Move ?
{

}

board::board()
{
  root=NULL;
}

void board::destroy_tree(node *leaf)
{
  if(leaf!=NULL)
  {
	destroy_tree(leaf->left);
	destroy_tree(leaf->right);
	delete leaf;
  }
}

void board::insert(int key, node *leaf)
{
  if(key< leaf->key_value)//if the value wa want to insert is 
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

node *board::search(int key, node *leaf)
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

node *board::search(int key, node *leaf)
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

// public insert
void board::insert(int key)
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

// public destroy
void board::destroy_tree()
{
  destroy_tree(root);
}

// public search
node *board::search(int key)
{
  return search(key, root);
}

