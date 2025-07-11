//
// Created by User on 6/27/2023.
//

#include <stdio.h>


int main() {
    int i, j;
    int marks[12] = {215, 117, 19, 210, 24, 27, 303, 34, 15, 12, 6, 1};
    int len = sizeof(marks) / sizeof(int);


    for (i = 0; i < len; i++) {

        for (j = 0; j < len ; j++) {
            if (marks[j] < marks[j + 1]) {
                marks[j] = marks[j] + marks[j + 1];
                marks[j + 1] = marks[j] - marks[j + 1];
                marks[j] = marks[j] - marks[j + 1];
            }
        }
    }

    for (i = 0; i < len; i++) {
        printf("%d ", marks[i]);
    }


    return 0;
}

