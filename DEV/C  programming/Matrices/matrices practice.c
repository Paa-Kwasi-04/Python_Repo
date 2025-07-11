//
// Created by User on 7/25/2023.
//
#include "stdio.h"


int main(){
    int a[3][3],b[3][3];
    int i ,j;

    //creating our matrix with user input
    for(i = 0;i<3;i++){
        for(j = 0;j<3;j++){
            printf("Enter element a[%d][%d]: ",i,j);
            scanf("%d", &a[i][j]);
        }
    }
    for(i = 0;i<3;i++){
        for(j = 0;j<3;j++){
            printf("Enter element b[%d][%d]: ",i,j);
            scanf("%d", &b[i][j]);
        }
    }

    //multiplication of matrices
//    int c[3][3];
//    for(i = 0;i<3;i++){
//        for(j = 0;j<3;j++){
//            c[i][j] = 0;
//            for(int k = 0;k<3;k++){
//               c[i][j] += a[i][k]*b[k][j];
//            }
//        }
//    }
//
//    for(i = 0;i<3;i++){
//        printf("\n");
//        for(j = 0;j<3;j++){
//            printf("%3d",c[i][j]);
//        }
//    }

//determinant of a matrix
int d = 0;
for(j=0;j<3;j++){
   d +=a[0][j]*(a[1][(j+1)%3]*a[2][(j+2)%3] - a[2][(j+1)%3]*a[1][(j+2)%3]);
}

    return 0;
}















