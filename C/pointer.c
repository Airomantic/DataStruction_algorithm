//
// Created by 蒋宗青 on 2021/9/30.
//

#include "stdio.h"
/**
取址运算符&
取值运算符：访问指针变量指向的数据
 */
int main() {
    char a = 'F';
    int i = 123;
    ///取址运算符&，注意避免访问未初始化的指针
    char *pa = &a ;
    int *pb = &i;
    ///取值运算符：访问指针变量指向的数据
    printf("c=%c\n",*pa);
    printf("i=%d\n",*pb);

    *pa = 'C';
    *pb +=1;
    printf("now,c=%c\n",*pa);
    printf("now,i=%d\n",*pb);
    ///查看指针占用字节数量，32bit和64bit的电脑不一样
    printf("sizeof pa =%d\n",sizeof(pa));
    printf("sizeof pb =%d\n",sizeof(pb));
    ///打印地址
    printf("the address a is %p\n",pa);
    printf("the address i is %p\n",pb);
}