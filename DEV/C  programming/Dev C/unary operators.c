// post and prefix does not really matter until it is being assigned to a variable
//the unary operators involves the increment and decrement operators

#include <stdio.h>


int a,b,c,d,e;

int main(){
    a = -5;
    b = ++a;
    c = a++ + b--;
    d = ++a + --b + c++;
    e = ++a + --b + c++ + --d;

    printf("the value of a now is%d\n",a);
    printf("the value of b now is%d\n",b);
    printf("the value of c now is%d\n",c);
    printf("the value of d now is%d\n",d);
    printf("the value of e now is%d",e);



    return 0;
}