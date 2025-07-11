//
// Created by User on 9/20/2023.
//
#include <conio.h>
#include "stdlib.h"
#include "stdio.h"

struct node
{
    int x;
    struct node *next;
};
int choice, i = 1;

int main()
{

    struct node *head = NULL, *newnode, *temp, *pretemp;

    do
    {
        newnode = (struct node *)malloc(sizeof(struct node));
        printf("Enter a number: ");
        scanf("%d", &newnode->x);
        newnode->next = NULL;

        if (head == NULL)
        {
            head = temp = newnode;
        }
        else
        {
            temp->next = newnode;
            temp = newnode;
        }
        printf("Do you want to continue: ");
        scanf("%d", &choice);
    } while (choice);

    // Reversing a linked list
    temp = head;
    while (head->next != NULL)
    {
        head = head->next;
    }

    return 0;
}
