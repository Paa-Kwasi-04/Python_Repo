// Created by User on 6/27/2023.
// performing a bubble sort and  binary search on an unsorted list


#include <stdio.h>

int main() {
    int i, j, key, l;
    int marks[12] = {215, 117, 19, 210, 24, 27, 303, 34, 15, 12, 6, 1};
    // getting the length of the array
    int len = sizeof(marks) / sizeof(int);

    // doing the bubble sorting
    for (i = 0; i < len; i++) {

        for (j = 0; j < len - 1; j++) {
            // swapping the values of the variables
            if (marks[j] > marks[j + 1]) {
                marks[j] = marks[j] + marks[j + 1];
                marks[j + 1] = marks[j] - marks[j + 1];
                marks[j] = marks[j] - marks[j + 1];
            }
        }
    }
    // Asking the user to search for a number in the array
    printf("Search for a number: ");    scanf("%d", &key);

    int low = 0;
    int high = len;
    int mid,flag = 0;

    // The binary search algorithm
    for (l = 0; l < len; l++) {
        mid = (high + low)/2;
        if (key == marks[mid]) {
            flag = 1;
            break;
        }else if(key>marks[mid]){
            low = mid + 1;
            continue;
        }else{
            high = mid -1;
            continue;
        }
    }

    // verifies to user if the number inputted is in array
    if(flag){
        printf("the number %d is found",key);
    }else{
        printf("the number %d wasn't found ",key);
    }

    return 0;
}