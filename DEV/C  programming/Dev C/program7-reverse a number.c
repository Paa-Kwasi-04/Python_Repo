//
// Created by User on 6/20/2023.
//If a five-digit number is input through the keyboard, write a program to reverse the number.


#include <stdio.h>
#include <math.h>
//
//int main() {
//    int num, i, rem, sum = 0;
//
//    // ask  user for number
//    printf("Enter a eight digit number:");
//    scanf("%d", &num);
//
//
//    // reversing the number
//    for (i = 8; i > 0; --i) {
//        rem = num % 10;
//        num /= 10;
//        sum += pow(10, i) * rem;
//
//    }
//
//
//    printf("%d\n", sum/10);
//
//
//
//    return 0;
//}
// better of writing the same code
int main(){

        int n, reverse=0, rem;
        //asking for the number to be reversed
        printf("Enter a number: ");
        scanf("%d", &n);

        // reversing of a number
        while(n!=0)
        {
            rem=n%10;
            reverse=reverse*10+rem;
            n/=10;
        }


        printf("%d",reverse);

        return 0;
}