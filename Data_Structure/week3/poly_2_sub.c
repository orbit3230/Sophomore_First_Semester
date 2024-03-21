#include <stdio.h>
#define MAX_TERMS 101

typedef struct {
    float coef;
    int expo;
} polynomial;

polynomial yA[MAX_TERMS] = {{8, 3}, {7, 1}, {1, 0}};
polynomial yB[MAX_TERMS] = {{10, 3}, {3, 2}, {1, 0}};
polynomial y[MAX_TERMS];  // 결과 다항식
int y1Index = 0;
int y2Index = 0;
int yIndex = 0;

void attach(float coef, int expo) {
    y[yIndex].coef = coef;
    y[yIndex].expo = expo;
    yIndex++;
}
void poly_add2() {
    
    int expo_y1;
    int expo_y2;
    while(y1Index <= 2 && y2Index <= 2) {
        expo_y1 = yA[y1Index].expo;
        expo_y2 = yB[y2Index].expo;
        if(expo_y1 > expo_y2) {
            attach(yA[y1Index].coef, expo_y1);
            y1Index++;
        }
        else if(expo_y1 == expo_y2) {
            attach(yA[y1Index].coef - yB[y2Index].coef, expo_y1);
            y1Index++;
            y2Index++;
        }
        else {
            attach(yB[y2Index].coef, expo_y2);
            y2Index++;
        }
    }
}
void print_poly(polynomial y[], int index) {
    int i;
    for(i = 0 ; i < index-1 ; i++)
        printf("%3.1fx^%d + ", y[i].coef, y[i].expo);
    printf("%3.1f\n", y[i].coef);
}
 int main(void)
 {
    poly_add2();
    print_poly(yA, y1Index);
    print_poly(yB, y2Index);
    printf("-----------------------------------------------------------------------------\n");
    print_poly(y, yIndex);
    return 0;
 }
