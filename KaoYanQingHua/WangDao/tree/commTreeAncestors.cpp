//
// Created by 蒋宗青 on 2021/10/22.
//

/**
* 二叉树两个结点寻找公共祖先
  https://www.bilibili.com/video/BV1ab4y1U7Pg/?p=2&spm_id_from=pageDriver
*/
#include "iostream"

using namespace std;
struct Tree{
    int data[12] = {-1, 1, 2, 3, -1, 4, -1, 5, -1, 6, -1}; //初始第一个为-1 空 然后才是根
};

int comm(Tree t, int i, int j)
{
    if (t.data[i] != -1 && t.data[j] != -1) {
        while (i != j) {
            if(i>j) i /= 2;
            else j /= 2;
        }
        return t.data[i];
    }
    return -1;
}
int main()
{
    Tree t;
    int ans = comm(t, 10, 7);
    cout << ans << endl;
    return 0;
}