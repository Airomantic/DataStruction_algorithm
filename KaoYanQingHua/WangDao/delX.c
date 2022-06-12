//
// Created by 蒋宗青 on 2021/10/17.
//

#include "stdio.h"

void delX(int *arr, int len, int x) {
    int k = 0, i = 0;
    while (len > i) { //这里不用用for
        if (*(arr + i) == x) {
            k++; // 或者 k =1时 ++k
        } else {
            *(arr + i - k) = *(arr + i);
        }
        i++;
    }
    //善尾工作
    for (int i = len - k; i < len; i++) {
        *(arr + i) = NULL;
    }
    for (int i = 0; i < len - k; i++) {
        printf("%d", arr[i]);
    }
}

int main() {
    int arr[] = {3, 2, 4, 2, 5, 2, 9, 20, 1, 2}, x; //注意这里有个20是不能被删除的
    int len = sizeof(arr) / sizeof(int);
    scanf("%d", &x);
    delX(arr, len, x);
    return 0;
}

