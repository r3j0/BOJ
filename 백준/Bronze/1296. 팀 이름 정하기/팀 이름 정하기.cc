#include <stdio.h>
#include <string.h>

typedef struct _TEAM {
    char name[30];
    int winable;
} Team;

int main(void) {
    char search[5] = "LOVE";

    char yeondu[30];
    int yeondu_count[4] = {0,}; // L, O, V, E;
    scanf("%s", yeondu);
    for (int i = 0; i < strlen(yeondu); i++) {
        for (int j = 0; j < 4; j++) {
            if (yeondu[i] == search[j]) {
                yeondu_count[j] += 1;
                break;
            }
        }
    }

    int n;
    Team t[50];

    scanf("%d", &n);
    getchar();
    for (int i = 0; i < n; i++) {
        scanf("%s", t[i].name);
        t[i].winable = 0;
        
        int count[4] = {0,};
        for (int j = 0; j < strlen(t[i].name); j++) {
            for (int k = 0; k < 4; k++) {
                if (t[i].name[j] == search[k]) {
                    count[k] += 1;
                    break;
                }
            }
        }       

        for (int j = 0; j < 3; j++) {
            for (int k = j + 1; k < 4; k++) {
                if (j == 0 && k == 1)
                    t[i].winable = ((yeondu_count[j] + count[j]) + (yeondu_count[k] + count[k]));
                else
                    t[i].winable *= ((yeondu_count[j] + count[j]) + (yeondu_count[k] + count[k]));
            }
        }
        t[i].winable %= 100;
    }

    // Selection Sort
    for (int i = 0; i < n - 1; i++) {
        int max = i;
        for (int j = i + 1; j < n; j++) {
            if (t[max].winable < t[j].winable || (t[max].winable == t[j].winable && strcmp(t[max].name, t[j].name) > 0)) max = j;
        }

        if (max != i) {
            Team tmp = t[max];
            t[max] = t[i];
            t[i] = tmp;
        }
    }

    printf("%s", t[0].name);
    return 0;
}