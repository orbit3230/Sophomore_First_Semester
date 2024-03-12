#include <stdio.h>

int factorial(int);

int main() {
    int n;;
    printf("n을 입력하세요: ");
    scanf("%d", &n);

    int fac = factorial(n);

    printf("%d", fac);
}

int factorial(int n) {
    if(n <= 1) return 1;
    else return (n * factorial(n-1));
}