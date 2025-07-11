//
// Created by User on 7/2/2023.
//Implement a C program to calculate the average of all the elements in an integer array.
#include <stdio.h>
int i, j, sum = 0;
float ave;
int a[5];
int len = sizeof(a) / sizeof(int);

// function for creating user array
void create_array(){
    for (i = 0; i < len; i++) {
        if (i == 0) {
            printf("Enter a number: ");
        } else {
            printf("Enter another number: ");
        }
        scanf("%d", &a[i]);
    }

}
int main() {

    // Allowing user to create his array
    create_array();

    // sum of elements in an array
    for (j = 0; j < len; j++) {
        sum += a[j];
    }

    ave = (float) sum / (float) len;
    printf("The Sum: %d\tThe Average: %.2f", sum, ave);


    return 0;
}



