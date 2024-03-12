#include <stdio.h>

int fibonacci(int);

int main() {
    printf("n: ");
    int n;
    scanf("%d", &n);

    printf("fibonacci n : %d", fibonacci(n));
}

int fibonacci(int n) {
    if(n==0) return 0;
    if(n==1) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
}