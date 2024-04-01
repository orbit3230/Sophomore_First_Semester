#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    double coef;
    int expon;
    struct ListNode* link;
} ListNode;
// 노드 삽입
ListNode* insert(ListNode* head, ListNode* pre, double coef, int expon) {
    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->coef = coef;
    p->expon = expon;
    p->link = pre->link;
    pre->link = p;
    return head;
}
// 맨 앞에 노드 삽입
ListNode* insert_first(ListNode* head, double coef, int expon) {
    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->coef = coef;
    p->expon = expon;
    p->link = head;
    head = p;
    return head;
}
// 노드 삭제
ListNode* remove_e(ListNode* head, ListNode* pre) {
    ListNode* removed;
    removed = pre->link;
    pre->link = removed->link;
    free(removed);
    return head;
}
// 맨 앞의 노드 삭제
ListNode* remove_first(ListNode* head) {
    ListNode* removed;
    if(head == NULL)
        return NULL;
    removed = head;
    head = removed->link;
    free(removed);
    return head;
}
// 다항식 출력
void poly_print(ListNode* head) {
    for(ListNode* p = head ; p != NULL ; p = p->link)
        printf("%.1fx^%d + ", p->coef, p->expon);
    printf("NULL \n");
}

ListNode* reverse(ListNode* head) {
    ListNode* reversed;
    reversed = NULL;
    while(head != NULL) {
        reversed = insert_first(reversed, head->coef, head->expon);
        head = head->link;
    }
    return reversed;
}

ListNode* poly_add(ListNode* head1, ListNode* head2) {
    ListNode* p1 = head1;
    ListNode* p2 = head2;
    ListNode* result = NULL;
    while(p1 && p2) {
        if(p1->expon == p2->expon) {
            double sum = p1->coef + p2->coef;
            if(sum != 0.0)
                result = insert_first(result, sum, p1->expon);
            p1 = p1->link;
            p2 = p2->link;
        } else if(p1->expon > p2->expon) {
            result = insert_first(result, p1->coef, p1->expon);
            p1 = p1->link;
        } else {
            result = insert_first(result, p2->coef, p2->expon);
            p2 = p2->link;
        }
    }
    // 남아 있는 항들을 결과에 항으로 추가
    for(; p1 != NULL ; p1 = p1->link)
        result = insert_first(result, p1->coef, p1->expon);
    for(; p2 != NULL ; p2 = p2->link)
        result = insert_first(result, p2->coef, p2->expon);

    return reverse(result);
}

int main() {
    ListNode* list1 = NULL;
    ListNode* list2 = NULL;
    ListNode* list3 = NULL;
    // 첫 번째 다항식
    list1 = insert_first(list1, 1, 0);
    list1 = insert_first(list1, 2, 8);
    list1 = insert_first(list1, 3, 12);
    // 두 번째 다항식
    list2 = insert_first(list2, 10, 6);
    list2 = insert_first(list2, -3, 10);
    list2 = insert_first(list2, 8, 12);

    poly_print(list1);
    poly_print(list2);
    printf("-------------------------------\n");
    list3 = poly_add(list1, list2);

    poly_print(list3);

    free(list1);
    free(list2);
    free(list3);
    
    return 0;
}