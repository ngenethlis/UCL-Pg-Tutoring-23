#include <stdio.h>
#include <stdlib.h>


typedef struct LinkedList{

    int data;

    struct LinkedList *next;

} LinkedList;


LinkedList* createLL(){


    

    LinkedList *head = (LinkedList*) malloc(sizeof(LinkedList));

    LinkedList *curr = (LinkedList*) malloc(sizeof(LinkedList));

    LinkedList temp = {0,head};

    head->next = curr ;

    // (*head).next = curr ;

    curr->data=0;

    for (int i=1;i<4;i++){
    LinkedList *nextNode = (LinkedList*) malloc(sizeof(LinkedList));
    nextNode->data=i;
    curr->next = nextNode;
    curr = curr->next;
    }
    curr->next=NULL;

    return head;
}

void printLL(LinkedList* head){

    LinkedList *curr = (LinkedList*) malloc(sizeof(LinkedList));
    curr = head->next;
    free(head);

    while (curr){
        printf("%d\n",curr->data);
        curr = curr->next;
    }

    free(curr);
}





int main(){

    return 0;
}

