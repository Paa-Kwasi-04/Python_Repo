#include <stdio.h>

int a,b,c;
int main(){
printf("Enter value of a: ");scanf("%d",&a);
printf("Enter value of b: ");scanf("%d",&b);
printf("Enter value of c: ");scanf("%d",&c);

if((a>b)>c){
  printf("%d is the max value of the three no",a);
}else if (b>a>c){
  printf("%d is the max value of the three no",b);
}



  return 0;
}