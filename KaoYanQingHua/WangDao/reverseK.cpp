//
// Created by 蒋宗青 on 2021/10/22.
//

#include "iostream"

using namespace std;
// 单链表
typedef struct lnode{
    int data;
    struct lnode *next;
}lnode,*linklist;

int a[5] = {5, 4, 3, 2, 1};
int n = 5;

void buildlist(linklist &L)
{
    L = (linklist) malloc(sizeof(lnode));
    lnode *s,*r = L;
    for (int i = 0; i < n; i++)
    {
        s = (lnode *) malloc(sizeof(lnode));
        s->data = a[i]; // 数组传给链表
        r->next = s;
        r = r->next;
    }
    r->next=NULL; //尾指针指向空
}

int findK(linklist L,int k)
{
    lnode *pre = L->next, *q = L->next; //pre，q都指向头结点
    int num = 0;
    while (pre != NULL)
    {
        if (num<k) num++;
        else q = q->next; //后指针开始同步移动
        pre = pre->next;  //前指针
    }
    if(num<k) return 0; //说输入的k>链表长度
    else{ //成功找到
        cout <<"倒数第k个结点的值为："<<q->data<<" ";
        return 1;
    }
}

int main()
{
    linklist L;
    buildlist(L);
    findK(L, 2);
    return 0;
}