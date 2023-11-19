#include <stdio.h>

typedef struct _TEAM {
    int number;
    int distance;
    int rank;
} Team;
Team t[9];

char map[55][55];
int main(void) {
    for (int i = 0; i < 9; i++) {
        t[i].number = i + 1;
        t[i].distance = 0;
        t[i].rank = 0;
    }

    int r, c;
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) scanf("%s", map[i]);

    for (int i = 0; i < r; i++) {
        for (int j = c - 1; j >= 0; j--) {
            if ('1' <= map[i][j] && map[i][j] <= '9')
                t[map[i][j] - '1'].distance = c - j;
        }
    }

    // Selection Sort - Distance
    for (int i = 0; i < 8; i++) {
        int min = i;
        for (int j = i + 1; j < 9; j++) {
            if (t[min].distance > t[j].distance) min = j;
        }

        if (min != i) {
            Team tmp = t[min];
            t[min] = t[i];
            t[i] = tmp;
        }
    }

    int rankCnt = 1;
    t[0].rank = 1;
    for (int i = 1; i < 9; i++) {
        if (t[i-1].distance != t[i].distance) rankCnt += 1;
        t[i].rank = rankCnt;
    }

    // Selection Sort - Number
    for (int i = 0; i < 8; i++) {
        int min = i;
        for (int j = i + 1; j < 9; j++) {
            if (t[min].number > t[j].number) min = j;
        }

        if (min != i) {
            Team tmp = t[min];
            t[min] = t[i];
            t[i] = tmp;
        }
    }

    for (int i = 0; i < 9; i++)
        printf("%d\n", t[i].rank);

    return 0;
}