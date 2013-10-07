#include <stdio.h>
#include <stdlib.h>

typedef int KeyType;
typedef int InfoType;
typedef struct {
    KeyType key;
    InfoType data;
} RecType;

void InsertSort(RecType R[], int n) {
    int i, j;
    RecType tmp;
    for (i = 1; i < n; i++) {
        tmp = R[i];
        j = i - 1;
        while (j >= 0 && tmp.key < R[j].key) {
            R[j+1] = R[j];
            j--;
        }
        R[j+1] = tmp;
    }
}
