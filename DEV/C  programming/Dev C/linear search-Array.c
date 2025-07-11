//
// Created by User on 6/20/2023.
//types of searches in arrays
// linear and binary search
#include <stdio.h>

int main() {
    int num;
    int i;
    int roll_no[9] = {58, 152, 161, 90, 12, 14, 44, 57, 19};
    int len_arr = sizeof(roll_no) / sizeof(int);

    printf("Enter the last three digits of your roll number: ");
    scanf("%d", &num);

    int flag = 0;

    for (i = 0; i < len_arr; i++) {
        if (num == roll_no[i]) {
            flag = 1;
            break;
        }
    }

    if (flag) {
        printf("You are enrolled in the course");
    } else {
        printf("you are not enrolled in the course");
    }


    return 0;
}