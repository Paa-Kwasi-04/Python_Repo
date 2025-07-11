//Queues
// Created by User on 10/11/2023.
//types of queues
//circular queue,
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
        } else if (rear == MAX - 1) {
            printf("Overflow error");
        } else {
            rear++;
            queue[rear] = NUM;

        }
        printf("\nEnter element to enqueue: ");
        scanf("%d", &NUM);
    }
}

void dequeue() {
    if (front == -1 || front > rear) {
        printf("Under flow error");
    }else if(front == rear){
        front = rear = -1;
    }
    else {
        front++;
        printf("Dequeue operation successful");
    }
}

void display() {
    if (front == -1 || front > rear) {
        printf("Under flow error");
    } else {
        for (int i = front; i <= rear; i++) {
            printf("%5d", queue[i]);
        }
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






























































































