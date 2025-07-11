//
// Created by User on 7/13/2023.
//
#include <stdio.h>

int main() {
    int i, j, c,k;
    int a[2][2] = {
            {1, 2},
            {2, 7}
    };
    int b[2][2] = {
            {5, 19},
            {3, 10}
    };

    printf("The Sum of Matrices");
    // Adding matrices
    for (j = 0; j < 2; j++) {
        printf("\n");
        for (i = 0; i < 2; i++) {
            c = a[j][i] + b[j][i];
            //printing out the sum
            printf("%d ", c);
        }
    }


    printf("\nThe Difference of Matrices");
    //subtracting matrices
    for (j = 0; j < 2; j++) {
        printf("\n");
        for (i = 0; i < 2; i++) {
            c = a[j][i] - b[j][i];
            //printing out the sum
            printf("%d ", c);
        }
    }


    //Multiplying matrices by factors
    printf("\nEnter factor to multiply matrix by: ");  scanf("%d",&k);
    printf("\nMultiplying  Matrices by factors of k");
    for (j = 0; j < 2; j++) {
        printf("\n");
        for (i = 0; i < 2; i++) {
            c = a[j][i] * k;
            //printing out the sum
            printf("%d ", c);
        }
    }




    return 0;
}