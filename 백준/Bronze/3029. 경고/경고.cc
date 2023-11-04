#include <stdio.h>

int main(void) {
    int start_h, start_m, start_s, end_h, end_m, end_s;
    scanf("%d:%d:%d", &start_h, &start_m, &start_s);
    scanf("%d:%d:%d", &end_h, &end_m, &end_s);

    start_s += (start_m) * 60 + (start_h) * 3600;
    end_s += (end_m) * 60 + (end_h) * 3600;
    int result = end_s - start_s;

    if (result <= 0) result += 86400;
    printf("%02d:%02d:%02d", result/3600, result%3600/60, result%60);
    return 0;
}