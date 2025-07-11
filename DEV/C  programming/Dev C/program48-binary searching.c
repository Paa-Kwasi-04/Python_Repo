//
// Created by User on 6/27/2023.
//WAP to search an element in a list of 10 element using Binary search.

#include <stdio.h>

int main(){

    int i,j,k,key;
    int roll_no[9] = {58, 152, 161, 90, 12, 14, 44, 57, 19};
    int len = sizeof(roll_no) / sizeof(int);

    //bubble sorting the array
    for(i = 0;i < len;i++){
        //swapping the number which causes the sorting
        if(roll_no[i]>roll_no[i+1]){
            roll_no[i] = roll_no[i] + roll_no[i+1];
            roll_no[i+1] = roll_no[i]-roll_no[i+1];
            roll_no[i] = roll_no[i]-roll_no[i+1];
        }
    }

    //Performing binary search on array
    printf("Search for a number: "); scanf("%d",&key);
    int low = 0, high = len,mid,flag;
    for(j = 0;j<len;j++){
        for(k = 0;k>len-1;k++){
            mid = (high+low)/2;
            if(key == roll_no[mid]){
                flag =1;
                break;
            }else if(key > roll_no[mid]){
                low = mid+1;
                continue;
            }else{
                high = mid-1;
                continue;
            }

        }
    }

    if(flag==1){
        printf("Key found");
    }else {
        printf("Key not found");
    }

    return 0;
}
