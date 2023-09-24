#include <stdio.h> 

int main(void) {
    int w, h;
    scanf("%d %d", &w, &h);
    printf("%.1lf", (double)w * h / 2);
    return 0;
}