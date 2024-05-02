#include <stdio.h>

typedef struct Node {
    char wordlist[100][100];
    struct Node *next;
} Node;
typedef struct Queue  {
    Node *head;
    Node *tail;
} Queue;

void init(Queue *q) {
    q->head = q->tail = NULL;
}
void enQueue(Queue *q, char *word) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    strcpy(newNode->wordlist[0], word);
    newNode->next = NULL;
    if (q->head == NULL) {
        q->head = q->tail = newNode;
    } else {
        q->tail->next = newNode;
        q->tail = newNode;
    }
}
char* deQueue(Queue *q) {
    if (q->head == NULL) {
        return NULL;
    }
    Node *tmp = q->head;
    q->head = q->head->next;
    char *word = malloc(sizeof(char) * 100);
    strcpy(word, tmp->wordlist[0]);
    free(tmp);
    return word;
}
char* peek(Queue *q) {
    if (q->head == NULL) {
        return NULL;
    }
    return q->head->wordlist[0];
}

int main() {
    int t;
    scanf("%d", &t);
    int n, m;
    scanf("%d %d", &n, &m);

    for(int i = 0 ; i < t ; i++) {
        Queue toMake;
        init(&toMake);
        for(int w = 0 ; w < m ; w++) {
            char word[100];
            scanf("%s", word);
            enQueue(&toMake, word);
        }

        Queue friends[n];
        for(int f = 0 ; f < n ; f++) {
            init(&friends[f]);
            int words;
            scanf("%d", &words);
            for(int w = 0 ; w < words ; w++) {
                char word[100];
                scanf("%s", word);
                enQueue(&friends[f], word);
            }
        }
        int make = 0;
        findNext:
        while(make < m) {
            char *word = deQueue(&toMake);
            for(int f = 0 ; f < n ; f++) {
                char *friendWord = peek(&friends[f]);
                if(strcmp(word, friendWord) == 0) {
                    deQueue(&friends[f]);
                    make++;
                    goto findNext;
                }
            }
            break;
        }
        if(make == m) {
            printf("1\n");
        } else {
            printf("0\n");
        }
    }
}