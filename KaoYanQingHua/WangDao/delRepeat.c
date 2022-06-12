//
// Created by 蒋宗青 on 2021/10/18.
//
#include "stdio.h"
///有序表中，删除所有重复的字母


int delRepeat(int *arr, int len);

int main()
{
    int arr[] = {1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7};
    int len = sizeof(arr) / sizeof(int);
    len = delRepeat(arr, len);
    for (int i=0;i<len;i++)
    {
        printf("%d", arr[i]);
    }
    return 0;
}

int delRepeat(int *arr, int len) {
    int k = 0;
    for (int i = 0;i <len;i++)
    {
        if (*(arr + i) - *(arr + i + 1)) //如果差值不为0，即不相同
        {
            *(arr + k++) = *(arr + i);// k做为一个指针操作
        }
        /// 相同的话，就不用进行k++，直接跳过，不用赋值
    }
    //可能性很小
    if(*(arr + len -1)==*(arr + len)) //如果最后一个元素恰好和后一个存储空间元素相等，则需要单独处理
    {
        *(arr + k++) = *(arr + len - 1);
    }
    return k;
}
