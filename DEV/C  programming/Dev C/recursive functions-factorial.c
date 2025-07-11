//
// Created by User on 6/29/2023.
//recursive functions are like functions calling themselves

#include <stdio.h>

int fact(int n);


int main(){
    int val,num;
    printf("Enter a number: ");
    scanf("%d",&num);

    val = fact(num);
    printf("\n Factorial is : %d",val);
    return 0;
}


int fact(int n){
    if(n<0)
        return 0;
    else if(n == 0)
        return 1;
    else{
        return (n* fact(n-1));
    }
}