// Problem: Write a function that takes two integers as parameters and returns their sum.




#include <stdio.h>
int sum(float y, float x){
    return y + x;
}

int main() {
    int a,b;
    printf("Enter a number: ");
    scanf("%d",&a);

    printf("Enter a number: ");
    scanf("%d",&b);

    printf("Sum : %d",sum(a,b));

    return 0;
}
