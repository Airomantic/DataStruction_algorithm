//
// Created by 蒋宗青 on 2021/9/30.
//
/**
 * https://www.bilibili.com/video/BV17s411N78s?p=23
 */
#include "stdio.h"


void pointerArray_str();

void ArrayPointer();

/**
int型函数需要放在main()前面，void函数可以放在main()后面
 * 指针变量是一个lvalue左值，而数组名是一个地址常量，不是左值，所以不能用*str来作为指针移动，*(target++)必须是可改变的
指针数组: 是数组,每个数组存放一个指针变量 举例：int *p1[5]    数组下标[]比*的优先级要高
 数组指针：是指针，它指向一个数组  举例： int (*p2)[5]
 */
int test()
{
    char str[] = "I love Jiang";
    char *target = str; //个人理解：通过指针变量取得指向str第一个元素地址，即初始化赋予指向的能力
    int count = 0;
    while (*(target++) !='\0') //++的优先级大于*，其实*target++ 这样写也可
        {
        count++;
        }
    printf("共有字符%d\n", count);
}

int pointerArray()
{
    int a = 1;
    int b = 2;
    int c = 3;
    int d = 4;
    int e = 5;
    int *pt[5] = {&a, &b, &c, &d, &e};
    for (int i = 0; i < 5; i++) {
        printf("%d", *pt[i]);
    }
}
int main()
{
//    test();
//    pointerArray();
//    pointerArray_str();
    ArrayPointer();
    return 0;
}
/**
 * 同一个优先级里面
 */
void ArrayPointer() {
    int temp[5] = {1, 2, 3, 4, 5}; //注意数组一定记得[5]，没有[]就是set集合
    int (*pt2)[5] = &temp; //要的不是一个变量的地址，要的是一个真正的身份，把它当作一个整体，如果不加&也可以，只不过会有一个警告
    for (int i = 0; i < 5; i++) {
        printf("%d\n", *(*pt2 + i));//多取了一次，要多一个*
    }
}

void pointerArray_str() {

    char *pt[5]={
            "让编程改变世界",
            "jiang",
            "香港科技大学HKUST",
            "前进，前进，前进"
    };
    for (int i = 0; i < 5; i++) {
        printf("%s\n", pt[i]); //给出字符串的地址，打出字符串，加上*是打出字符，是单个数组元素的地址
    }
}
