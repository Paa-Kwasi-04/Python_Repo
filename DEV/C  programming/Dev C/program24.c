//
// Created by User on 6/21/2023.
// WAP to add 10 numbers using for statement.

#include <stdio.h>
#include <conio.h>

int main() {
    int i, sum = 0, num;

    // use a for loop to ask the user for inputs and add as well
    for (i = 0; i < 10; i++) {
        if (i == 0) {
            printf("Enter any number:");
        } else if(i == 9) {
            printf("Enter last number:");
        }else{
            printf("Enter another number:");
        }

        scanf("%d", &num);
        // Adding the numbers being inputted
        sum += num;

    }
    printf("The sum of the ten numbers inputted are....\n");
    getch();
    printf("%d", sum);
    return 0;
}
