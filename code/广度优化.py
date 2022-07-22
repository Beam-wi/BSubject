import collections

def updateMatrix(matrix):
    """
    题目：给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
         两个相邻元素间的距离为 1 。
    例题：输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
         输出：[[0,0,0],[0,1,0],[0,0,0]]

         输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
         输出：[[0,0,0],[0,1,0],[1,2,1]]
    :param matrix:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    Q = collections.deque([])
    visited = set()
    # 初始化队列，将所有起始点加入
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                Q.append((i, j))
                visited.add((i, j))
    # 将所有相邻节点加入队列
    while Q:
        i, j = Q.popleft()  # 先取出都为0的点 (后面会把没加过的添加到队列)
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:  # 查找周边的四个点
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:  # 判断是否出界 是否加入过
                matrix[x][y] = matrix[i][j] + 1  # 因为是周边为1的临近点所以，后面的要加前面的总距离
                visited.add((x, y))
                Q.append((x, y))
    return matrix