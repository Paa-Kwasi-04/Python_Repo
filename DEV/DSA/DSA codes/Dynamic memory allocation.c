//
// Created by User on 10/1/2023.
//
#include "stdlib.h"
#include "stdio.h"


int main(){
    int a[5];

    for(int i= 0;i<5;i++){
        scanf("%d",&a[i]);
    }

    for(int i= 0;i<5;i++){
        printf("%5d",a[i]);
    }


    return 0;
}