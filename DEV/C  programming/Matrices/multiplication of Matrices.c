//
// Created by User on 7/13/2023.
//line 49 to 59 is here the multiplication begins
#include "stdio.h"


int main() {
    int a[3][3], b[3][3], i, j, k, r, c;
    printf("Enter the number of rows: ");
    scanf("%d", &r);
    printf("Enter the number of columns: ");
    scanf("%d", &c);

    //getting the matrix A
    for (j = 0; j < r; j++) {
        for (i = 0; i < c; i++) {
            printf("a[%d][%d]: ", j, i);
            scanf("%d", &a[j][i]);
        }
    }

    //getting the matrix B
    for (j = 0; j < r; j++) {
        for (i = 0; i < c; i++) {
            printf("b[%d][%d]: ", j, i);
            scanf("%d", &b[j][i]);
        }
    }


    // Printing the matrix A
    printf("Matrix A");
    for (j = 0; j < 2; j++) {
        printf("\n");
        for (i = 0; i < 2; i++) {
            printf("%d ", a[j][i]);
        }
    }

    // Printing the matrix B
    printf("\nMatrix B");
    for (j = 0; j < 2; j++) {
        printf("\n");
        for (i = 0; i < 2; i++) {
            printf("%d ", b[j][i]);
        }
    }

    //defining a zero matrix to reference when adding
    int d[3][3] = {0};

    //where the multiplication magic begins
    for (j = 0; j < r; j++) {
        for (i = 0; i < c; i++) {
            for (k = 0; k < 3; k++) {
                d[j][i] += a[j][k] * b[k][i];
            }
        }
    }

    //Displaying the product
    for (j = 0; j < r; j++) {
        printf("\n");
        for (i = 0; i < c; i++) {
            printf("%d\t", d[j][i]);
        }
    }


    return 0;
}



