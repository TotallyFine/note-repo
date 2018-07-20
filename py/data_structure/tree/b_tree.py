# coding:utf-8

"""
B树是一种树状数据结构，能够进行存储数据对其进行排序并允许以O(log n)的时间复杂度进行查找顺序读取、插入和删除。

B树可以看作是对2-3查找树的一种扩展，允许每个节点有M-1个子节点：
1 根节点至少有两个子节点
2 每个节点有M-1个key，并且以升序排列
3 位于M-1和M key的子节点的值位于M - 1和M key对应的value之间
4 其他节点至少有M/2个子节点
"""