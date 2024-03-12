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
    int sum = n;
    for(n = n-1 ; n >= 1 ; n--) {
        sum *= n;
    }
    return sum;
}