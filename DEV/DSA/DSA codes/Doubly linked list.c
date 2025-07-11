//
// Created by User on 9/23/2023.
//
#include "stdio.h"
#include "stdlib.h"

struct node{
    struct node*prev;
    int x;
    struct node*next;
};

struct node*head = NULL,*new_node,*temp,*ptr;

struct node* create(struct node*y) {

    int choice;
    do{
        new_node = (struct node *) malloc(sizeof(struct node));
        printf("\nEnter a number: ");
        scanf("%d", &(*new_node).x);
        (*new_node).next = NULL;

        if (y == NULL) {
            y = temp = new_node;
            (*new_node).prev = NULL;
        } else {
            (*new_node).prev = temp;
            (*temp).next = new_node;
            temp = new_node;
        }

        printf("Do you want to continue: ");
        scanf("%d", &choice);
    }while(choice);


    return y;
}
struct node* insert_beg(struct node*y){
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("\nEnter a number: ");
    scanf("%d", &(*new_node).x);

    (*new_node).prev = NULL;
    (*y).prev = new_node;
    (*new_node).next = y;
    y = new_node;

    return y;
}
struct node* insert_end(struct node*y){
    temp = y;
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("\nEnter a number: ");
    scanf("%d", &(*new_node).x);


    while(temp->next != NULL){
        temp = (*temp).next;
    }
    (*new_node).prev = temp;
    (*temp).next = new_node;
    (*new_node).next = NULL;

    return y;
}
struct node* insert_before(struct node*y){
    int pos;
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter value to be placed at the beginning: ");
    scanf("%d", &(*new_node).x);
    printf("Enter position you want to insert: ");
    scanf("%d",&pos);
    temp = y;

    for(int i= 1;i<pos;i++){
        temp = (*temp).next;
    }
    ptr = temp->prev;
    ptr->next = new_node;
    new_node->prev = ptr;
    new_node->next = temp;
    temp->prev = new_node;


    return y;
}
struct node* delete_beg(struct node*y){
    temp = y;
    temp->next->prev = NULL;
    y = temp->next;
    free(temp);

    return y;
}
struct node* delete_end(struct node*y){
    temp = y;

    while(temp->next != NULL){
        temp = (*temp).next;
    }
    temp->prev->next = NULL;
    free(temp);

    return y;
}
struct node* delete_node(struct node*y){
    int pos;
    printf("Enter position you want to delete: ");
    scanf("%d",&pos);

    temp = y;
    for(int i = 0;i<pos;i++){
        temp = (*temp).next;
    }
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    free(temp);

    return y;
}//
struct node* delete_list(struct node*y){
    temp = y;

    while(temp->next != NULL){
        temp = delete_beg(temp);
    }

    return y;
}
void display(struct node*y){
    //Printing the list
    temp = y;
    while(temp != NULL){
        printf("%3d", (*temp).x);
        temp = (*temp).next;
    }

}
int length(struct node*y){
    int count = 0;
    temp = y;
    while(temp != NULL){
        temp = (*temp).next;
        count++;
    }

    return count;
}




int main() {
    int choice;
    do {
        printf("\n\n------MENU-------\n");
        printf("1.Create Double linked List\n");
        printf("2.Insert a node at the begin\n");
        printf("3.Insert a node at the end\n");
        printf("4.Insert a node at a given position\n");
        printf("5.Delete the first node\n");
        printf("6.Delete the last node\n");
        printf("7.Delete a node at a given position\n");
        printf("8.Delete the entire list\n");
        printf("9.Display the list\n");
        printf("10.Find the length of the list\n");
        printf("11.Exit\n");

        printf("\nEnter your Option: ");
        scanf("%d", &choice);

        switch (choice) {
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
                head = insert_before(head);
                printf("Node has been inserted\n");
                break;
            case 5:
                head = delete_beg(head);
                printf("first node has been deleted\n");
                break;
            case 6:
                head = delete_end(head);
                printf("last node has been deleted\n");
                break;
            case 7:
                head = delete_node(head);
                printf("Node has been deleted\n");
                break;
            case 8:
                head = delete_list(head);
                printf("The list has been deleted\n");
                break;
            case 9:
                display(head);
                printf("\n");
                break;
            case 10:
                printf("Length of list: %d\n", length(head));
                break;

        }

    }while(choice != 11);

    printf("\n\nYou have exited the program ");
    return 0;
}
/*

 */