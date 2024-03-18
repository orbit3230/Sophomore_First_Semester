#include <stdio.h>
#define MAX(a, b) ((a > b) ? a : b)
#define MAX_DEGREE 101

typedef struct {
    int degree;
    float coef[MAX_DEGREE];
} polynomial;

polynomial poly_add1(polynomial y1, polynomial y2) {
    polynomial y;  // 결과 다항식
    int y1Index = 0,  y2Index = 0, yIndex = 0;
    int degree_y1 = y1.degree;
    int degree_y2 = y2.degree;
    y.degree = MAX(degree_y1, degree_y2);
    while(y1Index <= y1.degree && y2Index <= y2.degree) {
        if(degree_y1 > degree_y2) {
            y.coef[yIndex++] = y1.coef[y1Index++];
            degree_y1--;
        }
        else if(degree_y1 == degree_y2) {
            y.coef[yIndex++] = y1.coef[y1Index++] + y2.coef[y2Index++];
            degree_y1--;
            degree_y2--;
        }
        else {
            y.coef[yIndex++] = y2.coef[y2Index++];
            degree_y2--;
        }
    }
    return y;
}
void print_poly(polynomial y) {
    for(int i = y.degree ; i > 0 ; i--)
        printf("%3.1fx^%d + ", y.coef[y.degree - i], i);
    printf("%3.1f \n", y.coef[y.degree]);
}
 int main(void)
 {
    polynomial y1 = { 5,{ 3, 6, 0, 0, 0, 10 } };
    polynomial y2 = { 4,{ 7, 0, 5, 0, 1 } };
    polynomial y;
    print_poly(y1);
    print_poly(y2);
    y = poly_add1(y1, y2);
    printf("-----------------------------------------------------------------------------\n");
    print_poly(y);
    return 0;
 }
