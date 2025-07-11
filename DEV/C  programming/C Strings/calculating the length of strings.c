#include <stdio.h>



int main() {
    char str[100] ;
    printf("Enter a string\n");
    gets(str);  // acts like scanf but used for strings
    int i = 0;

    //this is where the characters including white space and full-stop are included
    while(str[i] != '\0' ){
        i++;
    }

    printf("\n The length of the string is: %d",i);


    return 0;
}
;