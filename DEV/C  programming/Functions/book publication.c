#include "stdio.h"



int main(){
    int i = 0,count = 0;
    char str1[60];
    printf("Enter any string: ");
    gets(str1);


    //length of string
    while(str1[i] != '\0'){
        if( ('a'<= str1[i] && 'z'>= str1[i])  ||('A'<= str1[i] && 'Z'>= str1[i])  ){
            count++;
        }

        i++;
    }

    printf("%d",count);

    return 0;
}






















