#include <stdio.h>
#include <string.h>

int doby_strcmp(char* a, char* b) {
    int idx = 0;
    int a_len = strlen(a);
    int b_len = strlen(b);
    while (idx < a_len || idx < b_len) {
        int a_so = 0;
        int b_so = 0;
        if ('a' <= a[idx] && a[idx] <= 'z') a_so = 32; // 소문자 -> 대문자
        if ('a' <= b[idx] && b[idx] <= 'z') b_so = 32; // -32

        // a_so 가 0이면, a[idx] - 0이 되어 대문자 유지
        // a_so 가 32이면, a[idx] - 32이 되어 소문자가 대문자가 됨.

        if (a[idx] - a_so < b[idx] - b_so) return 1; // a가 사전순으로 더 앞선다.
        else if (a[idx] - a_so > b[idx] - b_so) return 0; // b가 사전순으로 더 앞선다.

        idx += 1;
    }

    return 0; // 똑같다.
}

int main(void) {
    while(1) {
        int n;
        scanf("%d", &n);
        if (n == 0) break;

        char min_word[25];
        char tmp[25];

        scanf("%s", min_word);
        for (int i = 0; i < n - 1; i++) {
            scanf("%s", tmp);
            if (doby_strcmp(tmp, min_word)) strcpy(min_word, tmp);
        }

        printf("%s\n", min_word);
    }
    return 0;
}