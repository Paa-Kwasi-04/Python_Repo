//
// Created by User on 8/25/2023.
//here we are using the long division method to get the HCF of set of numbers
# include "stdio.h"

// this a recursive functions
int HCF(int a , int b){
    if(b== 0){
        return a ;
    }else{
       return  HCF(b, a % b);
    }
}

int main(){
    int num1,num2;
    printf("Enter the first number:");
    scanf("%d",&num1);
    printf("Enter the second number: ");
    scanf("%d",&num2);

    int x = HCF(num1, num2);
    printf("the HCF is : %d",x);



    return 0;
}