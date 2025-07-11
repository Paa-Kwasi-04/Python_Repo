#include "stdio.h"
#include "stdlib.h"

int* bubble_sort(int *a,int n){
    int i,j;
    for(i = 0;i <n-1;i++){
        int flag = 0;
        for(j = 0;j<n;j++){
            if(a[j]>a[j+1]){
                a[j] = a[j+1]+a[j];
                a[j+1] = a[j]-a[j+1];
                a[j]= a[j]-a[j+1];
                flag = 1;
            }
        }if(flag == 0){
            break;
        }
    }
    return a;
}
void primitive_insertion(int a[]){
    int n,i,j;
    for(i = 0;i<n;i++){
        j = i;
        while(j>=0 && a[j] < a[j-1]){
            int temp = a[j-1];
            a[j-1] = a[j];
            a[j] = temp;
            j--;
        }
    }
}
int* insertion_sort(int *a,int n){
    int i,j;
    for(i = 0;i<n;i++){
        int temp = a[i];
        j = i-1;
        while(j>=0 && a[j] > temp){
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = temp;
    }
    return a;
}

int* selection_sort(int*a,int n){
    int i,j;
    int min;
    for(i = 0;i<n-1;i++){
        int temp = a[i];
        min = i;
        j = i+1;
        while(j<n){
            if(a[j]< a[min]){
                min = j;
            }
            j++;
        }
        if(min != i){
            a[i] = a[min];
            a[min] = temp;
        }
    }
    return a;
}

int* merge(int*a,int lb,int mid,int ub){
    int k,i,j,*b;
    i = lb;
    j = mid+1;
    k = lb;

    while (i<= mid && j<= ub){
        if(a[i] <= a[j]){
           b[k] = a[i];
           i++;
        }else{
            b[k] = a[j];
            j++;
        }k++;
    }
    if(i>mid){
        while (j<= ub){
            b[k] = a[j];
            j++; k++;
        }
    }else{
        while(i<= mid){
            b[k] = a[i];
            i++;k++;
        }
    }


}


int main(){
    int n,i,j;
    printf("Enter the number of array elements: ");
    scanf("%d",&n);
    int *a = calloc(n,sizeof(int));


    for(i = 0;i<n;i++){
        printf("Enter a[%d]",i);
        scanf("%d",&a[i]);
    }

    a = selection_sort(a,n);

    for(i = 0;i<n;i++){
        printf("%d\t",a[i]);
    }


    return 0;
}