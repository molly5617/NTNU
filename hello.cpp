#include <stdio.h>

int main()
{
    char s[] = "hello world";        // 使用 char 陣列儲存字串
    printf("%s\n", s - s[4] + s[5]); // 正確使用 %s 輸出整個字串
    return 0;
}