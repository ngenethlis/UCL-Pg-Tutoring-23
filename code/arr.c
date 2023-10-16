#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    int numbers[10] = {1,2,3,4,5,6,7,8,9,10};

    char message[] = "Hello World!";
    // same thing as ^ using pointers char *pmessage = "Hello World!";

    for(int i=0;i<10;i++)
    {
        printf("The number is %d at index %d\n",numbers[i],i);
    }


    // printing as string without pointers

    char c;
    for (int j=0;message[j]!='\0';j++)
    {
        c = message[j];
        printf("%c",c);
    }

    printf("\n");

    for(char *p=message;*p!='\0';p++)
    {
        printf("%c",*p);
    }
    printf("\n");

 

    return 0;
}
