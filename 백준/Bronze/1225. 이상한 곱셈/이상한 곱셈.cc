#include <stdio.h>
#include <string.h>

char a[10001];
char b[10001];
int main(void) {
    scanf("%s %s", a, b);
    
    long long result = 0;
    for (int i = 0; i < strlen(a); i++) { 
        for (int j = 0; j < strlen(b); j++) {
            result += (a[i] - '0') * (b[j] - '0');
        }
    }
    printf("%lld", result);
    return 0;
}