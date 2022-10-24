typedef struct{                         //查找表的数据结构（顺序表）
    ElemType *elem;                     //动态数组基址
    int TableLen;                       //表的长度
}SSTable;



int Binary_Search(SSTable L, ElemType key){
    int low = 0, high=L.TableLen-1, min;
    while(low<=high){
        min = (low + high)/2;           //获取中间位置
        if(L.elem[mid]==key)
            return mid;                 //查成功返回所在位置
        else if(L.elem[mid]<key)
            low = mid + 1;              //从后半部分继续查找
        else
            high = mid - 1;             //从前半部分继续查找
    }
    return -1;
}
