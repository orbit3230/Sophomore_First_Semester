#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define MAX_LIST_SIZE 100  // 최대 크기
typedef int element;
typedef struct {
    element array[MAX_LIST_SIZE];
    int size;
} ArrayListType;
// 오류 처리 함수
void error(const char* message) {
    fprintf(stderr, "%s\n", message);
    exit(1);
}
// 리스트 initialize 함수
void init(ArrayListType* L) {
    L->size = 0;
}
// 리스트가 비어있으면 true, 그렇지 않으면 false
bool is_empty(ArrayListType* L) {
    return (L->size == 0);
}
// 리스트가 가득찼으면 true, 그렇지 않으면 false
bool is_full(ArrayListType* L) {
    return (L->size == MAX_LIST_SIZE);
}
// 리스트에서 특정 위치의 값 반환
element get_entry(ArrayListType* L, int index) {
    if(index < 0 || index >= L->size)
        error("인덱스 에러");
    return L->array[index];
}
// 리스트 출력
void print_list(ArrayListType* L) {
    for(int i = 0 ; i < L->size ; i++) {
        printf("%d->", L->array[i]);
    }
    printf("\n");
}
// 특정 위치에 삽입
void insert(ArrayListType* L, int index, element item) {
    if(is_full(L))
        error("리스트 오버플로우");
    if((index >= 0) && (index <= L->size)) {
        for(int i = (L->size - 1) ; i >= index ; i--)
            L->array[i+1] = L->array[i];
        L->array[index] = item;
        L->size++;
    }
    else
        error("인덱스 에러");
}
// 맨 끝에 삽입
void insert_last(ArrayListType* L, element item) {
    insert(L, L->size, item);
}
// 특정 위치 원소 삭제
element remove_e(ArrayListType* L, int index) {
    element item;
    if(index < 0 || index >= L->size)
        error("인덱스 에러");
    item = L->array[index];
    for(int i = index ; i < (L->size) - 1 ; i++)
        L->array[i] = L->array[i+1];
    L->size--;
    return item;
}

int main() {
    // ArrayListType를 정적으로 생성하고 ArrayListType를 가리키는 포인터를 함수의 매개변수로 전달한다.
    ArrayListType list;
    init(&list);
    insert(&list, 0, 10);
    print_list(&list);// 0번째 위치에 10 추가
    insert(&list, 0, 20);
    print_list(&list);// 0번째 위치에 20 추가
    insert(&list, 0, 30);
    print_list(&list);// 0번째 위치에 30 추가
    insert_last(&list, 40);
    print_list(&list);// 맨 끝에 40 추가
    remove_e(&list, 0);
    print_list(&list);// 0번째 항목 삭제
    return 0;
}