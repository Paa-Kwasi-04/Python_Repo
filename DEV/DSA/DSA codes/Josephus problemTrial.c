//
// Created by User on 10/28/2023.

#include "stdio.h"
#include "stdlib.h"

struct node {
    int data;
    struct node *next;
};

int main() {
    int N, k;
    struct node *head,*temp , *new_node;
    printf("Enter the number of individuals: ");
    scanf("%d", &N);
    printf("Enter k value: ");
    scanf("%d", &k);
    new_node = (struct node *) malloc(sizeof(struct node));
    head = new_node;
    new_node->data = 1;
    temp = head;


    //creating the ring of N individuals
    for (int i = 2; i <= N; i++) {
        new_node = (struct node *) malloc(sizeof(struct node));
        new_node->data = i;
        temp->next = new_node;
        new_node->next = head;
        temp = new_node;
    }


//Creating simulation for josephus problem
    temp = head;
    for(int i = 0;i<N;i++){
        for(int j = 0;j<k-1;j++){
            temp = temp->next;
        }
        temp->next = temp->next->next;
    }

    printf("\n The Winner is Player %d", temp->data);

    return 0;
}
