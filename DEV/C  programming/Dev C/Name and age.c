#include <stdio.h>

char name[30];
int age;

int main() {
// ask the user for name and age and print it out
    // username input
    printf("what is your name?\t");
    fgets(name, sizeof(name), stdin);
    // user age input
    printf("how old are you?");
    scanf("\t%d", &age);

// out the message with the user's name and age
    printf("hello %s you are %d years old", name, age);


    return 0;
}