//
// Created by User on 10/11/2023.
//
#include "stdio.h"
#include "stdlib.h"
#include "conio.h"


struct node{
    int x;
    struct node*next;
};

struct node* front = NULL,*rear = NULL,*new_node,*temp;
struct node*enqueue(struct node *y,struct node *z){
    new_node = (struct node*)malloc(sizeof(struct node));
    printf("Enter -1 to end enqueuing");
    getch();
    printf("\nEnter element to enqueue: ");
    scanf("%d", &new_node->x);
    while(new_node->x != -1){
        if( y == NULL && z == NULL){
            y = z = new_node;
        }else{
            z->next = new_node;
            new_node->next = NULL;
            z = new_node;
        }
        new_node = (struct node*)malloc(sizeof(struct node));
        printf("\nEnter element to enqueue: ");
        scanf("%d", &new_node->x);
    }
    free(new_node);

    return y;
}

struct node*dequeue(struct node*y,struct node*z){
    if(y == NULL && z == NULL){
        printf("Underflow error");
    }else{
        temp = y;
        y = y->next;
        free(temp);
    }

    return y;
}

int peek(struct node*y,struct node*z){
    if(y == NULL && z == NULL){
        printf("Underflow error");
    }else{
        return y->x;
    }
}

void display(struct node*y,struct node*z){
    if(y == NULL && z == NULL){
        printf("Underflow error");
    }else{
        temp = y;
        while(temp != NULL){
            printf("%5d",temp->x);
            temp = temp->next;
        }
    }
}

int main() {
    int option;
    do {
        printf("\n-----MENU-----\n");
        printf("\n1. Enqueue operation");
        printf("\n2. Dequeue operation");
        printf("\n3. Peek operation");
        printf("\n4. Display the queue");
        printf("\n5. Exit");
        printf("\nEnter you option: ");
        scanf("%d", &option);
        switch (option) {
            case 1:
                front = enqueue(front,rear);
                printf("\n");
                printf("Enqueuing operation complete ");
                break;
            case 2:
                front = dequeue(front,rear);
                printf("\n");
                printf("Dequeuing operation complete ");
                break;
            case 3:
                printf("\n");
                printf("PEEK = %d",peek(front,rear));
                break;
            case 4:
                printf("\n");
                display(front,rear);
                break;
            default:
                printf("Invalid option");
        }
    } while (option != 5);

    printf("\n have exited the program :)");


    return 0;
}