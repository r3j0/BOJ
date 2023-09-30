#include <stdio.h>

int main(void) {
    int a,b,min;
    scanf("%d %d",&a,&b);
    if(a<b)
        min = a;
    else
        min = b;
    printf("%d",min/2);
    return 0;
}