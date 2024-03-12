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
    
    int sum;
    int nMinus1 = 1;
    int nMinus2 = 0;
    for(int i = 2 ; i <= n ; i++) {
        sum = nMinus1 + nMinus2;
        nMinus2 = nMinus1;
        nMinus1 = sum;
    }
    return sum;
}