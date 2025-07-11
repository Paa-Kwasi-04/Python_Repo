//
// Created by User on 7/6/2023.
//
#include <stdio.h>

int main(){
    int n,i,j,large,s_large,k;
    printf("Enter number of elements in the array: ");
    scanf("%d",&n);
    int a[n];

    // getting elements in the array
    for(i = 0;i<n;i++){
        printf("Enter any number: ");
        scanf("%d", &a[i]);
    }

    //getting the largest element in the array
    large = a[0];
    for (j = 0; j < n; ++j) {
        // in each iteration checks to see if the element is greater than large
        if(a[j]>large){
//          s_large = large;
            large = a[j];
        }
    }
    printf("%d\n",large);
    // getting the second largest in the array
    s_large = 0;
    for (k = 0; k < n; ++k) {
        // checks to see if elements in the array are larger than s_large but not equal to large
        if(a[k]>s_large && a[k] != large){
            s_large = a[k];
        }
    }

    //displaying the second-largest number
    printf("the Second Largest number: %d",s_large);
    return 0;
}
