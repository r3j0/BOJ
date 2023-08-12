#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef char element;
typedef struct DlistNode{
    element data;
    struct DlistNode* llink;
    struct DlistNode* rlink;
}DlistNode;

void init(DlistNode* head){
    head->llink = head;
    head->rlink = head;
}

void insert(DlistNode* before, element item){
    DlistNode* newNode = (DlistNode *)malloc(sizeof(DlistNode));
    newNode->data = item;
    newNode->llink = before;
    newNode->rlink = before->rlink;
    before->rlink->llink = newNode;
    before->rlink = newNode;
}

void delete(DlistNode* head, DlistNode* removed){
    if(removed == head)    return;
    else{
        removed->llink->rlink = removed->rlink;
        removed->rlink->llink = removed->llink;
        free(removed);
    }

}

//입력된 문자열을 문자 단위로 쪼개서 리스트에 넣는 함수
DlistNode* read(char* input){
    element ch;
    DlistNode* head = (DlistNode *)malloc(sizeof(DlistNode));
    DlistNode* cursor;

    init(head);
    cursor = head;

    int len = strlen(input);
    
    for(int i=0;i<len;i++){
        ch = input[i];

        switch(ch){
            case '<':
                if(cursor != head)  cursor = cursor->llink;
                break;
            case '>':
                if(cursor != head->llink)  cursor = cursor->rlink;
                break;
            case '-':
                if(cursor != head) {
                cursor = cursor->llink;
                delete(head,cursor->rlink);
                }
                break;
            default :
                insert(cursor,ch);
                cursor = cursor->rlink;
                break;
        }
    }
    return head;
}

int main(void){
    int n;
    char** L;

    DlistNode* head = (DlistNode *)malloc(sizeof(DlistNode));

    scanf("%d",&n);

    L = (char **)malloc(sizeof(char *)*n);

    for(int i=0;i<n;i++){
        L[i] = (char *)malloc(sizeof(char)*1000000);
        scanf("%s",L[i]);
    }

    for(int i=0;i<n;i++){
        head = read(L[i]);
        DlistNode* p = head->rlink;
        
        while(p!=head) {
            printf("%c",p->data);
            p = p->rlink;
        }
        printf("\n");
    }
            
    return 0;
}