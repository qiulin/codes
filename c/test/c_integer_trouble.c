#include <stdio.h>

int main(int argc, char **argv) {
    long i = -1;
    if (i < sizeof(i)) {
        printf("OK\n");
    } else {
        printf("error\n");
    }

    char c = 128;
    char d = 129;
    printf("%d, %d\n", c, d);
    return 0;
}
