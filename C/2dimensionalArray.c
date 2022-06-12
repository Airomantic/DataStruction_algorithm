//
// Created by 蒋宗青 on 2021/9/30.
//
/**
* C语言事实上没有真正意义上的二维数组，二维数组的实现是简单通过的线性扩展方式实现的
语法糖：*(array+1) == array[1]，对于一门编程语言来说，它没有增加一门新的技能，而是通过增加一个语法方便程序员的使用，一种写法另一种形式
 https://www.bilibili.com/video/BV17s411N78s?p=24
*/

#include "stdio.h"

void test1();

void test2();

void test3();

int main()
{
//    test1();
//    test2();
    test3();
}

void test3() {
    int array[2][3] = {{0, 1, 2},
                       {3, 4, 5}};
    int (*p)[3] = array;

    printf("**(p+1): %d\n ", **(p + 1));
    printf("**(array+1):%d\n", **(array + 1));
    printf("array[1][0]:%d\n", array[1][0]);
    printf("*(*(p+1)+2): %d\n", *(*(p + 1) + 2));
    printf("*(*(array+1)+2): %d\n", *(*(array + 1) + 2));
    printf("array[1][2]: %d\n", array[1][2]);

}

/**
形式转换； *(array+i) == array[i] ，*(*(array+i)+j) == array[i][j] ,*(*(*(array+i)+j)+k) == array[i][j][k]
又一个语法糖: *(array+1)+3 == &array[1][3]
定义数组可以省略
 int array[2][3] = {{0,1,2},{3,4,5}} 只能是省略行（第一个） int array[][3] = {{0,1,2},{3,4,5}}
 */
void test2() {
    int array[4][5] = {0};
    int i,j,k = 0;
    for (i = 0; i < 4; i++) { //4行
        for (j = 0; j < 5; j++) {
            array[i][j] = k++; //赋值
        }
    }
    printf("*(array +1): %p\n", *(array + 1));
    printf("array[1]: %p\n", array[1]); //仍是地址，因为array是二维的，如果取值应该有个[][]
    printf("&array[1][0]:%p\n", &array[1][0]);
    printf("**(array+1)：%d\n",**(array+1)); //*(array + 1)是地址，在对它进行一层解引用(对地址解引用，就是取出地址里面真正的值)

    printf("*(*(array+1)+3): %d\n", *(*(array + 1) + 3)); //对 *(array + 1) + 3这个地址再解引用取值
    printf("array[1][3]: %d\n", array[1][3]);
}

void test1() {
    int array[4][5] = {0};

    printf("sizeof in :%d\n", sizeof(int));
    printf("array: %p\n", array);
    printf("array + 1: %p\n", array + 1); //十六进制的14是十进制 1*16^1 + 4*16^0 = 20 即一行5个int元素，每个占4个字节
}
