#include <stdio.h>

void quicksot(int r[], int s, int t) {
    int i = s, j = t;
    int tmp;
    if(s < t) {
        tmp = r[s];
        while(i!=j) {
            while(j>i && r[j] > tmp)
                j--;
            r[i] = r[j];
            while(i<j && r[i] < tmp)
                i++;
            r[j] = r[i];
        }
        r[i] = tmp;

        quicksot(r, s, i-1);
        quicksot(r, i+1, t);
    }
}

int main(int argc, const char *argv[])
{
    int num[10] = {12, 21, 4, 45, 5, 1, 5, 6, 11, 53};
    quicksot(num, 0, 9);

    int i;
    for (i = 0; i <= 9; i++) {
        printf("%d,", num[i]);
    }
    printf("\n");
    return 0;
}
