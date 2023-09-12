#include <stdio.h>

int main(void) {
    int n, x; scanf("%d %d", &n, &x);

    int tmp;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        if (tmp < x) printf("%d ", tmp);
    }
    return 0;
}