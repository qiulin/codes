// BTnode.h 二叉链表结构
template <class ElemType>
struct BTnode {
    ElemType Data;
    BTnode<ElemType> *Lchild, *Rchild;
};

