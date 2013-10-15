#include <stdio.h>
#include <stdarg.h>

#define _INTSIZEOF(n)   ( (sizeof(n) + sizeof(int) - 1) & ~(sizeof(int) - 1) )


void ar_cnt(int cnt, ...);
void ar_cst(char const *s, ...);


int main(int argc, char *argv[]) {
    int in_size = _INTSIZEOF(int);
    printf("int_size=%d\n", in_size);
    ar_cnt(5, 1, 2, 3, 4);
    return 0;
}


void ar_cnt(int cnt, ...) {
    int value = 0;
    int i = 0;
    int arg_cnt = cnt;
    va_list arg_ptr;
    va_start(arg_ptr, cnt);
    for (i = 0; i < cnt; i++) {
        value = va_arg(arg_ptr, int);
        printf("posation %d=%d\n", value, i+1);
    }
    va_end(arg_ptr);
}
