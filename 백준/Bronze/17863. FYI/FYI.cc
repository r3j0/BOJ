#include <stdio.h>

int main(void) {
    char phone[10];
    scanf("%s", phone);
    if (phone[0] == '5' && phone[1] == '5' && phone[2] == '5') printf("YES");
    else printf("NO");
    return 0;
}