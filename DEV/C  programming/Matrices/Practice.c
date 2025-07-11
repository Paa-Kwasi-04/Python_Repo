//
// Created by User on 7/20/2023.
//
#include "stdio.h"


int main(){
    int r,c,i,j,k,Ta[3][3],Tb[3][3];
    //ASk user to enter an array
    printf("Enter number of  rows: ");       scanf("%d",&r);
    printf("Enter number of columns: ");       scanf("%d",&c);
    int a[r][c],b[r][c];

    //matrix A creation
    for(j = 0;j<r;j++){
        for(i=0;i<c;i++){
            printf("Enter element for a[%d][%d]: ",j,i);
            scanf("%d",&a[j][i]);
        }
    }
    //matrix B creation
    for(j = 0;j<r;j++){
        for(i=0;i<c;i++){
            printf("Enter element for b[%d][%d]: ",j,i);
            scanf("%d",&b[j][i]);
        }
    }
    int d[3][3] = {0};

    // Multiplying AB
    for(j = 0;j<r;j++){
        for(i=0;i<c;i++){
            for(k = 0;k<3;k++){
              d[j][i] += a[j][k]*b[k][i];
            }
        }
    }
    //Printing AB
    printf("\n\n AB =");
    for( j  =0;j<r;j++) {
        printf("\n");
        for (i = 0; i < c; i++) {
            printf("%d\t", d[j][i]);
        }
    }
    //Multiplying BA
    int e[3][3] = {0};
    for(j = 0;j<r;j++){
        for(i=0;i<c;i++){
            for(k = 0;k<3;k++){
                e[j][i] += b[j][k]*a[k][i];
            }
        }
    }
    //Printing BA
    printf("\n\n BA =");
    for( j  =0;j<r;j++){
        printf("\n");
        for( i = 0;i<c;i++){
            printf("%d\t",e[j][i]);
        }
    }

    //get the determinant A
    int A = 0;
    for(j=0;j<3;j++){
        A  += a[0][j] * (a[1][(j+1)%3]*a[2][(j+2)%3] - a[2][(j+1)%3]*a[1][(j+2)%3]);
    }
    printf("\n\n|A| = %d",A);

    //get the determinant B
    int B = 0;
    for(j=0;j<3;j++){
        B  += b[0][j] * (b[1][(j+1)%3]*b[2][(j+2)%3] - b[2][(j+1)%3]*b[1][(j+2)%3]);
    }
            printf("\n|B| = %d",B);

    //Transpose of A
    for(j = 0;j<r;j++){
        for(i=0;i<c;i++){
            Ta[i][j]  = a[j][i];
        }
    }
    printf("\n\nA Transpose: ");
    for( j  =0;j<r;j++){
        printf("\n");
        for( i = 0;i<c;i++){
            printf("%d\t",Ta[j][i]);
        }
    }

    //Transpose of B
    for(j = 0;j<r;j++){
        for(i=0;i<c;i++){
            Tb[i][j]  = b[j][i];
        }
    }
    printf("\n\nB Transpose: ");
    for( j  =0;j<r;j++){
        printf("\n");
        for( i = 0;i<c;i++){
            printf("%d\t",Tb[j][i]);
        }
    }





    return 0;
}
