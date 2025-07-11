//
// Created by User on 10/19/2023.
//
#include "stdlib.h"
#include "stdio.h"
#include "conio.h"

struct node
{
    int priority;
    int x;
    struct node *next;
};
int count = 0;
struct node *front = NULL, *rear, *newnode, *ptr, *preptr;

struct node *insertion(struct node *y)
{
    newnode = (struct node *)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->x);
    printf("Enter the priority number: ");
    scanf("%d", &newnode->priority);

    if (y == NULL || newnode->priority < y->priority)
    {
        newnode->next = y;
        y = newnode;
    }
    else
    {
        ptr = y;
        while (ptr != NULL && newnode->priority > ptr->priority)
        {
            preptr = ptr;
            ptr = ptr->next;
        }
        preptr->next = newnode;
        newnode->next = ptr;
    }
    return y;
}

struct node *dequeue(struct node *y)
{
    if (y == NULL)
    {
        printf("Under Flow Error");
    }
    else
    {
        ptr = y;
        y = y->next;
        free(ptr);
    }
    return y;
}

int Peek(struct node *y)
{
    if (y == NULL)
    {
        printf("Under Flow Error");
        return -1;
    }
    else
    {
        return y->x;
    }
}

void display(struct node *y)
{
    if (y == NULL)
    {
        printf("Under Flow Error");
    }
    else
    {
        ptr = y;
        while (ptr != NULL)
        {
            printf("%5d", ptr->x);
            ptr = ptr->next;
        }
    }
}

int main()
{
    int option;
    do
    {
        printf("\n----MENU----\n");
        printf("\n1. Insert into the Queue");
        printf("\n2. Dequeue the Queue");
        printf("\n3. Peek");
        printf("\n4. Display");
        printf("\n5. Exit");
        printf("\n");
        printf("Enter your option: ");
        scanf("%d", &option);

        switch (option)
        {
        case 1:
            front = insertion(front);
            break;
        case 2:
            front = dequeue(front);
            break;
        case 3:
            printf("First element : %d", Peek(front));
            break;
        case 4:
            display(front);
            break;
        default:
            printf("Invalid Option");
        }
    } while (option != 5);

    printf("You have Exited the Program :)");

    return 0;
};
