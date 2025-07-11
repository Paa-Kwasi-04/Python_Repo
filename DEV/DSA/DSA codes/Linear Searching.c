//
// Created by User on 11/15/2023.
//
#include "stdio.h"



int main(){
    int n = 6,val,flag =0;
    int a[6] = {12,8,10,5,3,7},i;

    //Enter value to search for
    printf("Enter Value to search for: ");
    scanf("%d",&val);

    //Linear Searching: when the data in question is small
    for(i = 0;i< n;i++){
        if(a[i] == val){
            flag = 1;
            break;
        }
    }

    if(flag == 1){
        printf("%d was found ",val);
    } else{
        printf("Not found in array");
    }






    return 0;
}