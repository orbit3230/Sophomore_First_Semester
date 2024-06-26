#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 200

typedef struct TreeNode {
    int data;  // weight
    char ch;
    struct TreeNode *left, *right;
} TreeNode;

typedef struct Element {
    int key;
    TreeNode *node;
} Element;

typedef struct HeapType {
    Element *heap;
    int heap_size;
} HeapType;

void init(HeapType *h) {
    h->heap = (Element *)malloc(sizeof(Element) * MAX_ELEMENT);
    h->heap_size = 0;
}

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

TreeNode* huffman_tree(int freq[], char ch_list[], int n) {
    TreeNode *node, *x, *y;
    HeapType heap;
    Element e, e1, e2;

    init(&heap);
    for (int i = 0; i < n; i++) {
        node = (TreeNode *)malloc(sizeof(TreeNode));
        node->data = freq[i];
        node->ch = ch_list[i];
        node->left = node->right = NULL;
        e.key = node->data;
        e.node = node;
        push_min_heap(&heap, e);
    }
    for (int i = 1; i < n; i++) {
        e1 = pop_min_heap(&heap);
        e2 = pop_min_heap(&heap);
        x = e1.node;
        y = e2.node;
        node = (TreeNode *)malloc(sizeof(TreeNode));
        node->data = x->data + y->data;
        node->left = x;
        node->right = y;
        e.key = node->data;
        e.node = node;
        push_min_heap(&heap, e);
    }
    return pop_min_heap(&heap).node;
}

void print_codes(TreeNode *root, int codes[], int top) {
    // 왼쪽으로 가면서 1을 저장
    if (root->left) {
        codes[top] = 1;
        print_codes(root->left, codes, top + 1);
    }
    // 오른쪽으로 가면서 0을 저장
    if (root->right) {
        codes[top] = 0;
        print_codes(root->right, codes, top + 1);
    }
    // 리프 노드에 도달하면 코드를 출력
    if (!(root->left) && !(root->right)) {
        printf("'%c': ", root->ch);
        for (int i = 0; i < top; i++)
            printf("%d", codes[i]);
        printf("\n");
    }
}

int main() {
    char ch_list[] = {'s', 'i', 'n', 't', 'e'};
    int freq[] = {4, 6, 8, 12, 15};
    int codes[MAX_ELEMENT];
    TreeNode *root = huffman_tree(freq, ch_list, 5);
    print_codes(root, codes, 0);
    return 0;
}