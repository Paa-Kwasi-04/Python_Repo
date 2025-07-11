//
// Created by User on 6/22/2023.
//in binary searching you must sort first

#include <stdio.h>


int main() {
    int key, i;
    int marks[20] = {2, 4, 6, 8, 9, 12, 15, 18, 21, 25, 29, 33,
                     37, 41, 46, 51, 57, 64, 72, 80};


    printf("Please Enter a number");
    scanf("%d", &key);

    // binary search happens here
    int low = 0;
    int len_high = sizeof(marks) / sizeof(int); // very critical because it gives you the actual length of the array
    int high = len_high;
    int mid, flag = 0;

    for (i = 0; i < len_high; i++) {
        mid = (low + high) / 2;
        if (key == marks[mid]) {
            flag = 1;
            break;
        } else if (key > marks[mid]) {
            low = mid + 1;
            continue;
        } else {
            high = mid - 1;
            continue;
        }
    }

    if (flag == 1) {
        printf(" found %d", key);
    } else {
        printf(" %d not found ", key);
    }


    return 0;
}


















