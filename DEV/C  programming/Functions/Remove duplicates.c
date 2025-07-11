////TODO:doesn't run all the code
// Created by User on 7/4/2023.
//Write a C program to remove duplicates from a sorted integer array.
// The program should modify the original array in place.
#include <stdio.h>
int i,k,j,l,x;
int a[5];
const int len = sizeof(a) / sizeof(int);


// function for creating user array
void create_array(){
    for (i = 0; i < len; i++) {
        if (i == 0) {
            printf("Enter a number: ");
        } else {
            printf("Enter another number: ");
        }
        scanf("%d", &a[i]);
    }
}

void bubble_sorting(){
    //Bubble sorting the array
    for(k = 0; k < len; k++){
        for(j = 0; j < len - 1; j++){
            if(a[j]>a[j+1]){
                int c = a[j];
                a[j] = a[j+1];
                a[j+1] = c;
            }
        }
    }
}

int main(){
    // Allowing user to create his array
    create_array();
    //Bubble sorting the array
    bubble_sorting();

    //checking the sorted array
    for(x=0; x < len; x++) {
        printf("%d ", a[x]);
    }

    // checking for duplicates in the array
    int noDu[5];
    for(l = 0; l < len - 1; l++){
        if(a[l]!=a[l+1]){
            scanf("%d",&noDu[l]);
        }else{
            continue;
        }
    }

    // for print out the array
    for(x=0; x < len; x++){
        printf("\n%d ",a[x]);
        printf("\n\n%d ",noDu[x]);
    }

    return 0;
}

