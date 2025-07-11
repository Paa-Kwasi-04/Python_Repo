//
// Created by User on 11/15/2023.
//
#include "stdio.h"

int main(){
    int a[7] = {1,2,3,4,5,6,7},i,key,n = 7;

    //prompt for searching for values in the array
    printf("Enter Value to search for: ");
    scanf("%d",&key);

    int low = 0, high = n,mid,flag = 0;

    //Where the binary search magic begins
    for(i = 0; i < 7;i++){

        mid = (high+low)/2;

        if(a[mid] == key){
            flag = 1;
            break;
        }else if(a[mid] < key){
            low = mid+1;
            continue;
        }else{
            high = mid-1;
        }
    }

    if(flag == 1){
        printf("Value found");
    }else{
        printf("Not found");
    }








    return 0;
}