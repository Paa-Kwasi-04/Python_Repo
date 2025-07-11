//
// Created by User on 9/30/2023.
//
#include "stdio.h"
#define N 5
int stack[N];
int top = -1;

void push(){
    int x;
    printf("Enter the number: ");
    scanf("%d",&x);

    if(top == N-1){
        printf("Overflow condition");
    }else{
        top++;
        stack[top] = x;
    }
}

void pop(){
    int item;
    if(top == -1){
        printf("Underflow condition");
    }else{
        item  = stack[top];
        top--;
        printf("Enter the popped item is %d",item);
    }
}

void peek(){
    if(top == -1){
        printf("Underflow condition");
    }else{
        printf("%d",stack[top]);
    }
}

void display(){
    for(int i =top ; i>= 0;i--){
        printf("%5d", stack[i]);
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
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
        }
    }while(choice != 5);

    printf("Exited Program Successfully");
    return 0;
}