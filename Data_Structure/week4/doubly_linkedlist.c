#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct DListNode {
    element data;
    struct DListNode* llink;
    struct DListNode* rlink;
} DListNode;
// 이중 링크드 리스트 초기화
void init(DListNode* head) {
    head->llink = head;
    head->rlink = head;
}
// 노드 삽입
void dinsert(DListNode* before, element value) {
    DListNode* newnode = (DListNode*)malloc(sizeof(DListNode));
    newnode->data = value;
    newnode->llink = before;
    newnode->rlink = before->rlink;
    before->rlink->llink = newnode;
    before->rlink = newnode;
}
// 노드 삭제
void dremove(DListNode* head, DListNode* removed) {
    if(removed == head) return;
    removed->llink->rlink = removed->rlink;
    removed->rlink->llink = removed->llink;
    free(removed);
}
// 이중 링크드 리스트 출력
void print_dlist(DListNode* head) {
    DListNode* p;
    for(p = head->rlink; p != head; p = p->rlink) {
        printf("<-| |%d| |-> ", p->data);
    }
    printf("\n");
}

int main() {
    DListNode* head = (DListNode*)malloc(sizeof(DListNode));
    init(head);
    printf("Add nodes\n");
    for(int i = 0; i < 5; i++) {
        // 헤드 노드의 오른쪽에 삽입
        dinsert(head, i);
        print_dlist(head);
    }
    printf("\nRemove nodes\n");
    for(int i = 0; i < 5; i++) {
        print_dlist(head);
        dremove(head, head->rlink);
    }
    free(head);
    return 0;
}