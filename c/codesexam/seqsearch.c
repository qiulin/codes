#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int key;
    int data;
} NodeType;
#define MAXL 10
typedef NodeType SeqList[MAXL];


#define MAXI 30
typedef struct {
    int key;
    int link;
} IdxType;
typedef IdxType IDX[MAXI];


int SeqSearch(SeqList R, int n, int k) {
    int i = 0;
    while (i < n && R[i].key != k) i++;
    if (i >= n)
        return -1;
    else
        return i;
}

int BinSearch(SeqList R, int n, int k) {
    int low = 0, high = n-1, mid;
    while (low<=high) {
        mid = (low + high) / 2;
        if (R[mid].key == k)
            return mid;
        if (R[mid].key > k)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}


int IdxSearch(IDX I, int m, SeqList R, int n, int k) {
    int low = 0, high = m - 1, mid, i;
}
int main(int argc, const char *argv[])
{

    return 0;
}
