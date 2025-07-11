//
// Created by User on 9/8/2023.
//
#include "stdio.h"

char names[11],key;
int i,low = 0,mid,high = 11,flag = 0;

int binary(){
    high--;
    for(i = 0;i<11;i++){
        mid = (high+low)/2;
        if(names[mid] == key ){
            flag = 1;
            break;
        }else if(names[mid] > key){
            low = mid + 1;
            continue;
        }else{
            high = mid - 1;
        }
    }if(flag ==  1){
        printf("found");
    }else{
        printf("Not found");
    }

}

int main(){

    // Getting the names of bank clients
    for(i = 0;i<11;i++){
    printf("Enter the names: ");
    scanf("%s",names[i]);
    }

    // Printing out the list
    for(i = 0;i<11;i++){
        printf("%s",names[i]);
    }





















    return 0 ;
}