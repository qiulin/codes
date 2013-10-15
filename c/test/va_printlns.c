#include <stdio.h>
#include <stdarg.h>


void printlns(char *fst, ...) {
    char        *str;
    va_list     vl;
    str = fst;
    va_start(vl, fst);

    do {
        printf("%s\n", str);
        str = va_arg(vl, char*);
    } while (str != NULL);

    va_end(vl);
}


int main(int argc, char *argv[]) {
    printlns("First", "Second", "Third", NULL);
    return 0;
}
