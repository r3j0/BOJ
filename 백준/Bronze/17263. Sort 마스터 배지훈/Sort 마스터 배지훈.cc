#include <stdio.h>

int main(void) {
    int n; 
    scanf("%d", &n);

    int max_value = 0;
    int tmp;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        if (max_value < tmp) max_value = tmp;
    }
    
    printf("%d", max_value);
    return 0;
}