#include <stdio.h>
#include <string.h>

int power(int n, int k) {
    if (k == 0) return 1;
    else return n * power(n, k - 1);
}

int getIdx(int n, int idx) {
    if (idx == 0) return n % 10;
    else return getIdx(n / 10, idx - 1);
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    int n_size = 0;
    while ((power(10, n_size)) <= n) n_size += 1;

    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = n_size - 1; j >= 0; j--) {
            printf("%d", getIdx(n, j));
            count += 1;
            if (count == m) break;
        }
        if (count == m) break;
    }

    return 0;
}