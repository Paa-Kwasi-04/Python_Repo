#include <stdio.h>


int age;
char name[30];
int main(){
  //Enter your age
  printf("Enter your name: ");fgets(name,sizeof(name),stdin);
  printf("Enter your age: ");scanf("%d",&age);

  //Check if you can vote
  if(age>=18){printf("%s you are eligible to vote",name);}
  else{printf("Come back when you are 18yrs and above");}


  return 0;
}