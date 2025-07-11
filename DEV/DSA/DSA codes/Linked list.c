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
    temp = head;
    while (temp != NULL) {
        printf("%5d", (*temp).x);
        temp = (*temp).next;
    }
    getch();

    return 0;
}