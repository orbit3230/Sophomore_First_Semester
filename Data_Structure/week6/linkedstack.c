#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct StackNode {
    element data;
    struct StackNode* link;
} StackNode;

typedef struct {
    StackNode* top;
} LinkedStackType;

void init(LinkedStackType* s) {
    s->top = NULL;
}

int is_empty(LinkedStackType* s) {
    return (s->top == NULL);
}

int is_full(LinkedStackType* s) {
    return 0;
}

void push(LinkedStackType* s, element item) {
    StackNode* temp = (StackNode*)malloc(sizeof(StackNode));
    temp->data = item;
    temp->link = s->top;
    s->top = temp;
}

element pop(LinkedStackType* s) {
    if(is_empty(s)) {
        fprintf(stderr, "stack is empty.\n");
        exit(1);
    }
    else {
        element data = s->top->data;
        StackNode* temp = s->top;
        s->top = s->top->link;
        free(temp);
        return data;
    }
}

void printStack(LinkedStackType* s) {
    for(StackNode* p = s->top; p != NULL; p = p->link) {
        printf("%d->", p->data);
    }
    printf("NULL\n");
}