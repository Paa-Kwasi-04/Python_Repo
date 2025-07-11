//
// Created by User on 11/21/2023.

#include "stdio.h"
#include "stdlib.h"

void merge(int L[], int R[], int *A,int mid,int n)
{
    int i,j,k;
    i = j = k =  0;
    while(i< mid && j< n){
        if(L[i]<R[j]){
            A[k] = L[i];
            i++;
        }else{
            A[k] = R[j];
            j++;
        }k++;
    }
    while(i< mid){
        A[k] = L[i];
        i++; k++;
    }
    while(j< n){
        A[k] = R[j];
        j++; k++;
    }


}


void MergeSort(int* A,int n)
{
    if(n <= 1){
        return ;
    }
    int mid = n/2,i;
    int m = n-mid;
    int LHA[mid], RHA[m];

    //copying the LHS elements to the left subarray
    for( i = 0;i<mid;i++){
        LHA[i] = A[i];
    }
    //copying the RHS elements to the right subarray
    for( i = mid;i<n;i++){
        RHA[i] = A[i];
    }
    MergeSort(LHA,mid);
    MergeSort(RHA,m);
    merge(LHA,RHA,A,mid,n);
}


int main(){
    int n,i;
    printf("Enter the number of array elements: ");
    scanf("%d",&n);
    int *a = calloc(n,sizeof(int));

    for(i = 0;i<n;i++){
        printf("Enter a[%d]: ",i);
        scanf("%d",&a[i]);
    }

    MergeSort(a,n);

    for(i = 0;i<n;i++){
        printf("%d\t",a[i]);
    }


    return 0;
}