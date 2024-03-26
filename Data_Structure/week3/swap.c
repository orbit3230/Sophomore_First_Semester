#include <stdio.h>
void swap(int *x, int *y) {
  int tmp;
  tmp = *x;
  *x = *y;
  *y = tmp;
}
int main(void) {
  int a = 1, b = 2;
  swap(&a, &b);
  printf("a=%d, b=%d\n", a, b);
  return 0;
}