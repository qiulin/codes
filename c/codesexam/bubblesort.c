#include <stdio.h>

void bubblesort(int num[], int len) {
    int i, j;
    for (i = 0; i < len-1; i++) {
        for (j=len-1; j>i; j--) {
            if(num[j-1] > num[j]) {
                int tmp = num[j-1];
                num[j-1] = num[j];
                num[j] = tmp;
            }
        }
    }
}

int main(int argc, const char *argv[])
{
    int num[7] = {1,3,5,6,21, 53,3};
    int len = 7;
    bubblesort(num, len);
    int i;
    for(i=0; i<len; i++)
        printf("%d,", num[i]);
    printf("\n");
    return 0;
}
