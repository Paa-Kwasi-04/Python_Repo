//
// Created by User on 10/1/2023.
//
#include "stdio.h"
#include "stdlib.h"

struct node{
    int data;
    struct node* next;
};
struct node*top = NULL,*newNode,*temp;

struct node* push(struct node*y){
    newNode = (struct node*) malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d",&newNode->data);

    if(y == NULL){
        y = newNode;
        newNode->next = NULL;
    }else{
        newNode->next = y;
        y = newNode;
    }


    return  y;
}
struct node* pop(struct node*y){
    if(y == NULL){
        printf("Underflow Condition");
    }else{
        temp = y;
        y = temp->next;
        free(temp);
    }

    return y;
}
void peek(struct node*y){
    if(y == NULL){
        printf("Underflow Condition");
    }else{
        printf("top = %d",y->data);
    }
}
void display(struct node*y){
    if(y == NULL){
        printf("Underflow Condition");
    }else{
        temp = y;
        while(temp != NULL){
            printf("%5d",temp->data);
            temp = temp->next;
        }
    }
}

int main(){
    int choice;
    do{
        printf("\n\n-----MENU-----\n");
        printf("1.Push into stack\n");
        printf("2.Pop out of stack\n");
        printf("3.Peep stack\n");
        printf("4.Display stack\n");
        printf("5.Exit\n\n");

        printf("Enter option: ");
        scanf("%d",&choice);

        switch (choice) {
            case 1:
                top = push(top);
                printf("\n");
                break;
            case 2:
                top = pop(top);
                printf("\n");
                break;
            case 3:
                peek(top);
                printf("\n");
                break;
            case 4:
                display(top);
                printf("\n");
                break;
        }
    }while(choice != 5);

    printf("Exited Program Successfully");
    return 0;
}