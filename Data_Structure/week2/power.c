#include <stdio.h>

int power(int, int);

int main() {
    int x;
    printf("x: ");
    scanf("%d", &x);
    int n;
    printf("n: ");
    scanf("%d", &n);

    printf("x^n : %d", power(x, n));
}

int power(int x, int n) {
    if(n == 0) return 1;
    else if((n % 2) == 0) return power(x*x, n/2);
    else return x*power(x*x, (n-1)/2);
}