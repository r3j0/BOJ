#include <stdio.h>

int main(void) {
    int t;
    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        int arr[9][9] = {0,};
        int done = 1;
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) scanf("%d", &arr[i][j]);
        }

        // Garo
        for (int i = 0; i < 9; i++) {
            int now_arr[9] = {0,};
            for (int j = 0; j < 9; j++) now_arr[arr[i][j]-1] = 1;

            for (int j = 0; j < 9; j++) {
                if (now_arr[j] == 0) {
                    done = 0;
                    break;
                }
            }
        }

        // Sero
        for (int j = 0; j < 9; j++) {
            int now_arr[9] = {0,};
            for (int i = 0; i < 9; i++) now_arr[arr[i][j]-1] = 1;

            for (int i = 0; i < 9; i++) {
                if (now_arr[i] == 0) {
                    done = 0;
                    break;
                }
            }
        }

        // Sub-Square
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int now_arr[9] = {0,};
                for (int ni = i * 3; ni < (i + 1) * 3; ni++) {
                    for (int nj = j * 3; nj < (j + 1) * 3; nj++) now_arr[arr[ni][nj]-1] = 1;
                }

                for (int k = 0; k < 9; k++) {
                    if (now_arr[k] == 0) {
                        done = 0;
                        break;
                    }
                }
            }
        }

        if (done) printf("Case %d: CORRECT\n", tc);
        else printf("Case %d: INCORRECT\n", tc);
    }
    return 0;
}