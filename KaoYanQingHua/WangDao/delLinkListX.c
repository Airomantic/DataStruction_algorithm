//
// Created by 蒋宗青 on 2021/10/18.
// https://blog.csdn.net/weixin_45682058/article/details/121139903

#include "stdio.h"
#include "stdlib.h"

typedef struct Link {
    int value;
    struct Link *next;
};


struct Link *create() {
    struct Link *p, *rear, *head;
    int count = 0;
    rear = (struct Link *) malloc(sizeof(struct Link));
    head = (struct Link *) malloc(sizeof(struct Link));
    int value;
    printf("请输入链表各结点的值，以9999结束");
    scanf("%d", &value);
    while (value != 9999) { //依次创建结点
        p = (struct Link *) malloc(sizeof(struct Link));
        p->value = value;
        p->next = NULL;
        if (count++ == 0) {
            rear = p;
            head = p;
        } else {
            rear->next = p; //尾插法
        }
        scanf("%d", &value);
    }
    rear->next = NULL;
    return head;
}

struct Link *create2() {
    struct Link *p, *rear, *head;
    rear = (struct Link *) malloc(sizeof(struct Link));
    head = (struct Link *) malloc(sizeof(struct Link));
    head = rear = NULL;
    int value;
    printf("请输入链表各结点的值，以9999结束：");
    scanf("%d", &value);
    int count = 0;
    while (value != 9999) {
        p = (struct Link *) malloc(sizeof(struct Link));
        p->value = value;

        if (head == NULL) {
            head = p;
            rear = p;
        } else {
            p->next = head->next; //头插法
            head->next = p;
            rear = p;
            if (count++ == 0) {
                rear->next = NULL;
            }
        }
        scanf("%d", &value);
    }
    return head;
}

void deleteX(struct Link *pLink, int delNum) { //这里的第一个函数参数必须是引用值，不然会导致断链
    struct Link *pre; //定义个指针，进行删除
    if (pLink == NULL) return;
    if (pLink->value == delNum) {
        pre = pLink;
        pLink = pLink->next;
        free(pre);
        deleteX(pLink, delNum);
    } else {
        deleteX(pLink->next, delNum);
    }
}

int main() {
    int delNum;
    struct Link *head, *q;
    head = create2();
    q = head;
    printf("打印链表：");
    while (q != NULL) {
        printf("%d", q->value);
        q = q->next;
    }
    q = head;
    printf("输入想要删除的结点值：");
    scanf("%d", &delNum);
    deleteX(q, delNum);
    printf("删除后链表：");
    while (q != NULL) {
        printf("%d", q->value);
        q = q->next;
    }
    return 0;
}

