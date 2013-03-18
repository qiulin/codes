#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[])
{
    char *ptr1;
    char *ptr2 = "Hell, world!";
    char *re = (void *)(ptr1 = ptr2);
    printf("%x\n", re);
    return 0;
}
