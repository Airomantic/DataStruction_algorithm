//
// Created by 蒋宗青 on 2021/10/21.
///http://poj.org/problem?id=2367
///https://leetcode-cn.com/problems/course-schedule/
/// https://www.bilibili.com/video/BV1zZ4y1V7aA?from=search&seid=3047329614973251819&spm_id_from=333.337.0.0
/**
 * 课程表
 * 注意 这题 data[,] data[1]指向data[0]
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> point; //点与点之间的关系 key-value
    vector<int> visited; //
    bool ret = true;

    //DFS 接口
    void dfs(int i) //入参是数字key
    {
        visited[i] = 1; //正在访问
        for (int j:point[i]) //从当前的key出发 访问所有它相邻所有的点
            {
                if (visited[j] == 1)  // 说明形成了环
                {
                    ret = false;
                    return;
                } else if (visited[j] == 0){ //从未访问过的点，新开辟的点
                    dfs(j);
                    if (ret == false) {
                        //不加也行，优化一下  for (int j:point[i])避免错了还继续for完 节约了一下时间
                    }
                }
            }
        visited[i] = 2; // 该点与所有相邻的点均被访问
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        point.resize(numCourses); //指定大小
        visited.resize(numCourses);
        //遍历 把图放到二维容器里面去
        for (const auto &data:prerequisites) {
            point[data[1]].push_back(data[0]);// data[1]指向data[0]
        }
        for (int i = 0; i < numCourses && ret; i++) {
            // ret一旦找到return值是false就没必要继续往后搜索了
            dfs(i);
        }
        return ret;
    }
};
int main()
{

}