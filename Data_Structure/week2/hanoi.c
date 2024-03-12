#include <stdio.h>

int hanoi_tower(int, char, char, char);

int main() {
    printf("n: ");
    int n;
    scanf("%d", &n);

    hanoi_tower(n, 'A', 'B', 'C');
}

int hanoi_tower(int n, char from, char tmp, char to) {
    if(n == 1) printf("원판 1을 %c에서 %c로 옮긴다.\n", from, to);
    else {
        hanoi_tower(n-1, from, to, tmp);
        printf("원판 %d을(를) %c에서 %c로 옮긴다.\n", n, from, to);
        hanoi_tower(n-1, tmp, from, to);
    }
}