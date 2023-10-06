#include <stdio.h>
char s[100000];
int main(void) {
   int n; scanf("%d", &n);
   scanf("%s", s);

   int arr[26] = {0,}; // 알파벳 등장 횟수를 저장

   for (int i = 0; i < n; i++) 
      arr[s[i] - 'A'] += 1;

   int min = arr[0]; // A
   if (min > arr['H' - 'A']) min = arr['H' - 'A']; // H
   if (min > arr['I' - 'A']) min = arr['I' - 'A']; // I
   if (min > arr['R' - 'A']) min = arr['R' - 'A']; // R
   if (min > arr['C' - 'A']) min = arr['C' - 'A']; // C
   
   printf("%d", min);

   return 0;
}