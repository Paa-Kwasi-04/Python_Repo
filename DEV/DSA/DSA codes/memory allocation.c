//
// Created by User on 9/14/2023.
//malloc() is used generally to allocate memory for structures and calloc for arrays
// the calloc actually allocates anumber fo blocks of the same type and returns the base address as a void pointer
// memory allocation always goes with poiters since the malloc function returns the address the of the memory allocated
//syntax is
// data type * ptr = NULL;
// ptr = (data type * )malloc(n * sizeof(int));
//syntax of calloc
// ptr = (data type *)calloc(n blocks,sizeof(int));
//syntax of realloc
// ptr = (data type*)realloc(pre ptr,n * sizeof(int))

#include "stdio.h"
#include "stdlib.h"

int main(){
    int *a;
    int n;
    printf("Enter size: ");
    scanf("%d",&n);
    a = (int *) malloc(n*sizeof (int));

    for(int i = 0;i<n;i++){
        scanf("%d",(a+i));
    }
    for(int i = 0;i<n;i++){
        printf("%5d",*(a+i));
    }



    return 0;
}