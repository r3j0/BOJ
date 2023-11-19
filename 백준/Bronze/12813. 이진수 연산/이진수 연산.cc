#include <stdio.h>
#include <string.h>

char a[100005];
char b[100005];
int main(void) {
    scanf("%s", a);
    scanf("%s", b);
    int size = strlen(a);

    // A & B
    for (int i = 0; i < size; i++) {
        if (a[i] == '1' && b[i] == '1') printf("1");
        else printf("0");
    }
    printf("\n");

    // A | B
    for (int i = 0; i < size; i++) {
        if (a[i] == '0' && b[i] == '0') printf("0");
        else printf("1");
    }
    printf("\n");

    // A ^ B
    for (int i = 0; i < size; i++) {
        if (a[i] != b[i]) printf("1");
        else printf("0");
    }
    printf("\n");

    // ~A
    for (int i = 0; i < size; i++) {
        if (a[i] == '0') printf("1");
        else printf("0");
    }
    printf("\n");

    // ~B
    for (int i = 0; i < size; i++) {
        if (b[i] == '0') printf("1");
        else printf("0");
    }
    
    return 0;
}