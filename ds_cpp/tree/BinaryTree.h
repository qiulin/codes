#ifndef _BINARYTREE_H
#define _BINARYTREE_H
#include <stack>
#include <queue>
#include "BTnode.h"
#endif
using namespace std;

//二叉链表类
template<class ElemType>
class BinaryTree
{
    public:
        //构造函数
        BinaryTree() : m_root(NULL) {}

        //拷贝构造
        BinaryTree(const BinaryTree &rhs)
        {
            m_root = _Copy(rhs.m_root);
        }

        //赋值重载
        BinaryTree& operator=(const BinaryTree& rhs)
        {
            if(&rhs == this)
                return *this;

            _Destroy(m_root);
            m_root = _Copy(rhs.m_root);
            return *this;
        }

        //析构函数
        ~BinaryTree()
        {
            _Destroy(m_root);
        }

        //按以先序次序输入结点值的方式建立二叉树的接口函数
        void Create1(ElemType ch[], const ElemType &endChar);

        //以二叉树的先序和中序遍历次序建立二叉树的接口函数
        void Create2(ElemType ch1[], ElemType ch2[], int);

        //置空二叉树
        void Clear()
        {
            _Destroy(m_root);
        }

        //判断二叉树是否为空
        bool IsEmpty() const
        {
            return m_root == NULL;
        }

        //返回根节点的指针
        BTNode<ElemType>* Root() const
        {
            return m_root;
        }

        //返回二叉树T中元素为e的结点的指针
        BTNode<ElemType>* Locate(ElemType &e)
        {
            return _Locate(m_root, e);
        }

        //求二叉树深度
        int Depth()
        {
            return _Depth(m_root);
        }

        //返回节点的双亲结点
        BTNode<ElemType>* Parent(BTNode<ElemType> *p)
        {
            return _Parent(m_root, p);
        }

        //返回节点的左汉字结点
        BTNode<ElemType>* LeftChild(BTNode<ElemType> *p)
        {
            return p->lchild;
        }

        //返回结点的右孩子结点
        BTNode<ElemType>* RightChild(BTNode<ElemType> *p)
        {
            return p->rchild;
        }

        //返回结点的左兄弟结点
        BTNode<ElemType>* LeftSibing (BTNode<ElemType> *p);

        //返回结点的右兄弟结点
        BTNode<ElemType>* RightSibing (BTNode<ElemType> *p);

        //先序递归遍历二叉树的接口函数
        void PreorderTraverse(void (*visit)(cosnt ElemType &));

        //先序非递归遍历二叉树的接口函数
        void PreorderTraverseNonRecursive(void (*visit)(const ElemType &));

        //中序递归遍历二叉树的接口函数
        void InorderTraverse(void (*visit)(const ElemType &));

        //中序非递归遍历二叉树的接口函数
        void InorderTraverseNonRecursive(void (*visit)(const ElemType &));

        //后序遍历二叉树的接口函数
        void PostorderTraverse(void (*visit)(const ElemType &));

        //后序非递归遍历二叉树的接口函数
        void PreorderTraverseNonRecursive(void (*visit)(const ElemType &));

        //层序遍历二叉树
        void LevelTraverse(void (*visit)(const ElemType &e));

        //有条件插入
        bool InsertChild(BTNode<ElemType> *p, const int &, BinaryTree<char> &);

        //有条件删除
        void DeleteChild(BTNode<ElemType> *p, int which);


    private:
        BTNode<ElemType> *m_root; //二叉树根结点指针

        //复制二叉树
        BTNode<ElemType>* _Copy (BTNode<ElemType>* );

        //按先序次序输入结点值的方式建立二叉树
        void _Create1(BTNode<ElemType>* &, ElemType ch[], const ElemType &, int &);

        //已知二叉树的先序遍历次序及中序遍历次序，建立二叉树T
        void _Create2(BTNode<ElemType>*&, ElemType ch1[], ElemType ch2[], int,  int, int &);

        //销毁二叉树
        void _Destroy (BTNode<ElemType>* &);

        //求二叉树的深度
        int _Depth (BTNode<ElemType>* );

        //返回二叉树中元素值为e的结点的指针
        BTNode<ElemType>* _Locate (BTNode<ElemType>*, const ElemType &);

        //返回e结点的双亲结点指针
        BTNode<ElemType>* _Parent (BTNode<ElemType>*, BTNode<ElemType>*);

        //返回e结点的双亲结点指针
        BTNode<ElemType>* _Parent (BTNode<ElemType>*, BTNode<ElemType>*);

        //先序递归遍历二叉树
        void _PreorderTraverse (BTNode<ElemType>*, void (*visit)(const ElemType &e));

        //中序递归遍历二叉树
        void _InorderTraverse (BTNode<ElemType>*, void (*visit)(const ElemType &e));

        //后序递归遍历二叉树
        void _PostorderTraverse(BTNode<ElemType>*, void (*visit)(const ElemType  &e));
};
#endif
