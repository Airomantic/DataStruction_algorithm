//
// Created by 蒋宗青 on 2021/9/28.
//
#include <stdlib.h>
#include <math.h> //OVERFLOW
#include "stdio.h"
//#include "c1.h"  //已配置好头文件的绝对路径
#define OK 1
#define ERROR 0
/**
c语言中没有status这个关键字，但一般写程序时，会定义这样的一个类型，用来表示成功或失败状态，0表示成功，-1表示失败
ASL: https://www.cnblogs.com/ygsworld/p/10238729.html


 在链表中: *p表结点，p表指针变量(存储另一个普通变量的地址) https://www.bilibili.com/video/BV17s411N78s?p=21
 一般情况下: https://www.runoob.com/cprogramming/c-pointers.html
 结构体: 声明包含了指向自己类型的指针

 */
typedef int ElemType;
typedef int Status;

typedef struct LNode {
    ElemType data;
    struct LNode *next; //声明包含了指向自己类型的指针
} LNode, *LinkList; //LinkList为指向结构体LNode的指针类型，也可以单独写成 typedef struct LNode *LinkList;

///构造一个空的单链表L
Status InitList(LinkList *L) {
    *L = (LinkList) malloc(sizeof(struct LNode)); //生成新结点作为头结点，用头指针L指向头结点 其实就是初始化让L具有指针的性质
    if (!*L) //存储分配失败 注意 记得要判空
        exit(OVERFLOW);
    (*L)->next = NULL; //头结点的指针域置为空
    return OK;
}
/**
初始条件：线性表L已存在。操作结果：销毁线性表L
 */
Status DestroyList(LinkList *L)
{
    LinkList q; //声明一个指针变量，因为本身*LinkList就是结构指针了，所以q不用带*就能声明q为指针变量，普通情况下则: int *q带上*
    while (*L){
        q = (*L) ->next;
        free(*L);
        (*L)=q;
    }
    return OK;
}

/**
单链表取值
L为带头结点的单链表的头指针。当第i个元素存在时,其值赋给e并返回OK,否则返回ERROR
 */
Status GetElem(LinkList L, int i, ElemType *e) {
    int j = 1;
    LinkList p = L->next; //p指向第一个结点
    while (p && j < i) { //顺指针向后查找,直到p指向第i个元素或p为空
        p = p ->next;
        j++;
    }
    if (!p||j>i) //第i个元素不存在
        return ERROR;
    *e = p->data; //取第i个元素

    return OK;
}
/**
单链表的按值查找
 */
