#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p;
    int x = 5;
    p = &x;
    printf("Location of x is at  %d\n", p);

    return 0;
}