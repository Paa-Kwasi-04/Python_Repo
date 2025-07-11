//
// Created by User on 6/27/2023.
//WAP to search an element in a list of 10 element using Linear search.
#include <stdio.h>



int main() {

    int i, num, flag = 0;
    int roll_no[10] = {58, 152, 161, 90, 12, 14, 44, 57, 19};
    int len = sizeof(roll_no) / sizeof(int);
    printf("Enter a number: ");
    scanf("%d", &num);

    for (i = 0; i < len; i++) {
        if (num == roll_no[i]) {
            flag = 1;
            break;
        }
    }
    if (flag == 1) {
        printf("Roll number found\n");
    } else {
        printf("Roll number not found\n");
    }


    return 0;
}