#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct {
    element data;
    struct ListNode* link;
} ListNode;

int main() {
    // 리스트의 생성
    ListNode* head = NULL;
    head = (ListNode*)malloc(sizeof(ListNode));
    head->data = 10;
    head->link = NULL;
    // 2번째 노드 생성
    ListNode *p;
    p = (ListNode*)malloc(sizeof(ListNode));
    p->data = 20;
    p->link = NULL;
    head->link = p;

    free(head);
    free(p);
}