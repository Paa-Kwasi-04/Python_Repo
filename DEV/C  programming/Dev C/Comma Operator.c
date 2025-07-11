#include <stdio.h>

int main(){
    int a= 2, b = 3;
// the comma operator does the left operation first then forget it to do the second expression
    int result = (a++,b+=a);

    printf("%d",result);


    return 0;
}