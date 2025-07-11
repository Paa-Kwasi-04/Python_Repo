#include <stdio.h>

int i, j, r, c;

int main() {
    printf("Enter the number of rows: ");
    scanf("%d", &r);
    printf("Enter the number of columns: ");
    scanf("%d", &c);
    int matrix[r][c];
    //Manually writing down my own 2D array
    int a[2][2] = {{1,2},{2,5}};

    // asking a user to make an array of any dimension
    for (j = 0; j < r; j++) {
        for (i = 0; i < c; i++) {
            printf("Enter elements for the matrix row %d column %d: ",j,i);
            scanf("%d", &matrix[j][i]);
        }
    }

    //Printing out the array to the individual
    for (int k = 0; k < r; k++) {
        printf("\n");
        for (int n = 0; n < c; n++) {
            //matrix[k][n] +=  matrix[k][n];
            printf("%d ", matrix[k][n]);
        }
    }

    for (int k = 0; k < r; k++) {
        printf("\n");
        for (int n = 0; n < c; n++) {
            printf("%d ", a[k][n]);
        }
    }

    //getting  a zero matrix
    int d[2][2] = {0};

    return 0;
}
