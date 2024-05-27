#include <stdio.h>

typedef struct {
    int valueA;
    int valueB;
} Resource;

int main() {
    int t;
    scanf("%d", &t);

    for(int i = 0 ; i < t ; i++) {
        int n;
        scanf("%d", &n);
        Resource *resources = (Resource*)malloc(sizeof(Resource) * n);
        for(int j = 0 ; j < n ; j++) {
            int x, y;  // x : value of A country, y : value of B country
            scanf("%d %d", &x, &y);
            
        }

    }
}