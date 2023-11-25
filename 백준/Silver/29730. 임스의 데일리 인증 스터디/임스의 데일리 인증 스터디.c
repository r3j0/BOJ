#include <stdio.h>
#include <string.h>

int strlencmp(char* a, char* b) {
    if (strlen(a) > strlen(b)) return -1;
    else if (strlen(a) < strlen(b)) return 1;
    else {
        for (int i = 0; i < strlen(a); i++) {
            if (a[i] < b[i]) return 1;
            else if (a[i] > b[i]) return -1;
        }
    }

    return 0;
}

int toint(char* str) {
    int now = 0;
    for (int i = 0; i < strlen(str); i++) {
        now *= 10;
        now += str[i] - '0';
    }

    return now;
}

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();

    char arr[1001][105];
    int arrSize = 0;

    char boj[1001][105];
    int bojSize = 0;
    char bojstr[105] = "boj.kr/";
    for (int i = 0; i < n; i++) {
        char now[105];
        gets(now);

        char boj_tmp[105];
        strcpy(boj_tmp, now);
        boj_tmp[7] = 0;

        if (!strcmp(boj_tmp, bojstr)) {
            char* boj_ptr = now+7;
            strcpy(boj[bojSize++], boj_ptr);
        }
        else {
            strcpy(arr[arrSize++], now);
        }
    }

    // Selection Sort - arr
    for (int i = 0; i < arrSize - 1; i++) {
        int min = i;
        for (int j = i + 1; j < arrSize; j++) {
            if (strlencmp(arr[min], arr[j]) < 0) min = j;
        }

        if (min != i) {
            char tmp[105];
            strcpy(tmp, arr[min]);
            strcpy(arr[min], arr[i]);
            strcpy(arr[i], tmp);
        }
    }

    // Selection Sort - boj
    for (int i = 0; i < bojSize - 1; i++) {
        int min = i;
        for (int j = i + 1; j < bojSize; j++) {
            if (toint(boj[min]) > toint(boj[j])) min = j;
        }

        if (min != i) {
            char tmp[105];
            strcpy(tmp, boj[min]);
            strcpy(boj[min], boj[i]);
            strcpy(boj[i], tmp);
        }
    }

    for (int i = 0; i < arrSize; i++) printf("%s\n", arr[i]);
    for (int i = 0; i < bojSize; i++) printf("%s%s\n", bojstr, boj[i]);
    return 0;
}