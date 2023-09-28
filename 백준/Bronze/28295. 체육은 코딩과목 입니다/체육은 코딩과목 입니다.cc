#include <stdio.h>

int main(void) {
    char dir_alpha[4] = {'N', 'E', 'S', 'W'};
    int dir = 0;
    int tmp;

    for (int i = 0; i < 10; i++) {
        scanf("%d", &tmp);
        if (tmp == 1) dir = (dir + 1) % 4; // 우향우
        else if (tmp == 2) dir = (dir + 2) % 4; // 뒤로 돌아
        else { // 좌향좌
            dir -= 1;
            if (dir == -1) dir = 3;
        }
    }

    printf("%c", dir_alpha[dir]);
    return 0;
}