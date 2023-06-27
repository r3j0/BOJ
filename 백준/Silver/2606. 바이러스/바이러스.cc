#include <stdio.h>

int line[101][101] = { 0, };
int visit[101] = { 0, };

int computer;
int linenumber;

void movemovemove(int go) {
	for (int i = 1; i <= computer; i++) {
		if (line[go][i] == 1 && visit[i] == 0) {
			visit[i] = 1;
			movemovemove(i);
		}
	}
}

int main(void) {
	int go = 1;
	scanf("%d", &computer);
	scanf("%d", &linenumber);
	for (int i = 0; i < linenumber; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		line[a][b] = 1;
		line[b][a] = 1;
	}
	visit[go] = 1;
	movemovemove(go);
	int cnt = 0;
	for (int i = 2; i <= computer; i++) {
		if (visit[i] == 1)
			cnt++;
	}
	printf("%d", cnt);
	return 0;
}