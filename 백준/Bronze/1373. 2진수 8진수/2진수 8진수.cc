#include <stdio.h>
#include <string.h>

char n[1000005];
int result[1000005];
int result_size = 0;

int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int main(void) {
    scanf("%s", n);
    int n_size = strlen(n);

    for (int i = n_size - 1; i >= 0; i -= 3) {
        int c = 0;
        int now = 0;
        for (int k = i; k > max(i - 3, -1); k--) {
            now += (n[k] - '0') << c;
            c += 1;
        }
        result[result_size++] = now;
    }

    for (int i = result_size - 1; i >= 0; i--)
        printf("%d", result[i]);
    return 0;
}