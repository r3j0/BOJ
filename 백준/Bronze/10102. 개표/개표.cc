#include <stdio.h>


int main(void) {
	int n;
	char str[17];
	scanf("%d", &n);
	scanf("%s", str);
	
	int idx = 0;
	int a = 0;
	int b = 0;
	while(str[idx] != 0) {
		if(str[idx] == 'A') a += 1;
		else if(str[idx] == 'B') b += 1;
		
		idx += 1;
	}
	
	if (a > b) printf("A");
	else if (a < b) printf("B");
	else printf("Tie");
	return 0;
}