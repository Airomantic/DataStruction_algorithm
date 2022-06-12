"""
多路平衡查找树-B树
是一种组织和维护外存文件系统非常有效的数据结构
https://www.bilibili.com/video/BV1et4y117wc?from=search&seid=13950960766674611582&spm_id_from=333.337.0.0
1 根结点至少有两个子节点
2 每个中间结点都包含k-1个元素和k个孩子，其中m/2 <= k <= m
3 每一个叶子结点都包含k-1个元素，其中m/2 <= k <= m
4 所有的叶子结点都位于同一层
5 每个结点中的元素从小到大排列
"""