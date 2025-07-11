//
// Created by User on 10/17/2023.
//

#include "stdio.h"
#include "stdlib.h"
#include "conio.h"


struct node {
    int x;
    struct node *next;
};

struct node *front = NULL, *rear = NULL, *newnode, *temp,*pretemp;

// for the input restriction I choose to enqueue from the rear
struct node *enqueue_rear(struct node *y) {
    newnode = (struct node *) malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->x);
    newnode->next = NULL;

    if(y == NULL){
        y = rear = newnode;
        newnode->next = y;
    }else{
        rear->next = newnode;
        newnode->next = y;
        rear = newnode;
    }

    return y;
}

struct node *dequeue_front(struct node *y) {
    if (y == NULL) {
        printf("Underflow error");
    } else {
        temp = y;
        y = y->next;
        rear->next = y;
        free(temp);
    }
    return y;
}

struct node *dequeue_rear(struct node *y) {
    if (y == NULL) {
        printf("Underflow error");
    } else {
        temp = y;
        while(temp != rear){
            pretemp = temp;
            temp = temp->next;
        }
        pretemp->next = temp->next;
        rear = pretemp;
        free(temp);
    }
    return y;
}

int front_peek(struct node *y, struct node *z) {
    if (y == NULL && z == NULL) {
        printf("Underflow error");
        return -1;
    } else
        return y->x;
}

int rear_peek(struct node *y) {
    if (y == NULL) {
        printf("Underflow error");
        return -1;
    } else
        return rear->x;
}

void display(struct node *y, struct node *z) {
    if (y == NULL && z == NULL) {
        printf("Underflow error");
    } else {
        temp = y;
        while (temp->next!= y) {
            printf("%5d", temp->x);
            temp = temp->next;
        }printf("%5d", temp->x);
    }
}

int main() {
    int option;
    getch();
    do {
        printf("\n-----MENU-----\n");
        printf("\n1. Enqueue at rear operation");
        printf("\n2. Dequeue at front operation");
        printf("\n3. Dequeue at rear operation");
        printf("\n4. Front peek operation");
        printf("\n5. Rear peek operation");
        printf("\n6. Display the queue");
        printf("\n7. Exit");
        printf("\nEnter you option: ");
        scanf("%d", &option);
        switch (option) {
            case 2:
                front = dequeue_front(front);
                printf("\n");
                printf("Dequeuing operation complete ");
                break;
            case 1:
                front = enqueue_rear(front);
                printf("\n");
                printf("Enqueuing operation complete ");
                break;
            case 3:
                front = dequeue_rear(front);
                printf("\n");
                printf("Dequeuing operation complete ");
                break;
            case 4:
                printf("\n");
                printf("Front peek = %d", front_peek(front, rear));
                break;
            case 5:
                printf("\n");
                printf("Front peek = %d", rear_peek(front));
                break;
            case 6:
                printf("\n");
                display(front, rear);
                break;
        }
    } while (option != 7);

    printf("\n You have exited the program :)");

    return 0;
}