//
// Created by 蒋宗青 on 2021/9/27.
//

//#include <cstdlib> //C++
#include "stdio.h"
#include "stdlib.h" //C语言
/**
ABCDE

A 位于第 1 层
B 位于第 2 层
C 位于第 3 层
D 位于第 4 层
E 位于第 5 层

 位于第 6 层
 这是左斜树
 对于一颗
            A
     B             C
 null  D        E    null
  null null null null
 应输入：AB D  CE   |
 即;ABnullDnullnullCEnullnullnull
AB D  CE
A 位于第 1 层
B 位于第 2 层
D 位于第 3 层
C 位于第 2 层
E 位于第 3 层
 */

typedef char ElemType;
typedef struct BiTNode {
    char data;
    struct BiTNode *lchild, *rchild; //*lchild是结点，lchild是指针
} BiTNode, *BiTree; //*BiTree方便引用参数时的指针

///先序遍历创建
CreateBiTree(BiTree *T)
{
    char c;
    scanf("%c",&c);
    if(' '==c) //只能单引号
        {
        *T = NULL; //*T结点，空结点，还有叶子结点，所以写完ABCDE之后还得输入足够的叶子结点数量接入的空结点，比如这里有三个叶子结点，尾部还得至少输入空格7个
        }else{
        *T =(BiTNode *)malloc(sizeof (BiTNode)); //生成一个BiTNode的结点，强转BiTNode类型的指针 ，因为malloc返回的是一个地址
        (*T)->data = c; //赋值
        CreateBiTree(&(*T)->lchild); //双重指针，没有*是地址，对应*T，但不加&时，会报错-两边不对称，传入的可能不是函数所需要的
        CreateBiTree(&(*T)->rchild); //加上&取地址
    }
}
///访问二叉树结点的具体操作
visit(char c ,int level)
{
    printf("%c 位于第 %d 层\n",c,level);
}
///遍历二叉树
PreOrderTraverse(BiTree T,int level)
{
    if(T)
    {
        visit(T->data,level);
        PreOrderTraverse(T->lchild,level+1);
        PreOrderTraverse(T->rchild,level+1);
    }
}

int main()
{
    int level = 1;
    BiTree T = NULL; //指针指向一个new，或说指向空指针
    CreateBiTree(&T);
    PreOrderTraverse(T,level);
    return 0;
}

