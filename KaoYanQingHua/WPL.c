//
// Created by 蒋宗青 on 2021/10/15.
//
#include <stdlib.h>
#include "stdio.h"
typedef struct node{
    int weight;
    struct node *left,*right;
}BiNode,*BiTree;

int WPL = 0;

void inorder(BiTree bt, int lv)
{
    if(bt)
    {
        inorder(bt->left, lv + 1);
        if (bt ->left ==NULL && bt->right ==NULL)
        {
            WPL += (lv - 1) * bt->weight; //lv可看作工作指针，当指向子结点判断为空时，记得指回父结点获取权值
            inorder(bt->right, lv + 1);
        }
        printf("WPL = ", lv);
    }
}

void CreateBiThrTree(BiTree *pNode)
{
    int w;
    scanf("%d", &w);
    if (' ' == w) {
        *pNode = NULL;
    }else {
        *pNode = (BiNode *) malloc(sizeof(BiNode));
        //初始化
        (*pNode)->weight = w;

        CreateBiThrTree(&(*pNode)->left);
        CreateBiThrTree(&(*pNode)->right);
    }
}

int main()
{
    BiTree P,T = NULL ; //这是tree不是node T=NULL初始化
    CreateBiThrTree(&T);
    inorder(&P, T);
}


