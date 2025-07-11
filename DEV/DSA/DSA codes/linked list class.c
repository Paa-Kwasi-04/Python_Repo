//
// Created by User on 9/19/2023.
//
#include "stdlib.h"
#include "stdio.h"
#include "conio.h"

struct node {
    int x;
    struct node *next;
};
int option;
struct node *start = NULL;

// declaring the functions that perform algorithms on the linked list created
struct node *create_ll(struct node *);
struct node *display(struct node *);
struct node *insert_beg(struct node *);
struct node *insert_end(struct node *);
struct node *insert_before(struct node *);
struct node *insert_after(struct node *);
struct node *delete_beg(struct node *);
struct node *delete_end(struct node *);
struct node *delete_node(struct node *);
struct node *delete_after(struct node *);
struct node *delete_list(struct node *);


int main() {
    do {
        printf("\n\n *****MAIN MENU *****");
        printf("\n 1:Create a list");
        printf("\n 2:Display the list");
        printf("\n 3:Add a node at the beginning");
        printf("\n 4:Add a node at the end");
        printf("\n 5:Add a node before a given node");
        printf("\n 6:Add a node after a given node");
        printf("\n 7: Delete a node from the beginning");
        printf("\n 8: Delete a node from the end");
        printf("\n 9: Delete a given node");
        printf("\n 10: Delete a node after a given node");
        printf("\n 11: Delete the entire list");
//        printf("\n 12: Sort the list");
//        printf("\n 13: EXIT");
        printf("\n\n Enter your option : ");
        scanf("%d", &option);
    } while (option != 13);
    switch (option) {
        case 1:
            start = create_ll(start);
            printf("\n LINKED LIST CREATED");
            break;
        case 2:
            start = display(start);
            break;
        case 3:
            start = insert_beg(start);
            break;
        case 4:
            start = insert_end(start);
            break;
        case 5:
            start = insert_before(start);
            break;
        case 6:
            start = insert_after(start);
            break;
        case 7: start = delete_beg(start);
            break;
        case 8: start = delete_end(start);
            break;
        case 9: start = delete_node(start);
            break;
        case 10: start = delete_after(start);
            break;
        case 11: start = delete_list(start);
            printf("\n LINKED LIST DELETED");
            break;
//        case 12: start = sort_list(start);
//            break;
    }
    return 0;
}

//function for creating the linked list
struct node *create_ll(struct node *start) {
    struct node *new_node, *ptr;
    int num, choice;

    do {
        new_node = (struct node *) malloc(sizeof(struct node));
        printf("\n Enter the data : ");
        scanf("%d", &num);
        (*new_node).x = num;
        (*new_node).next = NULL;
        if (start == NULL) {
            start = new_node;
            ptr = start;
        } else {
            ptr = (*ptr).next;
            (*ptr).next = new_node;
        }
        printf("Do you want to continue: ");
        scanf("%d", &choice);
    } while (choice);
    return start;
}

//function for displaying the content of the linked list
struct node *display(struct node *start) {
    struct node *ptr;
    ptr = start;
    while (ptr != NULL) {
        printf("\t %d", (*ptr).x);
        ptr = (*ptr).next;
    }
    return start;
}

//function to insert a node at the beginning of linked list
struct node *insert_beg(struct node *start) {
    struct node *new_node;
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("\n Enter the data : ");
    scanf("%d", &(*new_node).x);
    (*new_node).next = start;
    start = new_node;
    return start;
}

//function to insert a node at the end of a linked list
struct node *insert_end(struct node *start) {
    struct node *ptr, *new_node;
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("\n Enter the data : ");
    scanf("%d", &(*new_node).x);
    (*new_node).next = NULL;
    ptr = start;
    while ((*ptr).next != NULL)
        ptr = (*ptr).next;
    (*ptr).next = new_node;
    return start;
}

//function to insert a node before a given node
struct node *insert_before(struct node *start)
{
    struct node *new_node, *ptr, *preptr;
    int val;
    new_node = (struct node *)malloc(sizeof(struct node));
    printf("\n Enter the data : ");
    scanf("%d",&(*new_node).x);
    printf("\n Enter the value before which the data has to be inserted : ");
    scanf("%d", &val);

    ptr = start;
    while((*ptr).x != val)
    {
        preptr = ptr;
        ptr = (*ptr).next;
    }
    (*preptr).next = new_node;
    (*new_node).next = ptr;
    return start;
}

//function to delete the first node in the linked list
struct node *delete_beg(struct node *start)
{
    struct node *ptr;
    ptr = start;
    start = (*start).next;
    free(ptr);
    return start;
}

//function to delete the last node in the linked list
struct node *delete_end(struct node *start)
{
    struct node *ptr, *preptr;
    ptr = start;
    while((*ptr).next != NULL)
    {
        preptr = ptr;
        ptr = (*ptr).next;
    }
    (*preptr).next = NULL;
    free(ptr);
    return start;
}

//function to delete a node at a specified position
struct node *delete_node(struct node *start)
{
    struct node *ptr, *preptr;
    int val;
    printf("\n Enter the value of the node which has to be deleted : ");
    scanf("%d", &val);
    ptr = start;
    if((*ptr).x  == val)
    {
        start = delete_beg(start);
        return start;
    }
    else
    {
        while((*ptr).x != val)
        {
            preptr = ptr;
            ptr = (*ptr).next;
        }
        (*preptr).next = (*ptr).next;
        free(ptr);
        return start;
    }
}

//function to delete a node after a given node
struct node *delete_after(struct node *start)
{
    struct node *ptr, *preptr;
    int val;
    printf("\n Enter the value after which the node has to deleted : ");
    scanf("%d", &val);
    ptr = start;
    while((*ptr).x != val)
    {
        preptr = ptr;
        ptr = (*ptr).next;
    }
    (*preptr).next=(*ptr).next;
    free(ptr);
    return start;
}

//function to delete a linked list
struct node *delete_list(struct node *start)
{
    struct node *ptr; // Lines 252-254 were modified from original code to   fixunresposiveness in output window
    if(start!=NULL)
    {
        ptr=start;
        while(ptr != NULL)
        {
            printf("\n %d is to be deleted next", (*ptr).x);
            start = delete_beg(ptr);
            ptr = start;
        }
    }
    return start;
}



