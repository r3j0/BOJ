#include <stdio.h>
#include <string.h>

int main(void) {
    char str[101];
    scanf("%s", str);
    
    int cnt = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') cnt += 1;
    }
    printf("%d", cnt);
    return 0;
}