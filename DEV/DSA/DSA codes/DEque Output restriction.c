//
// Created by User on 10/17/2023.
//where you can delete and insert from either the front or end
//there are two variants of the deque
// input restriction and output restriction

#include "stdio.h"
#include "stdlib.h"


struct node {
    int x;
    struct node *next;
};

struct node *front = NULL, *rear = NULL, *newnode, *temp,*pretemp;
struct node *enqueue_front(struct node *y) {
    newnode = (struct node *) malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->x);
    newnode->next = NULL;

    if(y == NULL){
        y = rear = newnode;
        newnode->next = y;
    }else{
        newnode->next = y;
        y = newnode;
        rear->next = y;
    }
    return y;
}
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


//for the output restriction I choose to dequeue from the rear
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

int front_peek(struct node *y) {
    if (y == NULL) {
        printf("Underflow error");
        return -1;
    } else
        return y->x;
}

int rear_peek(struct node *y) {
    if (y == NULL ) {
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
    do {
        printf("\n-----MENU-----\n");
        printf("\n1. Enqueue at front operation");
        printf("\n2. Enqueue at rear operation");
        printf("\n3. Dequeue at rear operation");
        printf("\n4. Front peek operation");
        printf("\n5. Rear peek operation");
        printf("\n6. Display the queue");
        printf("\n7. Exit");
        printf("\nEnter you option: ");
        scanf("%d", &option);
        switch (option) {
            case 1:
                front = enqueue_front(front);
                printf("\n");
                printf("Enqueuing operation complete ");
                break;
            case 2:
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
                printf("Front peek = %d", front_peek(front));
                break;
            case 5:
                printf("\n");
                printf("Front peek = %d", rear_peek(front));
                break;
            case 6:
                printf("\n");
                display(front, rear);
                break;
            default:
                printf("Invalid option");
        }
    } while (option != 7);

    printf("\n have exited the program :)");

    return 0;
}








