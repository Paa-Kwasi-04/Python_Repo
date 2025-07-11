//
// Created by User on 9/20/2023.
//
#include <conio.h>
#include "stdlib.h"
#include "stdio.h"


struct node {
    int x;
    struct node *next;
};
int choice,i = 1;

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

    //finding the length of linked list
    temp = head;

    while((*temp).next != NULL){
        i++;
        temp = (*temp).next;
    }
    printf("the length: %d",i);


    return 0;
}
