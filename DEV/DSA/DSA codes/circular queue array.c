//
// Created by User on 10/14/2023.
//
#include "stdio.h"
#include "conio.h"
#define MAX 60

int queue[MAX], NUM ;
int front = -1, rear = -1;
void enqueue() {
    printf("Enter -1 to end enqueuing");
    getch();
    printf("\nEnter element to enqueue: ");
    scanf("%d", &NUM);
    while (NUM != -1) {
        if (rear == -1 && front == -1) {
            front = rear = 0;
            queue[rear] = NUM;
        } else if ((rear+1)%MAX == front) {
            printf("Overflow error");
        }
        else {
            rear = (rear+1)%MAX;
            queue[rear] = NUM;

        }
        printf("\nEnter element to enqueue: ");
        scanf("%d", &NUM);
    }
}
void dequeue() {
    if (front == -1 && rear == -1) {
        printf("Under flow error");
    }else if(front == rear){
        front = rear = -1;
    }
    else {
        front  = (front+1)%MAX;
        printf("Dequeue operation successful");
    }
}

void display() {
    int i = front;
    if (front == -1 || rear == -1) {
        printf("Under flow error");
    } else {
       while(i != rear){
           printf("%5d",queue[i]);
           i = (i+1)%MAX;
       }printf("%5d",queue[i]);
    }
}

void peek() {
    if (front == -1 || front > rear) {
        printf("Under flow error");
    } else {
        printf("front = %d", queue[front]);
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
        printf("\n\nEnter you option: ");
        scanf("%d", &option);
        switch (option) {
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
            default:
                printf("Invalid option");
        }
    } while (option != 5);

    printf("\n\n have exited the program :)");


    return 0;
}
