#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode {
    element data;
    struct ListNode* link;
} ListNode;
// 맨 앞에 노드 삽입
ListNode* insert_first(ListNode* head, element value) {
    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->data = value;
    if(head == NULL) {
        head = p;
        p->link = p;
    }
    else {
        p->link = head->link;
        head->link = p;
    }
    return head;
}
// 맨 끝에 노드 삽입
ListNode* insert_last(ListNode* head, element value) {
    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->data = value;
    if(head == NULL) {
        head = p;
        p->link = p;
    }
    else {
        p->link = head->link;
        head->link = p;
        head = p;
    }
    return head;
}
// 맨 앞의 노드 삭제
ListNode* remove_first(ListNode* head) {
    ListNode* removed;
    if(head == NULL) return NULL;
    if(head == head->link) {
        free(head);
        return NULL;
    }
    removed = head->link;
    head->link = removed->link;
    free(removed);
    
    return head;
}
// 맨 끝의 노드 삭제
ListNode* remove_last(ListNode* head) {
    if (head == NULL) return NULL; // 리스트가 비어있는 경우
    // 노드가 하나뿐인 경우
    if (head->link == head) {
        free(head);
        return NULL;
    }
    ListNode* current = head->link; // 첫 번째 노드부터 시작
    while (current->link != head) { // 마지막 노드의 바로 이전 노드 찾기
        current = current->link;
    }
    // 이제 current는 마지막에서 두 번째 노드입니다.
    current->link = head->link; // 마지막에서 두 번째 노드가 첫 번째 노드를 가리키도록 함
    free(head); // 원래의 마지막 노드 (head)를 해제
    head = current; // head를 마지막에서 두 번째 노드로 업데이트

    return head;
}
// circular linked list 출력
void print_list(ListNode* head) {
    ListNode* p;
    if(head == NULL) {
        printf("empty\n");
        return;
    }
    p = head->link;
    do {
        printf("%d->", p->data);
        p = p->link;
    } while(p != head->link);
    printf("\n");
}

int main() {
    ListNode* head = NULL;
    element data; // 삭제된 데이터를 저장할 변수
    // list = 10->20->30->40
    head = insert_last(head, 20);
    head = insert_last(head, 30);
    head = insert_last(head, 40);
    head = insert_first(head, 10);
    print_list(head);

    head = remove_last(head);
    print_list(head);
    head = remove_first(head);
    print_list(head);
    head = remove_last(head);
    print_list(head);
    head = remove_first(head);
    print_list(head);
    return 0;
}