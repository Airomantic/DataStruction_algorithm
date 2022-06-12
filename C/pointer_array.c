//
// Created by 蒋宗青 on 2021/9/30.
//
#include <string.h>
#include "stdio.h"

int test1(void)
{
    int a;
    int *p = &a;

    printf("请输入一个整数：");
    scanf("%d",&a);
    printf("a = %d\n",a);

    printf("请重新输入一个整数：");
    scanf("%d",p); //p存放*p的地址，而*p又存放的是a的地址，即*p指向a
    printf("a = %d\n",a);

    char str[123];

    printf("请输入一个的域名：");
    scanf("%s",str); //跟指针一样，不需要取址操作符
    printf("这个域名是: %s\n",str);

    ///数组名其实是数组第一个元素的地址!
    printf("str地址: %s\n",str);
    printf("这个域名是: %s\n",&str[0]);

}
///32bit下 char占一个字节 int和float占4个字节，double占8个节
int test_array(){
    char a[] = "Jiang";
    int b[5]= {1,2,3,4,5};
    float c[5]={1.1,2.1,3.1,4.1,5.1};
    double d[5]={1.1,2.1,3.1,4.1,5.1};

    ///对比标准下标访问数组元素，该间接访问叫指针法
    char *p =a; //p+1 不是简单地将地址加1，而是指向数组的下一个元素，只是这里恰巧，增加一个字母是增加一个字节
    printf("*p =%c,*(p+1) =%c,*(p+2) =%c\n",*p,*(p+1),*(p+2));
    int *pt = b; //p+1 不是简单地将地址加1，而是指向数组的下一个元素，对于int型，每次是地址加4（数组单个元素的长度），定义指针变量的时候就告诉编译器，那么double就是加8
    printf("*pt =%d,*(pt+1) =%d,*(pt+2) =%d\n",*pt,*(pt+1),*(pt+2));

    ///数组名本身就是指向数组第一个元素的地址，指针法作用于数组
    printf("*b =%d,*(bt+1) =%d,*(b+2) =%d\n",*b,*(b+1),*(b+2));

    ///查看数组元素的地址递增存储规则
    printf("a[0] ->%p,a[1] ->%p,a[2] ->%p,\n",&a[0],&a[1],&a[2]); //char的字节用字母表示，一个字母占一个字节
    printf("b[0] ->%p,b[1] ->%p,b[2] ->%p,\n",&b[0],&b[1],&b[2]); //十位以上的a=10,b=11,c=12...
    printf("c[0] ->%p,c[1] ->%p,c[2] ->%p,\n",&c[0],&c[1],&c[2]);
    printf("d[0] ->%p,d[1] ->%p,d[2] ->%p,\n",&d[0],&d[1],&d[2]); //16进制
}
int test_array_pointer()
{
    char *str = "I love Jiang";
    int i,length;

    length = strlen(str); //把调用的strlen()获取到的长度存放到一个变量当中，这样在for循环进行比较是否越界时，就不用重复调用strlen()产生大量耗时
    for (i = 0; i < length; i++) {
        printf("%c",str[i]); //当个字符时就不能用%s，而是%c
    }
}
int main()
{
//    test1(); //这些调用函数都要写在main()前面
//    test_array();
    test_array_pointer();
    return 0;
}
