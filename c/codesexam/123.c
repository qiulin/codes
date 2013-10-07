#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[])
{
    int i;
    for (i = 1; i <= 9; i++) {
        if(i * 3 <= 9) {
            printf("%d%d%d\n",i, 2*i, 3*i);
        }
    }
    return 0;
}
