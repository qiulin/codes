/****************************
 * 测试多种数据类型的长度
 * ***************************/

#include <iostream>
#include <stdlib.h>
using namespace std;

int main(int argc, const char *argv[])
{
    char str[] = "hello";
    char *p = str;
    char *ptr = (char *)malloc(100);
    int n = 10;
    std::cout << "sizeof(str[]):" << sizeof(str) << std::endl;
    std::cout << "sizeof(*p):" << sizeof(p) << std::endl;
    std::cout << "sizeof(n):" << sizeof(n) << std::endl;
    std::cout << "sizeof(*ptr)" << sizeof(ptr) << std::endl;
    return 0;
}
