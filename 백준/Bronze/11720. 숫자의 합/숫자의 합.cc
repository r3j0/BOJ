#include <stdio.h>

char s[101];
int main(void) {
    int n;
    scanf("%d", &n);
    scanf("%s", s);
    
    int sum_value = 0;
    for (int i = 0; i < n; i++) sum_value += (s[i] - '0');
    
    printf("%d", sum_value);
    return 0;
}