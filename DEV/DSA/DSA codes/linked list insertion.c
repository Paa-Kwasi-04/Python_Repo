//
// Created by User on 9/19/2023.
//
#include <conio.h>
#include "stdlib.h"
#include "stdio.h"


struct node {
    int x;
    struct node *next;
};
int choice;

int main() {

    struct node *head = NULL, *newnode, *temp;

    do{
        newnode = (struct node *) malloc(sizeof(struct node));
        printf("Enter a number: ");
        scanf("%d", &(*newnode).x);
        (*newnode).next = NULL;

        if (head == NULL) {
            head = temp = newnode;
        } else {
            (*temp).next = newnode;
            temp = newnode;
        }
        printf("Do you want to continue: ");
        scanf("%d", &choice);
    } while (choice);

    //inserting at the beginning of the linked list

    newnode = (struct node*) malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d", &(*newnode).x);
    (*newnode).next = head;
    head = newnode;

    //insertion at the end
    newnode = (struct node*) malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d", &(*newnode).x);
    (*newnode).next = NULL;

    temp = head;
    while((*temp).next != NULL){
        temp = (*temp).next;
    }
    (*temp).next = newnode;

    //insertion after any given location
    int pos,i=1;
    newnode = (struct node*)malloc(sizeof(struct node));
    printf("which position do you want to insert at: ");
    scanf("%d",&pos);

    temp = head;
    while(i<pos){
        temp = (*temp).next;
        i++;
    }
    printf("Enter a number: ");
    scanf("%d", &(*newnode).x);
    //this assigns the address of the node after the position to the newnode's next pointer
    (*newnode).next = (*temp).next;
    //this assigns the node before the position with the address of the newnode
    (*temp).next = newnode;















    return 0;
}