#include <stdio.h>

// syntax of conditionals
// if(x){
// printf();
// }else if(){
// printf();
// }else{
// printf();
// }
int main(){
////Get integer from user

    int num,r;

    printf("Enter any number:");
    scanf("%d", &num);
////check if it is even or odd
//    r = num % 2;
//    if (r == 0){ printf("%d is Even", num);}
//    else {
//        printf("%d is odd", num);
//    }

    printf("the number %d is %s",num,(num % 2? "odd":"Even"));

    return 0;
}