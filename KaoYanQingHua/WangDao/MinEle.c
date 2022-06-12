//
// Created by 蒋宗青 on 2021/10/15.
//
#include <stdlib.h>
#include "stdio.h"
void delMin(int *arr,int len){
    if(!len)
    {
        printf("数组为空");
        return;
    }
    int min = *arr; //数组的地址默认放在数组第一位元素，既下标为0的位置
    int minPos = 0;
    for (int i = 0; i < len; i++) {
        if (min > *(arr + i)) //* 表示值，arr + i相当于arr[index]下标index
        {
            min = *(arr + i);
            minPos = i;
        }
    }
    *(arr + minPos) = *(arr + len - 1);
    *(arr + len - 1) = NULL;

}

int main()
{
    int n;
    printf("请输入数组长度：");
    scanf("%d", &n);
    int *arr = (int *) malloc(sizeof(n)); //动态分配数组
    printf("请输入数组的元素：");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", arr + i);
    }
    delMin(arr, n);
    for (int i = 0; i < n - 1; i++) {
        printf("%d", *(arr + i)); //或arr[i]
    }
}