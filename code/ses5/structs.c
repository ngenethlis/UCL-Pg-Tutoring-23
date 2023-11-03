#include <stdio.h>
#include <stdlib.h>

typedef struct LinkedList
{
    int data;
    struct LinkedList *next;
} LinkedList;


int main(){

    LinkedList *head = (LinkedList*) malloc(sizeof(LinkedList));

    LinkedList *curr = (LinkedList*) malloc(sizeof(LinkedList));

    head->next = curr ;

    curr->data=0;

    for (int i=1;i<4;i++){
    LinkedList *nextNode = (LinkedList*) malloc(sizeof(LinkedList));
    nextNode->data=i;
    curr->next = nextNode;
    curr = curr->next;
    }
    curr->next=NULL;

    curr = head->next;

    while (curr){
        printf("%d\n",curr->data);
        curr = curr->next;
    }

    return 0;
}