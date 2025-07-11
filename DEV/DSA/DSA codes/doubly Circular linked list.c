//
// Created by User on 9/27/2023.
//
#include <conio.h>
#include "stdlib.h"
#include "stdio.h"


struct node {
    struct node *prev;
    int x;
    struct node *next;
};

int choice = 1, num;
struct node *head = NULL, *new_node, *temp, *ptr;

struct node *create(struct node *y) {

    printf("Enter 0 to end the list\n\n");
    while (choice != 0) {
        new_node = (struct node *) malloc(sizeof(struct node));
        printf("\nEnter a number: ");
        scanf("%d", &new_node->x);
        choice = new_node->x;

        if (y == NULL) {
            y = temp = new_node;
            new_node->next = y;
            new_node->prev = new_node;
        } else {
            temp->next = new_node;
            new_node->prev = temp;
            new_node->next = y;
            y->prev = new_node;
            temp = new_node;
        }
    }

    return y;
}
struct node *insert_beg(struct node *y) {
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d", &(*new_node).x);

    temp = ptr = y;
    ptr = temp->prev;
    ptr->next = new_node;
    new_node->prev = ptr;
    new_node->next = temp;
    temp->prev = new_node;
    y = new_node;

    return y;
}
struct node *insert_end(struct node *y) {
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d", &(*new_node).x);

    temp = ptr = y;

    while (temp->next != y) {
        temp = temp->next;
    }
    temp->next = new_node;
    new_node->prev = temp;
    ptr->prev = new_node;
    new_node->next = ptr;

    return y;
}
struct node *insert_before(struct node *y) {
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d", &(*new_node).x);
    printf("Enter number you want to insert before: ");
    scanf("%d", &num);
    temp = y;
    while (temp->x != num) {
        ptr = temp;
        temp = temp->next;
    }
    ptr->next = new_node;
    new_node->prev = ptr;
    new_node->next = temp;
    temp->prev = new_node;

    return y;
}
struct node *insert_after(struct node *y) {
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d", &(*new_node).x);
    printf("Enter number you want to insert after: ");
    scanf("%d", &num);
    temp = y;
    while (temp->x != num) {
        temp = temp->next;
    }
    ptr = temp->next;
    temp->next = new_node;
    new_node->prev = temp;
    ptr->prev = new_node;
    new_node->next = ptr;

    return y;
}
struct node *delete_beg(struct node *y) {
    temp = y;
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    y = temp->next;
    free(temp);

    return y;
}
struct node *delete_end(struct node *y) {
    temp = y;
    ptr = temp->prev;
    ptr->prev->next = temp;
    temp->prev = ptr->prev;

    free(ptr);


    return y;
}
struct node *delete_before(struct node *y) {
    printf("Enter number you want to delete before: ");
    scanf("%d", &num);
    temp = y;

    while (temp->x != num) {
        ptr = temp;
        temp = temp->next;
    }
    ptr->prev->next = temp;
    temp->prev = ptr->prev;
    free(ptr);

    return y;

}
struct node *delete_after(struct node *y) {
    printf("Enter number you want to delete after: ");
    scanf("%d", &num);
    temp = y;

    while (temp->x != num) {
        temp = temp->next;
    }
    ptr = temp->next;
    temp->next = ptr->next;
    ptr->next->prev = temp;


    free(ptr);

    return y;

}
struct node *delete_list(struct node *y) {
    temp = y;
    while (temp->next != y) {
        temp = delete_end(temp);
    }
    free(temp);
    y = NULL;

    return y;
}
void display(struct node *y) {
    temp = y;
    while (temp->next != y) {
        printf("%5d", temp->x);
        temp = temp->next;
    }
    printf("%5d", temp->x);
}
struct node *sort(struct node *y) {
    temp = ptr = y;
    while (temp->next != y) {
        while (temp->next != y) {
            ptr = temp->next;
            if (temp->x > ptr->x) {
                int c = temp->x + ptr->x;
                temp->x = c - temp->x;
                ptr->x = c - temp->x;
            } else {
                continue;
            }
        }
    }

    return y;
}


int main() {
    int choices;
    do {
        printf("\n\n\n------MENU-------\n");
        printf("1.Create Double linked List\n");
        printf("2.Insert a node at the begin\n");
        printf("3.Insert a node at the end\n");
        printf("4.Insert a node after a given number\n");
        printf("5.Insert a node before a given number\n");
        printf("6.Delete the first node\n");
        printf("7.Delete the last node\n");
        printf("8.Delete a node before a given number\n");
        printf("9.Delete a node after a given number\n");
        printf("10.Delete the entire list\n");
        printf("11.Sort the list\n");
        printf("12.Display the list\n");
        printf("13.Exit\n");

        printf("\nEnter your Option: ");
        scanf("%d", &choices);

        switch (choices) {
            case 1:
                head = create(head);
                break;
            case 2:
                head = insert_beg(head);
                printf("Node has been inserted\n");
                break;
            case 3:
                head = insert_end(head);
                printf("Node has been inserted\n");
                break;
            case 4:
                head = insert_after(head);
                printf("Node has been inserted\n");
                break;
            case 5:
                head = insert_before(head);
                printf("Node has been inserted\n");
                break;
            case 6:
                head = delete_beg(head);
                printf("first node has been deleted\n");
                break;
            case 7:
                head = delete_end(head);
                printf("last node has been deleted\n");
                break;
            case 8:
                head = delete_before(head);
                printf("Node has been deleted\n");
                break;
            case 9:
                head = delete_after(head);
                printf("Node has been deleted\n");
                break;
            case 10:
                if (delete_list(head) == NULL) {
                    printf("The list has been deleted\n");
                }
                break;
            case 11:
                head = sort(head);
                break;
            case 12:
                display(head);
                printf("\n");
                break;
        }

    } while (choices != 13);



    printf("\n\nYou have exited the program ");
    return 0;
}