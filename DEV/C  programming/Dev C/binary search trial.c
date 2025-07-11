//
// Created by User on 6/27/2023.
//
#include <stdio.h>

int main() {
    int key, i;
    int marks[20] = {2, 4, 6, 8, 9, 12, 15, 18, 21, 25, 29, 33,
                     37, 41, 46, 51, 57, 64, 72, 80};

    printf("Enter your Roll number:");
    scanf("%d", &key);

    // binary search begins here
    int low = 0;
    int len = sizeof(marks) / sizeof(int);
    int high = len;
    int mid, flag = 0;

    for (i = 0; i < len; i++) {
        mid = (high + low) / 2;
        if (key == marks[mid]) {
            flag = 1;
            break;
        } else if (key < marks[mid]) {
            high = mid -1;
            continue;
        } else {
            low = mid + 1;
            continue;
        }

    }
    if(flag){
        printf("Your roll number %d was found",key);
    }else{
        printf("Can't find your roll number");
    }


    return 0;
}