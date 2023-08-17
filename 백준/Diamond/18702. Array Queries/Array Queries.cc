#include <iostream>
#include <cmath> 
#define SIZE 100001
using namespace std;
typedef long long LL;

typedef struct _Node {
	LL max;
	LL min;
	LL sums;

	LL sumLazy;
	LL sqrtLazy;
} node;

node tree[SIZE * 4];
LL arr[SIZE];

inline int readChar();
template<class T = int> inline T readInt();
template<class T> inline void writeInt(T x, char end = 0);
inline void writeChar(int x);
inline void writeWord(const char *s);
static const int buf_size = 1 << 18;
inline int getChar(){
	static char buf[buf_size];
	static int len = 0, pos = 0;
	if(pos == len) pos = 0, len = fread(buf, 1, buf_size, stdin);
	if(pos == len) return -1;
	return buf[pos++];
}
inline int readChar(){
	int c = getChar();
	while(c <= 32) c = getChar();
	return c;
}
template <class T>
inline T readInt(){
	int s = 1, c = readChar();
	T x = 0;
	if(c == '-') s = -1, c = getChar();
	while('0' <= c && c <= '9') x = x * 10 + c - '0', c = getChar();
	return s == 1 ? x : -x;
}
static int write_pos = 0;
static char write_buf[buf_size];
inline void writeChar(int x){
	if(write_pos == buf_size) fwrite(write_buf, 1, buf_size, stdout), write_pos = 0;
	write_buf[write_pos++] = x;
}
template <class T>
inline void writeInt(T x, char end){
	if(x < 0) writeChar('-'), x = -x;
	char s[24]; int n = 0;
	while(x || !n) s[n++] = '0' + x % 10, x /= 10;
	while(n--) writeChar(s[n]);
	if(end) writeChar(end);
}
inline void writeWord(const char *s){
	while(*s) writeChar(*s++);
}
struct Flusher{
	~Flusher(){ if(write_pos) fwrite(write_buf, 1, write_pos, stdout), write_pos = 0; }
}flusher;

node merge(node a, node b) {
	node tmp;
	if (a.max > b.max)
		tmp.max = a.max;
	else
		tmp.max = b.max;

	if (a.min < b.min)
		tmp.min = a.min;
	else
		tmp.min = b.min;

	tmp.sums = a.sums + b.sums;
	tmp.sumLazy = 0;
	tmp.sqrtLazy = 0;
	return tmp;
}
void init(int start, int end, int idx) {
	if (start == end) {
		tree[idx].max = arr[start];
		tree[idx].min = arr[start];

		tree[idx].sums = arr[start];
		tree[idx].sumLazy = 0;
		tree[idx].sqrtLazy = 0;
		return;
	}

	int mid = (start + end) / 2;
	init(start, mid, idx * 2);
	init(mid + 1, end, idx * 2 + 1);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}
void push(int start, int end, int idx) {
	if(tree[idx].sumLazy != 0 || tree[idx].sqrtLazy != 0) {
		if (tree[idx].sqrtLazy == 0) {
			tree[idx].max += tree[idx].sumLazy;
			tree[idx].min += tree[idx].sumLazy;
			tree[idx].sums += (end - start + 1) * tree[idx].sumLazy;

			if (start != end) {
				tree[idx * 2].sumLazy += tree[idx].sumLazy;
				tree[idx * 2 + 1].sumLazy += tree[idx].sumLazy;
			}
		}
		else {
			tree[idx].max = tree[idx].sqrtLazy + tree[idx].sumLazy;
			tree[idx].min = tree[idx].sqrtLazy + tree[idx].sumLazy;
			tree[idx].sums = (end - start + 1) * (tree[idx].sqrtLazy + tree[idx].sumLazy);

			if (start != end) {
				tree[idx * 2].sumLazy = tree[idx].sumLazy;
				tree[idx * 2].sqrtLazy = tree[idx].sqrtLazy;
				tree[idx * 2 + 1].sumLazy = tree[idx].sumLazy;
				tree[idx * 2 + 1].sqrtLazy = tree[idx].sqrtLazy;
			}
		}
	}	

	tree[idx].sumLazy = 0;
	tree[idx].sqrtLazy = 0;
}

void update_sums(int start, int end, int idx, int left, int right, int value) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right) {
		tree[idx].sumLazy += value;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_sums(start, mid, idx * 2, left, right, value);
	update_sums(mid + 1, end, idx * 2 + 1, left, right, value);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

void update_sqrt(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return;
	if (left <= start && end <= right && floor(sqrt(tree[idx].min)) == floor(sqrt(tree[idx].max))) {
		tree[idx].sqrtLazy = floor(sqrt(tree[idx].max));
		push(start, end, idx);
		return;
	}
	if (left <= start && end <= right && tree[idx].min + 1 == tree[idx].max) {
		tree[idx].sumLazy = floor(sqrt(tree[idx].min)) - tree[idx].min;
		push(start, end, idx);
		return;
	}

	int mid = (start + end) / 2;
	update_sqrt(start, mid, idx * 2, left, right);
	update_sqrt(mid + 1, end, idx * 2 + 1, left, right);
	tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
}

LL getSums(int start, int end, int idx, int left, int right) {
	push(start, end, idx);
	if (end < left || right < start) return 0;
	if (left <= start && end <= right) return tree[idx].sums;

	int mid = (start + end) / 2;
	return getSums(start, mid, idx * 2, left, right) + getSums(mid + 1, end, idx * 2 + 1, left, right);
}

int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
	int test = readInt();
	for(int t = 0; t < test; t++) {
		int n = readInt();
        int m = readInt();
		for (int i = 0; i < n; i++) {
        arr[i] = readInt();
    }
    init(0, n - 1, 1);

		for (int i = 0; i < m; i++) {
			int mode = readInt();
            int l = readInt();
            int r = readInt(); 
			if (mode == 3) {
                int x = readInt();
				update_sums(0, n - 1, 1, l - 1, r - 1, x);
			}
			else if (mode == 1) {
				update_sqrt(0, n - 1, 1, l - 1, r - 1);
			}
			else writeInt(getSums(0, n - 1, 1, l - 1, r - 1), '\n');
		}

    if (t != test - 1) {
      for (int idx = 0; idx < 5; idx++) update_sqrt(0, n - 1, 1, 0, n - 1);
      update_sums(0, n - 1, 1, 0, n - 1, -1);
    }
	}
    Flusher();
	return 0;
}