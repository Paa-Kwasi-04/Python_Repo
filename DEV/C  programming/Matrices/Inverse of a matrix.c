//
// Created by User on 7/20/2023.
//inverse is for only square matrices with a non-zero integer determinant
#include "stdio.h"


int main() {
    int i, j, r, c;
    printf("Enter the number of rows: ");
    scanf("%d", &r);
    printf("Enter the number of columns: ");
    scanf("%d", &c);
    int a[r][c];

    // asking a user to make an array of any dimension
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            printf("Enter element for a[%d][%d]: ", j, i);
            scanf("%d", &a[i][j]);
        }
    }

    //this is here the Det magic begins
    int det = 0;

    for (j = 0; j < 3; ++j) {
        det += a[0][j] *
               (a[1][(j + 1) % 3] * a[2][(j + 2) % 3] - a[2][(j + 1) % 3] * a[1][(j + 2) % 3]);
    }


    printf("Determinant: %d", det);

    //getting the cofactors of the matrix and transposing it straight away
    int d[3][3];
    printf("\nThe Inverse is: ");
    for (i = 0; i < r; i++) {
        printf("\n");
        for (j= 0; j < c; j++) {
            d[i][j]=0;
            //finds co factors and transposes it at once
           d[i][j] = (a[(j+1)%3][(i+1)%3]*a[(j+2)%3][(i+2)%3])-(a[(j+1)%3][(i+2)%3]*a[(j+2)%3][(i+1)%3]);
           //getting the inverse
            printf("%5d",d[i][j]/det);
        }
    }






























































    

    return 0;
}
