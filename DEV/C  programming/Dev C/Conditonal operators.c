#include <stdio.h>


int a,b,c,large;
int main() {
    printf("Enter a: ");scanf("%d",&a);
    printf("Enter b: ");scanf("%d",&b);
    printf("Enter c: ");scanf("%d",&c);

    large = (a>b)?((a>b)?a:c):((b>c)?b:c);
    printf("the largest Number is: %d",large);
    return 0;
}
