//
// Created by User on 8/1/2023.
//



#include <string.h>
#include <stdio.h>

int main(){
    //Code to compare two strings
    int flag = 0;
       char str1[50],str2[50],str3[101];
       printf("Enter string 1: ");
       gets(str1);
       printf("Enter string 2: ");
       gets(str2);
       int len1 = strlen(str1);
       int len2 = strlen(str2);
       int total_len = len1+len2;

    if (len1 != len2){
        printf("The strings are not the same");
    }
    else {
        for (int i=0;i<len1;i++){
            if (str1[i] != str2[i]){
                flag = 1;
                break;
            }
        }
        if (flag){
            printf("The strings are not the same");
        }else{
            printf("The strings are the same");
        }
    }
    return 0;
}