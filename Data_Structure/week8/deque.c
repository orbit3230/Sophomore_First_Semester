#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 5
typedef int element;
typedef struct {
    element data[MAX_QUEUE_SIZE];
    int front, rear;
} DequeType;

void init(DequeType* dq) {
    dq->front = 0;
    dq->rear = 0;
}

int is_empty(DequeType* dq) {
    return (dq->front == dq->rear);
}

int is_full(DequeType* dq) {
    return ((dq->rear + 1) % MAX_QUEUE_SIZE == dq->front % MAX_QUEUE_SIZE);
}

void add_front(DequeType* dq, element item) {
    if(is_full(dq)) {
        fprintf(stderr, "queue is full.\n");
        exit(1);
    }
    dq->data[dq->front] = item;
    dq->front = (dq->front - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
}

void add_rear(DequeType* dq, element item) {
    if(is_full(dq)) {
        fprintf(stderr, "queue is full.\n");
        exit(1);
    }
    dq->rear = (dq->rear + 1) % MAX_QUEUE_SIZE;
    dq->data[dq->rear] = item;
}

element delete_front(DequeType* dq) {
    if(is_empty(dq)) {
        fprintf(stderr, "queue is empty.\n");
        exit(1);
    }
    dq->front = (dq->front + 1) % MAX_QUEUE_SIZE;
    return dq->data[dq->front];
}

element delete_rear(DequeType* dq) {
    if(is_empty(dq)) {
        fprintf(stderr, "queue is empty.\n");
        exit(1);
    }
    element data = dq->data[dq->rear];
    dq->rear = (dq->rear - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
    return data;
}

void printQueue(DequeType* dq) {
    printf("front: %d, rear: %d\n", dq->front, dq->rear);
    if(!is_empty(dq)) {
        int i = dq->front;
        printf("|");
        do {
            i = (i + 1) % MAX_QUEUE_SIZE;
            printf(" %d |", dq->data[i]);
            if(i == dq->rear) break;
        } while(i != dq->front);
    }
    printf("\n");
}

int main() {
    DequeType dq;
    init(&dq);
    add_front(&dq, 1); printQueue(&dq);
    add_front(&dq, 2); printQueue(&dq);
    add_rear(&dq, 3); printQueue(&dq);
    add_rear(&dq, 4); printQueue(&dq);
    delete_front(&dq); printQueue(&dq);
    delete_rear(&dq); printQueue(&dq);
    delete_front(&dq); printQueue(&dq);
    delete_rear(&dq); printQueue(&dq);
    return 0;
}