#include <stdio.h>

int main(){


int a[10];
int len  = sizeof(a)/sizeof(int);

for (int i = 0; i <len ; i++)
{
    if(i == 0){
        printf("Enter a number: ");
        scanf("%d",&a);
    }else{
        printf("Enter another number: ");
        scanf("%d",&a);
     }

}

    return 0;
}