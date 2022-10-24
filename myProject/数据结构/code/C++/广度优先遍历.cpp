//广度优先遍历要点
//1. 找到与一个顶点相邻的所有顶点
//2. 标记哪些顶点被访问过
//3. 需要一个辅助队列

//FirstNeighbor(G, x):   求图G中顶点x的第一个邻接点，若有则返回顶点号。
//                       若x没有邻接点或图中不存在x，则返回-1。

//NextNeighbor(G, x, y): 假设图G中顶点y是顶点x的一个邻接点，返回除y之外顶点x的下一
//                       个邻接点的顶点号，若y是x的最后一个邻接点，则返回-1。

bool visited[MAX_VERTEX_NUM];       //访问标记数组，初始都为false.


//广度优先遍历
void BFS(Graph G, int v){           //从顶点v出发，广度优先遍历图G
    visit(v);                       //访问初始顶点v
    visited[v] = TRUE;              //对v做已访问标记
    EnQueue(Q, v);                  //顶点v入队列Q
    while(!isEmpty(Q)){             //持续遍历直到队列为空
        DeQueue(Q, v);              //出队列，v表示出队列的第一个顶点
        for(w=FirstNeighbor(G, v); w>=0; w=NextNeighbor(G, v, w))   //初始为v的第一个临近点，后面每次找除上层以外的其他临近点。
            //检测所有邻接点
            if(!visited[w]){        //w为v的尚未访问的邻接顶点
                visit(w);           //访问顶点w
                visited[w]=TRUE;    //对w做已访问标记
                EnQueue(Q, w);      //将w入队列
            }
    }
}