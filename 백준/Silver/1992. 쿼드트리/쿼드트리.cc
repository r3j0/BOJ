#include <stdio.h>
#define SIZE 66

char movie[SIZE][SIZE];

int zeroPrefixSum[SIZE][SIZE] = {0,};
int onePrefixSum[SIZE][SIZE] = {0,};

void start(int start_y, int start_x, int end_y, int end_x) {
    int now = (end_x + 1 - start_x) * (end_x + 1 - start_x);
    
    int now_zero = zeroPrefixSum[end_y][end_x];
    if(start_x > 0) now_zero -= zeroPrefixSum[end_y][start_x-1];
    if(start_y > 0) now_zero -= zeroPrefixSum[start_y-1][end_x];
    if(start_x > 0 && start_y > 0) now_zero += zeroPrefixSum[start_y-1][start_x-1];

    if (now_zero == now) {
        printf("0");
        return;
    }

    int now_one = onePrefixSum[end_y][end_x];
    if(start_x > 0) now_one -= onePrefixSum[end_y][start_x-1];
    if(start_y > 0) now_one -= onePrefixSum[start_y-1][end_x];
    if(start_x > 0 && start_y > 0) now_one += onePrefixSum[start_y-1][start_x-1];

    if (now_one == now) {
        printf("1");
        return;
    }

    printf("(");
    start(start_y, start_x, (end_y + start_y) / 2, (end_x + start_x) / 2);
    start(start_y, (end_x + start_x) / 2 + 1, (end_y + start_y) / 2, end_x);
    start((end_y + start_y) / 2 + 1, start_x, end_y, (end_x + start_x) / 2);
    start((end_y + start_y) / 2 + 1, (end_x + start_x) / 2 + 1, end_y, end_x);
    printf(")");
}

int main(void) {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%s", movie[i]);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i > 0) {
                zeroPrefixSum[i][j] += zeroPrefixSum[i-1][j];
                onePrefixSum[i][j] += onePrefixSum[i-1][j];
            }
            if (j > 0) {
                zeroPrefixSum[i][j] += zeroPrefixSum[i][j-1];
                onePrefixSum[i][j] += onePrefixSum[i][j-1];
            }
            if (i > 0 && j > 0) {
                zeroPrefixSum[i][j] -= zeroPrefixSum[i-1][j-1];
                onePrefixSum[i][j] -= onePrefixSum[i-1][j-1];
            }

            if (movie[i][j] == '0') zeroPrefixSum[i][j] += 1;
            else onePrefixSum[i][j] += 1;
        }
    }

    start(0, 0, n - 1, n - 1);

    return 0;
}