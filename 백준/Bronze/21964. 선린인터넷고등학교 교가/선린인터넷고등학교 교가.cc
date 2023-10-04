#include <stdio.h>

char str[100001];

int main(void) {
   int n;
   scanf("%d", &n);
   scanf("%s", str);

   for (int i = 0; i < 5; i++) printf("%c", str[n-5+i]);
   return 0;
}