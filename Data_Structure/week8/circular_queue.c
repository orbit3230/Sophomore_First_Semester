#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 5
typedef int element;
typedef struct {
    element data[MAX_QUEUE_SIZE];
    int front, rear;
} QueueType;

void init(QueueType* q) {
    q->front = 0;
    q->rear = 0;
}

int is_empty(QueueType* q) {
    return (q->front == q->rear);
}

int is_full(QueueType* q) {
    return ((q->rear + 1) % MAX_QUEUE_SIZE == q->front % MAX_QUEUE_SIZE);
}

void enqueue(QueueType* q, element item) {
    if(is_full(q)) {
        fprintf(stderr, "queue is full.\n");
        exit(1);
    }
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = item;
}

element dequeue(QueueType* q) {
    if(is_empty(q)) {
        fprintf(stderr, "queue is empty.\n");
        exit(1);
    }
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    return q->data[q->front];
}

void printQueue(QueueType* q) {
    printf("front: %d, rear: %d\n", q->front, q->rear);
    if(!is_empty(q)) {
        int i = q->front;
        printf("|");
        do {
            i = (i + 1) % MAX_QUEUE_SIZE;
            printf(" %d |", q->data[i]);
            if(i == q->rear) break;
        } while(i != q->front);
    }
    printf("\n");
}

int main() {
    QueueType q;
    init(&q);
    enqueue(&q, 1); printQueue(&q);
    enqueue(&q, 2); printQueue(&q);
    enqueue(&q, 3); printQueue(&q);
    enqueue(&q, 4); printQueue(&q);
    dequeue(&q); printQueue(&q);
    dequeue(&q); printQueue(&q);
    dequeue(&q); printQueue(&q);
    dequeue(&q); printQueue(&q);
    return 0;
}