//
// Created by User on 6/29/2023.
//creating functions below or above main but above is recommended
// use pointers '*' when you actually want to change something
// check sum of an array is just to add the elements in the array


#include <stdio.h>
int marks[12] = {215, 117, 19, 210, 24, 27, 303, 34, 15, 12, 6, 1};


void swap_3(int *val_1,int *val_2){
    int c = *val_1;
    *val_1 = *val_2;
    *val_2 = c;
}

void bubble_sorting(int len, int arr[]){
    int i,j;
    // doing the bubble sorting
    for (i = 0; i < len; i++) {

        for (j = 0; j < len - 1; j++) {
            // swapping the values of the variables
            if (arr[j] > arr[j + 1]) {
                swap_3(&arr[j],&arr[j+1]);
            }
        }
    }
}


int main() {
    int key, l;

    // getting the length of the array
    int len = sizeof(marks) / sizeof(int);

    // Asking the user to search for a number in the array
    printf("Search for a number: ");    scanf("%d", &key);

    bubble_sorting(len,marks);

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


