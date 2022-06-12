//
// Created by 蒋宗青 on 2021/10/17.
//
#include <stdlib.h>
#include "stdio.h"
/// i位置换到 len -(i+1)



void reverseS(int *arr, int n);

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
    reverseS(arr, n);
    for (int i = 0; i < n ; i++) {
        printf("%d", *(arr + i)); //或arr[i]
    }
}

void reverseS(int *arr, int len) {
    int temp;
    for (int i = 0; i < len / 2; i++)
    {
        temp = *(arr + i);
        *(arr + i) = *(arr + len - i - 1);
        *(arr + len - i - 1) = temp;
    }
}
