//
// Created by 蒋宗青 on 2021/10/2.
//

#include <stdio.h>
#include <stdlib.h>

//#include <malloc.h>
typedef char TElemType;
// 二叉树的二叉线索存储表示
typedef enum {
    Link,
    Thread
} PointerTag; // Link(0):指针,Thread(1):线索
typedef struct BiThrNode {
    TElemType data;
    struct BiThrNode *lchild, *rchild; // 左右孩子指针
    PointerTag LTag, RTag; // 左右标志
} BiThrNode, *BiThrTree;
TElemType Nil = ' '; // 字符型以空格符为空
BiThrTree pre; // 全局变量,始终指向刚刚访问过的结点
// 按先序输入二叉线索树中结点的值,构造二叉线索树T
// 空格(字符型)表示空结点
int CreateBiThrTree(BiThrTree *T) {
    TElemType h;
    scanf("%c", &h);
    if (h == Nil)
        *T = NULL;
    else {
        *T = (BiThrTree) malloc(sizeof(BiThrNode));
        if (!*T)
            exit(0);
        (*T)->data = h; // 生成根结点(先序)
        CreateBiThrTree(&(*T)->lchild); // 递归构造左子树
        if ((*T)->lchild) // 有左孩子
            (*T)->LTag = Link;
        CreateBiThrTree(&(*T)->rchild); // 递归构造右子树
        if ((*T)->rchild) // 有右孩子
            (*T)->RTag = Link;
    }
    return 1;
}

// 算法6.7 P135
// 中序遍历进行中序线索化。
void InThreading(BiThrTree p) {
    if (p) {
        InThreading(p->lchild); // 递归左子树线索化
        if (!p->lchild) // 没有左孩子
        {
            p->LTag = Thread; // 前驱线索
            p->lchild = pre; // 左孩子指针指向前驱
        }
        if (!pre->rchild) // 前驱没有右孩子
        {
            pre->RTag = Thread; // 后继线索
            pre->rchild = p; // 前驱右孩子指针指向后继(当前结点p)
        }
        pre = p; // 保持pre指向p的前驱
        InThreading(p->rchild); // 递归右子树线索化
    }
}

// 算法6.6 P134
// 中序遍历二叉树T,并将其中序线索化,Thrt指向头结点。
int InOrderThreading(BiThrTree *Thrt, BiThrTree T) {
    *Thrt = (BiThrTree) malloc(sizeof(BiThrNode)); // 建头结点
    if (!*Thrt)
        exit(0);
    (*Thrt)->LTag = Link; //标志左孩子为指针
    (*Thrt)->RTag = Thread; //标志右孩子为线索
    (*Thrt)->rchild = *Thrt; // 右指针回指
    if (!T) // 若二叉树空，则左指针回指
        (*Thrt)->lchild = *Thrt;
    else {
        (*Thrt)->lchild = T; //头结点左指针指向树的根
        pre = *Thrt;
        InThreading(T); // 中序遍历进行中序线索化
        pre->RTag = Thread; // 最后一个结点线索化
        pre->rchild = *Thrt;
        (*Thrt)->rchild = pre;
    }
    return 1;
}

// 算法6.5 P134
// 中序遍历二叉线索树T(头结点)的非递归算法。
int InOrderTraverse_Thr(BiThrTree T, int(*Visit)(TElemType)) {
    BiThrTree p;
    p = T->lchild; // p指向根结点
    while (p != T) { // 空树或遍历结束时,p==T
        while (p->LTag == Link)
            p = p->lchild;
        if (!Visit(p->data)) // 访问其左子树为空的结点
            return 0;
        while (p->RTag == Thread && p->rchild != T) {
            p = p->rchild;
            Visit(p->data); // 访问后继结点
        }
        p = p->rchild;
    }
    return 1;
}

int vi(TElemType c) {
    printf("%c ", c);
    return 1;
}

int main() {
    BiThrTree H, T;
    printf("请按先序输入二叉树(如:ab三个空格,表示a为根结点,"
           "b为左子树的二叉树)\n");
    CreateBiThrTree(&T); // 按先序产生二叉树
    InOrderThreading(&H, T); // 中序遍历，并中序线索化二叉树
    printf("中序遍历(输出)二叉线索树:\n");
    InOrderTraverse_Thr(H, vi); // 中序遍历(输出)二叉线索树
    printf("\n");
    system("pause");
    return 0;
}