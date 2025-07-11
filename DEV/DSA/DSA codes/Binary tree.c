//
// Created by User on 11/9/2023.
//
#include "stdio.h"
#include "stdlib.h"
#include "conio.h"


struct node
{
    int data;
    struct node*left,*right;
};

struct node*root = NULL;

//creating normal binary tree recursively
struct node*create(){
    int x;
    struct node*newnode = (struct node*)malloc(sizeof(struct node));

    printf("\nEnter data (-1 for no node): ");  scanf("%d",&x);

    if (x == -1)
    {
        return 0;
    }
    newnode->data = x;
    printf("Enter left child of %d",x);
    getch();
    newnode->left = create();
    printf("Enter right child of %d",x);
    getch();
    newnode->right = create();

    return newnode;
}

//preorder traversal
void preorder(struct node*root){
    if(root == NULL){
        return;
    }else{
        printf("%d",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

//inorder traversal
void inorder(struct node*root){
    if(root == NULL){
        return;
    }else{
        inorder(root->left);
        printf("%d",root->data);
        inorder(root->right);
    }
}

//postorder traversal
void postorder(struct node*root){
    if(root == NULL){
        return;
    }else{
        postorder(root->left);
        postorder(root->right);
        printf("%d",root->data);

    }
}


int main()
{

    root = create();
    postorder(root);
    return 0;

}
