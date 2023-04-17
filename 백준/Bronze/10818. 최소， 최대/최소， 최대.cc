#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int tmp;
	
	int max = -1000001;
	int min = 1000001;
	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		
		if(max < tmp) max = tmp;
		if(min > tmp) min = tmp;
	}
	
	printf("%d %d", min, max);
	return 0;
}