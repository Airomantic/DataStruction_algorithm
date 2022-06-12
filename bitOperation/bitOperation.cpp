//
// Created by 蒋宗青 on 2021/9/22.
//
/**
https://www.bilibili.com/video/BV1ss41197pu?spm_id_from=333.999.0.0
过滤器：判断当前位是0还是1，采用与运算&
 &操作：任何数字与0做与操作(&)结果都为0，任何数字A与1做与操作(&)结果都为本身A
 对一串数字如：11011，保留它的最后一位数字，那就拿另外一串00001与它做逻辑与操作(&)，因为00001前面都是0，与操作后对应0的数字都被取消掉，把最后一位留下
 分治法
 两个两个过滤 01010101  和与运算得d1，原二进制串向后移动一位再与运算d2  最后加运算d1+d2
 四个四个过滤 00110011  和与运算得d1，右移动两位和与运算得d2，d1+d2加运算得到m1  00001111  对m1与运算得y1,右移四位与运算得y2，再y1+y2加运算得1的总和结果
 */
#include "stdio.h"

 int countOnes(int num)
 {
    int count = 0;
     while (num > 0) {
         if ((num & 1) == 1) {
             count ++;
         }
         num = num >>1;
     }
     return count;
 }
int main()
{
    int co = countOnes(17);
    printf("%d\n", co);
    return 0;
}