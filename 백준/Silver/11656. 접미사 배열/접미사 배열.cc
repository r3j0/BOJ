#include <stdio.h>
#include <string.h>

char str[1005];
char arr[1005][1005];
int main(void) {
    scanf("%s", str);
    int strSize = strlen(str);
    for (int i = 0; i < strSize; i++) {
        char* ptr = str+i;
        strcpy(arr[i], ptr);
    }

    // Selection Sort
    for (int i = 0; i < strSize - 1; i++) {
        int min = i;
        for (int j = i + 1; j < strSize; j++) {
            if (strcmp(arr[min], arr[j]) > 0) min = j;
        }

        if (min != i) {
            char tmp[1005];
            strcpy(tmp, arr[min]);
            strcpy(arr[min], arr[i]);
            strcpy(arr[i], tmp);
        }
    }

    for (int i = 0; i < strSize; i++) printf("%s\n", arr[i]);
    return 0;
}