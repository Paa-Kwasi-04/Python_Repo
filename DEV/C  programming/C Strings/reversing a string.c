//
// Created by User on 8/1/2023.
//
#include "string.h"
#include "stdio.h"


int main(){
    // Code to reverse a string
    char string[50];
    printf("Enter the string to reverse: ");
    gets(string);
    char rev_str[50];
    //printf("The reversed string is: ");
    int len = strlen(string);
    int i = len-1,j=0;
    while (i >=0) {
        //printf("%c",string[i]);
        rev_str[j] = string[i];
        i--;
        j++;
    }printf("The reversed string is %s",rev_str);

    /* Another way to reverse a string
  int len = strlen(string);
  int i=0,j=len-1;
  while (j>i){
      string[i] += string[j];
      string[j] = string[i] - string[j];
      string[i] -= string[j];
      i++;
      j--;
  }
  printf("The reversed string is %s",string);
   */


    return 0;
}
