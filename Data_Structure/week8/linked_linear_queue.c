#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 5
typedef int element;
typedef struct Node {
    element data;
    struct Node* next;
} Node;
typedef struct LinearQueue {
    Node* front;
    Node* rear;
    int size;
} LinearQueue;

void init(LinearQueue* q) {
    q->front = NULL;
    q->rear = NULL;
    q->size = 0;
}

int is_empty(LinearQueue* q) {
    return (q->size == 0);
}

int is_full(LinearQueue* q) {
    return (q->size == MAX_QUEUE_SIZE);
}

void enqueue(LinearQueue* q, element item) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = item;
    newNode->next = NULL;
    if(is_empty(q)) {
        q->front = newNode;
        q->rear = newNode;
    }
    else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
    q->size++;
}

element dequeue(LinearQueue* q) {
    if(is_empty(q)) {
        fprintf(stderr, "queue is empty.\n");
        exit(1);
    }
    else {
        Node* temp = q->front;
        element data = temp->data;
        q->front = q->front->next;
        free(temp);
        return data;
    }
    q->size--;
}

void printQueue(LinearQueue* q) {
    printf("|");
    for(Node* p = q->front; p != NULL; p = p->next) {
        printf(" %d |", p->data);
    }
    printf("\n");
}

int main() {
    LinearQueue q;
    init(&q);

    enqueue(&q, 10); printQueue(&q);
    enqueue(&q, 20); printQueue(&q);
    enqueue(&q, 30); printQueue(&q);
    dequeue(&q); printQueue(&q);
    dequeue(&q); printQueue(&q);
    dequeue(&q); printQueue(&q);

    return 0;
}