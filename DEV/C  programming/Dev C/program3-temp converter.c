#include <stdio.h>

double F, C;

int main(){
//ask for a temp in Fahrenheit 
printf("Enter any Fahrenheit  temperature:  ");
scanf("%lf", &F);

// convert to Celsius by (F-32)*5/9
C = (double)((F-32)*5/9);
printf("the equivalent Celsius temperature is %lf", C);


  return 0;
}