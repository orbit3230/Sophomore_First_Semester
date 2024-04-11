#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int element;

typedef struct StackNode {
    element data;
    struct StackNode* link;
} StackNode;

typedef struct LinkedStackType {
    StackNode* top;
} LinkedStackType;

void init(LinkedStackType* s);
int is_empty(LinkedStackType* s);
int is_full(LinkedStackType* s);
void push(LinkedStackType* s, element item);
element pop(LinkedStackType* s);
void printStack(LinkedStackType* s);

int check_matching(char* input) {
    LinkedStackType s;
    init(&s);
    for(int i = 0; i < strlen(input); i++) {
        char ch = input[i];
        switch(ch) {
            case '(':
            case '{':
            case '[':
                push(&s, ch);
                break;
            case ')':
                if(is_empty(&s) || pop(&s) != '(') return 0;
                break;
            case '}':
                if(is_empty(&s) || pop(&s) != '{') return 0;
                break;
            case ']':
                if(is_empty(&s) || pop(&s) != '[') return 0;
                break;
        }
    }
    if(!is_empty(&s)) return 0;
    return 1;  // 모두 통과하면 정상 괄호
}

int main() {
    char* str = (char*)malloc(sizeof(char) * 100);
    scanf("%s", str);
    if(check_matching(str)) printf("Correct parentheses matching\n");
    else printf("Incorrect parentheses matching\n");
    return 0;
}

