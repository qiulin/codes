#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void left_shift_one(char *s, int n)
{
    char t = s[0];
    int i;
    for (i = 1; i < n; i++)
    {
        s[i-1] = s[i];
    }
    s[n-1] = t;
}


void left_shift_m(char *s, int n, int m)
{
    while (m--) {
        left_shift_one(s, n);
    }
}



int main(int argc, char *argv[])
{
    char str[50];
    sprintf(str, "abcdefg");
    printf("%s\n", str);
    left_shift_m(str, 3, 7);
    printf("%s\n", str);
    return 0;
}
