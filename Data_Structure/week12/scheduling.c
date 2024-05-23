#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 200
#define JOBS 7
#define MACHINES 3
typedef struct Element {
    int key;
    int machine;
} Element;

typedef struct HeapType {
    Element *heap;
    int heap_size;
} HeapType;

HeapType* create() {
    return (HeapType *)malloc(sizeof(HeapType) * MAX_ELEMENT);
}

void init(HeapType *h) {
    h->heap_size = 0;
}
// 최대 힙
void push_max_heap(HeapType *h, Element item) {
    int i = ++(h->heap_size);

    while((i != 1) && (item.key > h->heap[i/2].key)) {
        h->heap[i] = h->heap[i/2];
        i /= 2;
    }
    h->heap[i] = item;
}
Element pop_max_heap(HeapType *h) {
    int parent, child;
    Element item, temp;

    item = h->heap[1]; // return할 key
    temp = h->heap[(h->heap_size)--];
    parent = 1;
    child = 2;
    while (child <= h->heap_size) {
        // 왼쪽 자식과 비교
        if ((child < h->heap_size) && (h->heap[child].key) < h->heap[child + 1].key)
            child++; // 오른쪽 자식으로 이동
        if (temp.key >= h->heap[child].key)
            break;
        // break가 걸리지 않았다 -> 더 내려가야 한다
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2;
    }
    h->heap[parent] = temp;
    return item;
}
// 최소 힙
void push_min_heap(HeapType *h, Element item) {
    int i = ++(h->heap_size);

    while((i != 1) && (item.key < h->heap[i/2].key)) {
        h->heap[i] = h->heap[i/2];
        i /= 2;
    }
    h->heap[i] = item;
}
Element pop_min_heap(HeapType *h) {
    int parent, child;
    Element item, temp;

    item = h->heap[1]; // return할 key
    temp = h->heap[(h->heap_size)--];
    parent = 1;
    child = 2;
    while (child <= h->heap_size) {
        // 왼쪽 자식과 비교
        if ((child < h->heap_size) && (h->heap[child].key) > h->heap[child + 1].key)
            child++; // 오른쪽 자식으로 이동
        if (temp.key <= h->heap[child].key)
            break;
        // break가 걸리지 않았다 -> 더 내려가야 한다
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2;
    }
    h->heap[parent] = temp;
    return item;
}

int main() {
    int jobs[JOBS] = {8, 7, 6, 5, 3, 2, 1}; // 작업은 정렬되어 있다고 가정
    Element m = {0, 0};
    HeapType* h = create();
    init(h);
    for (int i = 0; i < MACHINES; i++) {
        m.key = 0;
        m.machine = i+1;
        push_min_heap(h, m);
    }
    // 최소힙에서 기계를 꺼내서 작업을 할당하고 사용가능 시간을 증가 시킨 후에
    // 다시 최소힙에 추가한다.
    for (int i = 0; i < JOBS; i++) {
        m = pop_min_heap(h);
        printf("JOB %d을 시간=%d부터 시간=%d까지 기계 %d번에 할당한다. \n",
               i, m.key, m.key + jobs[i] - 1, m.machine);
        m.key += jobs[i];
        push_min_heap(h, m);
    }
    return 0;
}