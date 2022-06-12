//
// Created by 蒋宗青 on 2021/9/28.
//
/**
引入线索二又树是为了方便找到结点在某个遍历序列中的前驱和后继结点
该线索二叉树的前继后续指针是建立在"中序遍历"的，因为有的左右孩子指针是被占用，有的存在浪费，前序和后序遍历都不可以
 Thread 线，思路，线程闯过
 前序输入到内存对中序线索化没有影响，因为它是链式的，不是数组顺序存储一个挨着一个：https://www.bilibili.com/video/BV1jW411K7yg?p=50
 函数前不写默认返回为int，如果没有返回值则加上void
 或加上状态，如Statue 失败负几负几 如果是面向对象 就是try{}except异常处理机制对这个程序进行保护
 */
#include "stdio.h"
#include "stdlib.h" //malloc
//#include "string.h"
typedef char ElemType;
/**
线索存储标志位
 Link(0): 表示指向左右孩子的指针
 Thread(1): 表示指向前驱后继的线索
 */
typedef enum {
    Link,Thread
}PointerTag; //跟数组一样Link是从0开始，Thread是从1开始，编译器会把它们看成0和1
typedef struct BiThreadNode
{
    char data;
    struct BiThreadNode *lchild,*rchild;
    PointerTag ltag;
    PointerTag rtag;
}BiThreadNode,*BiThreadTree; //在malloc时BiThreadTree就等于BiThreadNode *
///全局变量，始终指向刚刚访问过的结点，记得要设初值，需要个头指针
BiThreadTree pre; //先前，这是Tree

///创建一棵二叉树,约定用户遵照前序遍历的方式输入数据
void CreateBiThrTree(BiThreadTree *T) //传入树的地址，*T是包含，指针域，数据域，标志域于一身
{
    char c;
    scanf("%c", &c);
    if (' ' == c) {
        *T = NULL;
    } else {
        *T = (BiThreadNode *) malloc(sizeof(BiThreadNode));
        //初始化
        (*T)->data = c;
        //先默认它是有左右孩子的，先把它创建出来普通二叉树，通过一个过程函数对这个二叉树线索化，逐步排查，若没有左右孩子即叶结点就设置ltag和rtag来修改*lchild和*rchild指向前驱后继
        (*T)->ltag = Link;
        (*T)->rtag = Link;

        CreateBiThrTree(&(*T)->lchild);
        CreateBiThrTree(&(*T)->rchild);
    }
}
/**
              A
       B            E
    C    D      null  F
 前：ABC__D__E_F__ 即：ABC  D  E F  |
 中：CBDAEF
 中序遍历线索化，即(递归左线索)(结点处理)(递归右线索)
*/
void InThreading(BiThreadTree T)
{//pre是全局变量，初始化时其右孩子指针为空，便于在树的最左点开始 建线索
    if(T){
        InThreading(T->lchild); //这个递归没有返回值，执行到底后就能跳出这一行，执行下一行

        if (!T ->lchild){ //没有左孩子
            T->ltag=Thread;
            T->lchild = pre; //把lchild指向刚刚访问过的结点
        }

        if (!pre->rchild)
        {
            pre->rtag = Thread;
            pre ->rchild = T; //T是刚刚访问过的线索
        }
        pre = T; //访问完之后，保持pre指向T的前驱

        InThreading(T->rchild); //递归右孩子线索化
    }
}
void InOrderThreading(BiThreadTree *p,BiThreadTree T)
{
    *p = (BiThreadTree) malloc(sizeof(BiThreadNode));
    ///初始化
    (*p) ->ltag = Link; //0
    (*p) ->rtag = Thread;
    (*p) ->rchild = *p;
    if(!T){
        (*p) ->lchild = *p; //空树就指向自己
    }else{
        (*p)->rchild = T; //头结点的左孩子指向根
        pre = *p; //pre初值指向头结点 这样pre就可以名正言顺
        InThreading(T); //对以T为根的二叉树进行中序线索化
        //收尾，指回去
        pre ->rchild = *p; //InThreading()结束后，pre为最右结点，pre的右线索指向头结点
        pre ->rtag = Thread; //1
        (*p) ->rchild=pre; //头结点的右线索指向pre
    }
}
void visit(char c)
{
    printf("%c", c);
}
///非递归迭代中序遍历
void InOrderTraverse(BiThreadTree T)
{
    BiThreadTree p; //通过p来接手T头指针
    p = T ->lchild;
///p=T 头指针等于根结点，空树或遍历到结束的时候
    while (p != T) {
        //先遍历左子树
        while (p->ltag == Link){ //Link 是0说明它是有左子树的
            p = p->lchild; //直到走到叶子结点没有左孩子就要指向前驱
        }
        visit(p->data); //访问到最左边这个叶结点
        while (p->rtag == Thread && p->rchild != T) { //p->rchild != T 如果没有指回去头结点，说明它是有后继的
            p = p ->rchild; //执行完这句，最左边这个叶结点就到了它的后继结点了
            visit(p->data);
        }
        p = p->rchild; //最右这个叶结点指向头结点
    }
}

int main()
{
    BiThreadTree P,T = NULL ; //这是tree不是node T=NULL初始化
    CreateBiThrTree(&T);
    InOrderThreading(&P,T);

    printf("中序遍历输出:");
    InOrderTraverse(P); //p是pre头结点头指针，T是根结点

    return 0;
}