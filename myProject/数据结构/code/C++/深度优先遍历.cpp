//深度优先遍历要点
//1. 找到与一个顶点相邻的所有顶点
//2. 标记哪些顶点被访问过

//FirstNeighbor(G, x):   求图G中顶点x的第一个邻接点，若有则返回顶点号。
//                       若x没有邻接点或图中不存在x，则返回-1。

//NextNeighbor(G, x, y): 假设图G中顶点y是顶点x的一个邻接点，返回除y之外顶点x的下一
//                       个邻接点的顶点号，若y是x的最后一个邻接点，则返回-1。

bool visited[MAX_VERTEX_NUM];       //要是全局, 初始全False

void DFS(Graph G, int v){           //从顶点v出发，深度优先遍历图G
    visit(v);                       //访问顶点v
    visited[v] = TRUE;              //设已访问标记
    for(w=FirstNeighbor(G, v), w>=0, w=NextNeighbor(G, v, w))
        if(!visited[w]){            //w为u的尚未访问的邻接顶点
            DFS(G, w);
        }
}