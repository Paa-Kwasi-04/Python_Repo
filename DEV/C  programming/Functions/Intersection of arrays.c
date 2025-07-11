////TODO: something wrong with the interscetion
// Created by User on 7/4/2023.
//Given two integer arrays, write a C program to find the intersection
// of the two arrays (common elements) and store them in a new array.
#include <stdio.h>

int main(){
    int j,i,c[6];
    int a[6] = {2,4,7,3,9,5};
    int b[6] = {1,2,3,4,5,6};
    int na = sizeof(a)/sizeof(int);
    int nb = sizeof(b)/sizeof(int);

    //checking for intersection btn arrays
    for(j = 0; j < na; j++){
        for ( i = 0; i < nb; ++i) {
            if(a[j] == b[i]){
                c[i] = a[j];
            }
        }
    }

    for(int k = 0;k<6;k++){
        printf("%d",c[k]);
    }
    return 0;
}
