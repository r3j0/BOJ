#include <stdio.h>
#include <string.h>

int main(void) {
    char str[1001];
    scanf("%s", str);
    
    int cnt = 0;
    for (int i = 0; i < strlen(str) - 3; i++) { 
        // 문자열은 0부터 strlen(str) - 1 까지 문자를 가진다.
        // 뒤에 남은 3글자, 2글자, 1글자... 에서 DKSH가 나오진 않으므로 ( 4글자기에 )
        // 마지막 4글자까지 탐색하고 종료하기 위해 조건을 i < strlen(str) - 3 으로 잡는다.
        if (str[i] == 'D' && str[i+1] == 'K' && str[i+2] == 'S' && str[i+3] == 'H') cnt += 1;
    }
    printf("%d", cnt);
    return 0;
}