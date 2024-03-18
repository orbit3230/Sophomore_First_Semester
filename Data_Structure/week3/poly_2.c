#include <stdio.h>
#define MAX(a, b) ((a > b) ? a : b)
#define MAX_TERMS 101

typedef struct {
    float coef;
    int expo;
} polynomial;

polynomial y1[MAX_TERMS] = {{8, 3}, {7, 1}, {1, 0}};
polynomial y2[MAX_TERMS] = {{10, 3}, {3, 2}, {1, 0}};
polynomial y[MAX_TERMS];  // 결과 다항식

polynomial poly_add2(polynomial y1, polynomial y2) {
    
    int y1Index = 0,  y2Index = 0, yIndex = 0;
    int expo_y1 = &y1.expo;
    int expo_y2 = &y2.expo;
    y.expo = MAX(expo_y1, expo_y2);
    while(y1Index <= y1.expo && y2Index <= y2.expo) {
        if(expo_y1 > expo_y2) {
            y.coef[yIndex++] = y1.coef[y1Index++];
            expo_y1--;
        }
        else if(expo_y1 == expo_y2) {
            y.coef[yIndex++] = y1.coef[y1Index++] + y2.coef[y2Index++];
            expo_y1--;
            expo_y2--;
        }
        else {
            y.coef[yIndex++] = y2.coef[y2Index++];
            expo_y2--;
        }
    }
    return y;
}
void attach(float coef, int expo) {
    y[0] = {coef, expo};
}
void print_poly(polynomial y[]) {
    for(int i = y.expo ; i > 0 ; i--)
        printf("%3.1fx^%d + ", y.coef[y.expo - i], i);
    printf("%3.1f \n", y.coef[y.expo]);
}
 int main(void)
 {
    polynomial y;
    print_poly(*y1);
    print_poly(*y2);
    y = poly_add2(y1, y2);
    printf("-----------------------------------------------------------------------------\n");
    print_poly(y);
    return 0;
 }
