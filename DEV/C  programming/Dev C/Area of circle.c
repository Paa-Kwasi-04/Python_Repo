#include <stdio.h>

int r;
int main(){
    //ask the user for the radius of circle
    printf("Enter the circle's radius: ");scanf("%d",&r);
    double Area = 3.14 * r* r;

    //display play the area to user
    printf("the area of the circle is :%.2f",Area);

    return 0;
}