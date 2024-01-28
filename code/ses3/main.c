#include <stdio.h>
#include <stdlib.h>
#include "someFile.h"

int main(void){

    int a = 5;
    int b = 10;
    int c = add(a,b);
    printf("The sum of %d and %d is %d \n",a,b,c);
    return 0;
}