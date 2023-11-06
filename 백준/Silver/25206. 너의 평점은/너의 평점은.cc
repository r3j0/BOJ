#include <stdio.h>
#include <string.h>

double gradeToScore(char g[5]) {
    if (strcmp(g, "A+") == 0) return 4.5;
    else if (strcmp(g, "A0") == 0) return 4.0;
    else if (strcmp(g, "B+") == 0) return 3.5;
    else if (strcmp(g, "B0") == 0) return 3.0;
    else if (strcmp(g, "C+") == 0) return 2.5;
    else if (strcmp(g, "C0") == 0) return 2.0;
    else if (strcmp(g, "D+") == 0) return 1.5;
    else if (strcmp(g, "D0") == 0) return 1.0;
    else if (strcmp(g, "F") == 0) return 0.0;
}

int main(void) {
    double all_mul = 0.0;
    double all_sum = 0.0;
    for (int i = 0; i < 20; i++) {
        char name[55];
        double score;
        char grade[5];
        scanf("%s %lf %s", name, &score, grade);

        if (strcmp(grade, "P") == 0) continue;
        all_mul += gradeToScore(grade) * score;
        all_sum += score;
    }

    printf("%.6lf", all_mul / all_sum);
    return 0;
}