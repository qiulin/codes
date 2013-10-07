#include <iostream>
#include "BinaryTree.h"


//先序递归遍历二叉树
template <class ElemType>
void BinaryTree<ElemType>::_PreorderTraverse (BTNode<ElemType>*T,
        void(*visit)(const ElemType &e))
{
    if(T){
        visit(T->data);
        _PreorderTraverse(T->lchild, visit);
        _PreorderTraverse(T->rchild, visit);
    }
}

//先序递归遍历二叉树的接口函数
template <class ElemType>
void BinaryTree<ElemType>::PreorderTraverse(void (*visit) (const ElemType &e))
{
    _PreorderTraverse(m_root, visit);
}
