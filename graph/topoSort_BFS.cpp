//
// Created by 蒋宗青 on 2021/10/21.
//

/**
* https://www.bilibili.com/video/BV1Ux411R7tz?from=search&seid=3047329614973251819&spm_id_from=333.337.0.0
 * https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/
 * 王道 https://www.icourse163.org/learn/kaopei-1462037162?tid=1462809445#/learn/content?type=detail&id=1240055141&cid=1261308855&replay=true
 * 邻接矩阵
输入
5 6
1 2
1 3
2 3
2 4
3 4
3 5
输出
1 2 3 4 5
*/
#include "iostream"
#include "vector"
#include <iomanip>                                // For stream manipulators
#include <string>                                 // For string class
#include <sstream>                                // For istringstream
#include <algorithm>                              // For replace_if() & for_each()
#include <set>                                    // For map container
#include <iterator>                               // For advance()
#include <cctype>
//#include "bits/stdc++.h" //https://blog.csdn.net/qq_30914611/article/details/101642850

using namespace std;
int main()
{
    int n, m, x, y;
    cin >> n >> m;
    vector<vector<int>> v(n + 1, vector<int>(n + 1, 0)); //第二个参数表初始化为0 二维有第二参数的第二个参数
    vector<bool> visited(n + 1, false); //第一个参数为size 第二个参数表初始化为false
    vector<int> res;
    vector<int> indegree(n + 1, 0);
    for (int i = 0; i < m; i++)
    {
        cin >> x >> y;
        v[x][y] = 1;//有边设为1    x->y
        indegree[y]++; //x指向y
    }

    multiset<int> q; //队列
    for (int i = 1; i < n; i++) {
        if (indegree[i] == 0) {
            q.insert(i);
            visited[i] = true;
        }
    }
    while (!q.empty()) {
        int cur = *q.begin();
        q.erase(q.begin()); //消除度为0的的点
        res.push_back(cur); //加入目标路径的集合中
        for (int i = 0; i < v[cur].size(); i++) {
            if (v[cur][i]==0) continue;
            if (--indegree[i] == 0 && !visited[i]) {
                visited[i] = true;
                q.insert(i); //入队
            }
        }
    }
    for (auto i:res) {
        cout << i << " ";
    }
    return 0;
}