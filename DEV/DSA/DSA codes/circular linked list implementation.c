//
// Created by User on 9/20/2023.
//
#include "stdio.h"
#include "stdlib.h"

struct node{
    int x;
    struct node*next;
};
int choice;
struct node*head = NULL,*new_node,*temp;

int main(){

    do{
         new_node = (struct node*) malloc(sizeof(struct node));
         printf("Enter a number: ");
        scanf("%d",&(*new_node).x);
        (*new_node).next = NULL;

         if(head == NULL){
        head = new_node;
        temp = new_node;
        (*new_node).next = head;
        }else{
        (*temp).next =new_node;
        temp = new_node;
        (*new_node).next = head;
        }

        printf("Do you want to continue: ");
        scanf("%d",&choice);
    }while(choice);

    //displaying the circular linked list
    temp = head;

    while((*temp).next != head){
        printf("%5d",(*temp).x);
        temp = (*temp).next;
    }printf("%5d",(*temp).x);





    return 0;
}