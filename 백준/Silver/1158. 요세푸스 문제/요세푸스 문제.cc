#include <stdio.h>
 
int queue[25000000];
int rear = -1;
int top = -1;
 
int size() { return top - rear; }
int empty() { return (size()) ? 0 : 1; }
int front() { return (empty()) ? -1 : (queue[rear + 1]); }
int back() { return (empty()) ? -1 : (queue[top]); }
void push(int x) { queue[++top] = x; }
int pop() { 
    if (empty()) return -1;
    else return queue[++rear]; 
}
void skip() {
    int x = pop();
    push(x);
}
 
int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++) push(i);

    printf("<");
    while (!empty()) {
        if (size() != n) printf(", ");

        int skip_count = k % size() + (((k % size()) == 0) ? size() : 0);
        for (int i = 0; i < skip_count - 1; i++) skip();
        printf("%d", front());
        rear++;
    }
    printf(">");
    return 0;
}