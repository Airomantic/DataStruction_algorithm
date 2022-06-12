//
// Created by 蒋宗青 on 2021/10/23.
//
/**
ABD##E##C##
D E B C A 
 */
#include "iostream"

using namespace std;
typedef struct TreeNode{
    char data;
    struct TreeNode *lchild,*rchild;
    int tag; //标志域，记录结点是否被访问过
    //一个结点具有4个空间 t-> data-> *lchild-> *rchild-> tag
}TreeNode,*Tree;
//ABD##E##C##
void createTree(Tree &t){
    char ch;
    ch = getchar();
    if(ch=='#') t = NULL;
    else
    {
        t = (TreeNode *) malloc(sizeof(TreeNode)); //使开辟的空间具有树结点TreeNode的*性质 t为对象
        t->data = ch;
        t->tag = 0;
        t->lchild = NULL;
        t->rchild = NULL; //一开始都是空
        createTree(t->lchild); //递归构造左右孩子
        createTree(t->rchild);
    }
}

///非递归求后续遍历
void postOrd(Tree t){
    struct TreeNode *stack[100];//栈可以直接使用这个结构体
    int top = -1; //栈顶指针
    TreeNode *p = t; //指针先指向这棵树
    TreeNode *x;//出栈时，要用结点把它保存起来

    while (p||top!=-1)
    {
        if(p)
        {
            top++; //进栈先向上移动指针
            stack[top] = p; // 再将p指向的结点赋值进去
            p = p->lchild;
        } else { // p为空，只能通过栈不为空，这时读取栈顶元素，判断其左孩子
            p = stack[top];
            if (p->rchild && p->rchild->tag == 0)
                p = p->rchild; //去指向它的右孩子
            //如果访问过，就出栈，并且输出该结点
            else{
                p = stack[top];
                top--;
                cout << p->data << " ";
                p->tag = 1;
                p = NULL; // p指向NULL
            }
        }
    }
}
int main()
{
    Tree t;
    createTree(t);
    postOrd(t);
    return 0;
}