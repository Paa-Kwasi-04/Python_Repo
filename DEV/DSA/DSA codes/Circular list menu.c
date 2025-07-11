//
// Created by User on 9/21/2023.
//

#include "stdlib.h"
#include "stdio.h"

struct node {
    int x;
    struct node *next;
};

struct node *head = NULL, *new_node, *temp,*pretemp;


struct node *create(struct node *y) {
    int choice;
    do{
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter any number: ");
    scanf("%d", &(*new_node).x);

    if (y == NULL) {
        y = temp = new_node;
        (*new_node).next = y;
    } else {
        (*temp).next = new_node;
        temp = new_node;
        (*new_node).next = y;
    }

    printf("Do you want to continue: ");
    scanf("%d", &choice);
    }while(choice);

    return y;
}
struct node *insert_beg(struct node *y) {
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter value to be placed at the beginning: ");
    scanf("%d", &(*new_node).x);
    temp = y;
    while ((*temp).next != y) {
        temp = (*temp).next;
    }
    (*temp).next = new_node;
    (*new_node).next = y;
    y = new_node;

    return y;
}
struct node *insert_end(struct node*y){
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter value to be placed at the end: ");
    scanf("%d", &(*new_node).x);

    temp = y;
    while((*temp).next != y){
        temp = (*temp).next;
    }
    (*temp).next = new_node;
    (*new_node).next = y;

    return y;
}
struct node *insert_node(struct node*y){
    int pos;
    new_node = (struct node *) malloc(sizeof(struct node));
    printf("Enter value to be placed at the beginning: ");
    scanf("%d", &(*new_node).x);
    printf("Enter position you want to insert: ");
    scanf("%d",&pos);
    temp = y;

    for(int i = 0;i<pos;i++){
        pretemp = temp;
        temp = (*temp).next;
    }
    (*new_node).next  = temp;
    (*pretemp).next = new_node;

    return y;
}
struct node* delete_beg(struct node*y){
    temp = y;
    while((*temp).next != y){
        temp = (*temp).next;
    }
    (*temp).next = (*y).next;
    free(y);
    y = (*temp).next;

    return y;
}
struct node* delete_end(struct node*y){
    temp = y;
    while((*temp).next != y){
        pretemp = temp;
        temp = (*temp).next;
    }
    (*pretemp).next = (*temp).next;
    free(temp);

    return y;
}
struct node* delete_node(struct node*y){
    int pos;
    printf("Enter position you want to delete: ");
    scanf("%d",&pos);

    temp = y;
    for(int i = 0;i<pos;i++){
        pretemp = temp;
        temp = (*temp).next;
    }
    (*pretemp).next = (*temp).next;
    free(temp);


    return y;
}
struct node* delete_list(struct node*y){
     temp = y;
     while((*temp).next != y){
       temp = delete_end(temp);
     }y = NULL;
     free(temp);

     return y;
}
void display(struct node *y) {
    temp = y;
    while ((*temp).next != y) {
        printf("%3d", (*temp).x);
        temp = (*temp).next;
    }printf("%3d", (*temp).x);


}
int length(struct node*y){
    int count = 0;
    temp = y;
    while((*temp).next != y){
        temp = (*temp).next;
        count++;
    }count++;

    return count;
}




int main() {
    int choice;
    do {
        printf("\n\n------MENU-------\n");
        printf("1. Create Circular List\n");
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
                head = insert_node(head);
                printf("Node has been inserted\n");
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
            case 9:
                display(head);
                printf("\n");
                break;
            case 10:
                printf("Length of list = %d\n", length(head));

        }

    }while(choice != 11);

    printf("\n\nYou have exited the program ");
    return 0;
}