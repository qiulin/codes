#include <iostream>

using namespace std;

struct st1
{
    char a;
    int b;
    short c;
};

struct st2
{
    short c;
    char a;
    int b;
};

int main(int argc, const char *argv[])
{
    int len = sizeof(st1);
    std::cout << "sizeof(st1)" << sizeof(st1) << std::endl;
    std::cout << "sizeof(st2)" << sizeof(st2) << std::endl;
    return 0;
}
