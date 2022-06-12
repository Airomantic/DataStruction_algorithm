//
// Created by 蒋宗青 on 2021/9/18.
//
/**
Segmentation fault 分段错误 类似于出界的问题
gcc kmp.cpp -o kmp.c
注意Linux下
 malloc(sizeof(int) * n);
 mac下要加上 (int*)，否则cannot initialize a variable of type 'int *' with an rvalue of type 'void *'
 (int*)malloc(sizeof(int) * n);
 */
#include <stdio.h>
#include <stdlib.h> //malloc 基于Linux,mac系统直接用不了，还需加上
//#include <sys/malloc.h> //mac系统，此时不需要
#include <string.h> //strlen
void prefix_table(char pattern[], int prefix[], int n) {
    prefix[0] = 0;
    int len = 0;
    int i = 1;
    while (i < n) {
        if (pattern[len] == pattern[i]) {
            len++;
            prefix[i] = len;
            i++;
        } else {
            if (len > 0) { //为0时第一位对到了prefix下标0前面出界的位置（可想成-1），不能在向前找了
                len = prefix[len - 1];
            } else { //卡死在一开始 为0时是第一位和第二位len和i永远不一样
                prefix[i] = len; //这时len就已经是0了，写=0也可以
                i++;
            }
        }
    }
}

void move_prefix_table(int prefix[], int n) {
    int i;
    for (i = n - 1; i > 0; i--) {
        prefix[i] = prefix[i - 1];
    }
    prefix[0] = -1;
}

void kmp_search(char text[], char pattern[]) {

    ///准备工作
    int n = strlen(pattern);
    int m = strlen(text);
    int* prefix = (int*)malloc(sizeof(int) * n); //通过malloc创建一个数组 第二个* 申请每个元素都是int
    prefix_table(pattern, prefix, n); //无需返回，操作后的数据都都放在内存里了，直接调用函数即可
    move_prefix_table(prefix, n);
    ///kmp搜索
    // text[i] , len(text) = m //主串T
    // pattern[j], len(patter) = n  //匹配串P

    int i = 0;
    int j = 0;
    while (i < m) {
        ///这个完成匹配查询放在while里面
        if (j == n - 1 && text[i] == pattern[j]) { //当到了最后移位开始匹配，并且匹配成功
            printf("found pattern at %d\n", i - j);
            j = prefix[j]; // 继续往后看还有没有新的可以完整匹配pattern串的
        }
        if (text[i] == pattern[j]) {
            i++;
            j++;
        } else {
            j = prefix[j];//关键点：利用保存的公共子串记录，当前不匹配的prefix元素记录pattern下标的元素移动到当前j指针的位置
            if (j == -1) { //特殊情况，当中间有个元素不相等匹配到了prefix首位的-1
                i++;
                j++;
            }

        }
    }
}

int main() {
    /*char pattern[] = "ABABCABAA";
    int n = 9;
    int prefix[n];

    prefix_table(pattern, prefix, n);
    move_prefix_table(prefix, n); //-1	0	0	1	2	0	1	2	3	首位加上了-1同时把末尾1给顶出去了
    for (int i = 0; i < n; i++) {
        printf("%d\t", prefix[i]); //0	0	1	2	0	1	2	3	1 需要对其移位（首位加个-1）
    }
     */
    char pattern[] = "ABABCABAA";
    char text[] = "ABABBAABABCABAAABCABBA"; //从0开始Ω
    kmp_search(text,pattern);
}