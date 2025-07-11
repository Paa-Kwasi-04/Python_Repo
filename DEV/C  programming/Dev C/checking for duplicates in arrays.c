//
// Created by User on 7/6/2023.
//
#include <stdio.h>


int main() {
    int i,j,n,flag = 0 ;
    printf("Enter number of elements in the array: ");
    scanf("%d", &n);
    int a[n];

    for (i = 0; i < n; i++) {
        printf("Enter any number: ");
        scanf("%d", &a[i]);
    }

    for(j = 0;j<n;j++){
        for(i = j+1;i<n;i++){
            if(a[j] ==a[i]){
                flag = 1;
            }
        }
    }

    if(flag == 1){
        printf("duplicates found");
    }else{
        printf("No duplicates found");
    }

    return 0;
}












