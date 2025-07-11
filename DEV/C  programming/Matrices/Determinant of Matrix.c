//
// Created by User on 7/18/2023.
//
//All you need to know for the  determinant is the position of


#include "stdio.h"


int main() {
    int i, j, r, c;
    printf("Enter the number of rows: ");
    scanf("%d", &r);
    printf("Enter the number of columns: ");
    scanf("%d", &c);
    int a[r][c];

    // asking a user to make an array of any dimension
    for (j = 0; j < r; j++) {
        for (i = 0; i < c; i++) {
            printf("Enter element for a[%d][%d]: ", j, i);
            scanf("%d", &a[j][i]);
        }
    }

    //this is here the Det magic begins
    int det = 0,x = 0;

    for (j = 0; j < 3; ++j) {
        det += a[x][j] *
               (a[x + 1][(j + 1) % 3] * a[x + 2][(j + 2) % 3] - a[x + 2][(j + 1) % 3] * a[x + 1][(j + 2) % 3]);
    }


    printf("Determinant: %d", det);


    return 0;
}