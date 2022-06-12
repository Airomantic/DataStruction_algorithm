//
// Created by 蒋宗青 on 2021/10/18.
//
#include <stdlib.h>
#include "stdio.h"

typedef char ElemType;

typedef struct LNode {
    ElemType data;
    struct LNode *next; //声明包含了指向自己类型的指针
} LNode, *LinkList; //LinkList为指向结构体LNode的指针类型，也可以单独写成 typedef struct LNode *LinkList;

void Del_X_3(LinkList L, ElemType x) {
    LNode *p;
    if (L == NULL) {
        return;
    }
    if (L->data == x) {
        p = L;
        L = L->next;
        free(p);
        Del_X_3(L, x);
    } else { // L所指结点值不为x
        Del_X_3(L->next, x);
    }
}

int main() {
    struct LNode *head, *p, *q, *t;
//    createLL()
    int i, n, a;
    scanf("%d", &n);
    head = NULL;
    for (int i = 0; i < n; i++) {
        p = (struct LNode *) malloc(sizeof(struct LNode));
        scanf("%d", &a);
        p->data = a;
        p->next = NULL;
        if (head == NULL)
            head = p;
        else
            q->next = p;
        q = p;
    }
    Del_X_3()
    //输出链表
    t = head;
    while (t != NULL) {
        printf("%d ", t->data);
        t = t->next;
    }
    return 0;
}

