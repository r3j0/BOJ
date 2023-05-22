#include <stdio.h>
#include <stdlib.h>

char str[800005];

int main(void) {
	int n;
	scanf("%d", &n);
	scanf("%s", str);
	
	int idx = 0;
	int se = 0;
	int bi = 0;
	while(str[idx] != 0) {
		if (str[idx] == 's') {
			se += 1;
			idx += 8;
		}
		else {
			bi += 1;
			idx += 7;
		}
	}
	
	if(se > bi) printf("security!");
	else if (se < bi) printf("bigdata?");
	else printf("bigdata? security!");
	
	return 0;
}