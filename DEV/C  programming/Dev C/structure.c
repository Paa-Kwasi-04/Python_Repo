//
// Created by User on 8/25/2023.
//
#include <stdio.h>


// Define the structure
typedef struct student {
    char name[50];
    int rollNumber;
    float marks;
}S;

int main() {
    // Declare an array of 30 students
    S students[5];

    // Populate the array with data
    for (int i = 0; i < 5; ++i) {
        printf("Enter details for student %d:\n", i + 1);

        printf("Name: ");
        scanf("%s", students[i].name);

        printf("Roll Number: ");
        scanf("%d", &students[i].rollNumber);

        printf("Marks: ");
        scanf("%f", &students[i].marks);
    }

    // Display the entered data
    printf("\nStudent Details:\n");
    for (int i = 0; i < 5; ++i) {
        printf("Student %d\n", i + 1);
        printf("Name: %s\n", students[i].name);
        printf("Roll Number: %d\n", students[i].rollNumber);
        printf("Marks: %.2f\n", students[i].marks);
        printf("\n");
    }

    return 0;
}
