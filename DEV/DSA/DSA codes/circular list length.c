//
// Created by User on 9/21/2023.
//

#include "stdlib.h"
#include "stdio.h"

struct node{
    int x;
    struct node*next;
};
int choice,i=0;
struct node*head = NULL,*new_node,*temp;

 int main(){

     do{
     new_node = (struct node*)malloc(sizeof(struct node));
     printf("Enter a number: ");
     scanf("%d",&(*new_node).x);

     if(head == NULL){
         head = temp =new_node;
         (*new_node).next = head;
     }else{
         (*temp).next = new_node;
         temp = new_node;
         (*new_node).next = head;
     }

     printf("Do you want to continue: ");
     scanf("%d",&choice);
     }while(choice);

     //calculating the length of the list
     temp = head;

     while((*temp).next != head){
         i++;
         temp = (*temp).next;
     }i++;
     printf("length = %d",i);

     return 0;
 }