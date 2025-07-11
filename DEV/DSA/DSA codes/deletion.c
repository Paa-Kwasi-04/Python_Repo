//
// Created by User on 9/20/2023.
//
#include "stdlib.h"
#include "stdio.h"

struct node {
    int x;
    struct node *next;
};
int choice;
struct node *head = NULL, *new_node, *temp,*pretemp;

int main() {

    do {
        new_node = (struct node *) malloc(sizeof(struct node));
        printf("Enter a number: ");
        scanf("%d", &(*new_node).x);
        (*new_node).next = NULL;

        if (head == NULL) {
            head = new_node;
            temp = new_node;
        } else {
            (*temp).next = new_node;
            temp = new_node;
        }
        printf("Do you want to continue: ");
        scanf("%d", &choice);
    } while (choice);

    //printing the linked list
    temp = head;
    while(temp != NULL){
        printf("%d",(*temp).x);
        temp = (*temp).next;
    }

    //deleting the first node in the linked list
    temp =  head;
    head = (*temp).next;
    free(temp);

    //deleting the last node in the linked list
    temp = head;
    while((*temp).next != NULL){
        pretemp = temp;
        temp = (*temp).next;
    }
    (*pretemp).next = NULL;
    free(temp);

    //deleting from a node from a specified position
    int posi,c=1;
    printf("Enter position whose node you want to delete: ");
    scanf("%d",&posi);

    temp = head;

    while(c < posi){
        pretemp = temp;
        temp = (*temp).next;
        c++;
    }
    (*pretemp).next = (*temp).next;
    free(temp);

    // deleting the whole linked list
    temp = head;

    while((*temp).next != NULL){
        pretemp = temp;
        temp = (*temp).next;
        free(pretemp);
    }
    head = NULL;



    return 0;
}


