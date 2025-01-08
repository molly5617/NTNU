#include <stdio.h>
#include <string>
using namespace std;
int main()
{
    string s = "hello world";
    printf("%s\n", s - s[4] + s[5]);
}