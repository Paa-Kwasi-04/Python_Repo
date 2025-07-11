#include <stdio.h>

int x, y;

int main() {

    printf("Enter a number:");
    scanf("%d", &x);
    printf("Enter another number:");
    scanf("%d", &y);

    printf("their sum is $d\n", y + x);
    printf("their differece is %d\n", x - y);
    printf("their product is %d", x * y);


    return 0;
}