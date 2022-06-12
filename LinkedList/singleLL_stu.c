//
// Created by 蒋宗青 on 2021/9/28.
//


#include <stdio.h>

#define NAMELEN 8 /* 姓名最大长度 */
#define CLASSLEN 4 /* 班级名最大长度 */
struct stud /* 记录的结构 */
{
    char name[NAMELEN+1];
    long num;
    char sex;
    int age;
    char Class[CLASSLEN+1];
    int health;
};
typedef struct stud ElemType; /* 链表结点元素类型为结构体 */
//#include"c2-2.h"
char sta[3][9]={"健康  ","一般  ","神经衰弱"}; /* 健康状况(3类) */
FILE *fp;

#define N 4 /* student记录的个数 */
int main()
{
    struct stud student[N]={{"王小林",790631,'m',18,"计91",0},
            {"陈红",790632,'f',20,"计91",1},
            {"刘建平",790633,'m',21,"计91",0},
            {"张立立",790634,'m',17,"计91",2}}; /* 表的初始记录 */
            int i,j,flag=1;
            long num;
            char filename[13],name[NAMELEN+1];
            ElemType e;
            LinkList T,p,q;
            InitList(&T); /* 初始化链表 */
            while(flag)
            {
                printf("1:将结构体数组student中的记录按学号非降序插入链表\n");
                printf("2:将文件中的记录按学号非降序插入链表\n");
                printf("3:键盘输入新记录，并将其按学号非降序插入链表\n");
                printf("4:删除链表中第一个有给定学号的记录\n");
                printf("5:删除链表中第一个有给定姓名的记录\n");
                printf("6:修改链表中第一个有给定学号的记录\n");
                printf("7:修改链表中第一个有给定姓名的记录\n");
                printf("8:查找链表中第一个有给定学号的记录\n");
                printf("9:查找链表中第一个有给定姓名的记录\n");
                printf("10:显示所有记录 11:将链表中的所有记录存入文件 12:结束\n");
                printf("请选择操作命令: ");
                scanf("%d",&i);
                switch(i)
                {
                    case 1: for(j=0;j<N;j++)
                        InsertAscend(T,student[j]);
                    break;
                    case 2: printf("请输入文件名: ");
                    scanf("%s",filename);
                    if((fp=fopen(filename,"rb"))==NULL)
                        printf("打开文件失败!\n");
                    else
                    {
                        while(ReadFromFile(&e))
                            InsertAscend(T,e);
                        fclose(fp);
                    }
                    break;
                    case 3: ReadIn(&e);
                    InsertAscend(T,e);
                    break;
                    case 4: printf("请输入待删除记录的学号: ");
                    scanf("%ld",&num);
                    if(!DeleteElemNum(T,num))
                        printf("没有学号为%ld的记录\n",num);
                    break;
                    case 5: printf("请输入待删除记录的姓名: ");
                    scanf("%s",name);
                    if(!DeleteElemName(T,name))
                        printf("没有姓名为%s的记录\n",name);
                    break;
                    case 6: printf("请输入待修改记录的学号: ");
                    scanf("%ld%*c",&num); /* %*c吃掉回车符 */
                    if(!FindFromNum(T,num,&p,&q))
                        printf("没有学号为%ld的记录\n",num);
                    else
                    {
                        Modify(&q->data);
                        if(q->data.num!=num) /* 学号被修改 */
                            {
                            p->next=q->next; /* 把q所指的结点从L中删除 */
                            InsertAscend(T,q->data); /* 把元素插入L */
                            free(q); /* 删除q */
                            }
                    }
                    break;
                    case 7: printf("请输入待修改记录的姓名: ");
                    scanf("%s%*c",name); /* %*c吃掉回车符 */
                    if(!FindFromName(T,name,&p,&q))
                        printf("没有姓名为%s的记录\n",name);
                    else
                    {
                        num=q->data.num; /* 学号存入num */
                        Modify(&q->data);
                        if(q->data.num!=num) /* 学号被修改 */
                            {
                            p->next=q->next; /* 把q所指的结点从L中删除 */
                            InsertAscend(T,q->data); /* 把元素插入L */
                            free(q); /* 删除q */
                            }
                    }
                    break;
                    case 8: printf("请输入待查找记录的学号: ");
                    scanf("%ld",&num);
                    if(!FindFromNum(T,num,&p,&q))
                        printf("没有学号为%ld的记录\n",num);
                    else
                        Print(q->data);
                    break;
                    case 9: printf("请输入待查找记录的姓名: ");
                    scanf("%s",name);
                    if(!FindFromName(T,name,&p,&q))
                        printf("没有姓名为%s的记录\n",name);
                    else
                        Print(q->data);
                    break;
                    case 10:printf("  姓名    学号 性别 年龄 班级 健康状况\n");
                    ListTraverse(T,Print);
                    break;
                    case 11:printf("请输入文件名: ");
                    scanf("%s",filename);
                    if((fp=fopen(filename,"wb"))==NULL)
                        printf("打开文件失败!\n");
                    else
                        ListTraverse(T,WriteToFile);
                    fclose(fp);
                    break;
                    case 12:flag=0;
                }
            }
}

