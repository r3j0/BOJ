#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
   int a, n;
   scanf("%d %d", &a, &n);
   char arr[100];

   int i = 0;

   if (a == 0) {
      arr[0] = 48;
      i++;
   }
   int mod;
   while (a > 0) {
      mod = a % n;
      a /= n;

      if (mod < 10)
         mod += 48;
      else
         mod += 55;

      arr[i] = (char)mod;
      i++;
   }

   for (i -= 1; i >= 0; i--)
      printf("%c", arr[i]);
}