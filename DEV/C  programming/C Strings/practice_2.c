//
// Created by User on 7/25/2023.
//reversing strings
#include "stdio.h"


int main() {
    int i;
    char str1[5][20];
     for(i = 0;i<2;i++){
         printf("Enter the names of students present: ");
         scanf("%s",&str1[i]);
     }

    for (i = 0;i<5;i++) {
        printf("%s\n",str1[i]);
    }



    return 0;
}
