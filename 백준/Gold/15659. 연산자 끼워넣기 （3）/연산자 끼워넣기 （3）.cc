#include <stdio.h>
int n;
int arr[12];
int ope[4];
int ope_order[11] = {0,};

int max_result = 0;
int min_result = 0;
int first_result = 0;

int compute(void) {
    int waiting_queue[12];
    int waiting_queue_size = 0;
    int waiting_ope_queue[12];
    int waiting_ope_queue_size = 0;

    for (int i = 0; i < n - 1; i++) {
        if (2 <= ope_order[i] && ope_order[i] <= 3) {
            if (waiting_queue_size == 0) {
                if (ope_order[i] == 2) {
                    waiting_queue[waiting_queue_size++] = arr[i] * arr[i+1];
                }
                else {
                    waiting_queue[waiting_queue_size++] = arr[i] / arr[i+1];
                }
            }
            else {
                if (ope_order[i] == 2) waiting_queue[waiting_queue_size - 1] *= arr[i+1];
                else waiting_queue[waiting_queue_size - 1] /= arr[i+1];
            }
        }
        else {
            if (waiting_queue_size == 0) {
                waiting_queue[waiting_queue_size++] = arr[i];
                waiting_queue[waiting_queue_size++] = arr[i+1];
                waiting_ope_queue[waiting_ope_queue_size++] = ope_order[i];
            }
            else {
                waiting_queue[waiting_queue_size++] = arr[i+1];
                waiting_ope_queue[waiting_ope_queue_size++] = ope_order[i];
            }
        }
    }

    int result = 0;
    if (waiting_queue_size == 1) { 
        result = waiting_queue[0];
    }
    else {
        for (int i = 0; i < waiting_queue_size - 1; i++) {
            if (i == 0) {
                if (waiting_ope_queue[0] == 0) {
                    result = waiting_queue[0] + waiting_queue[1];
                }
                else {
                    result = waiting_queue[0] - waiting_queue[1];
                }
            }
            else {
                if (waiting_ope_queue[i] == 0) {
                    result += waiting_queue[i + 1];
                }
                else {
                    result -= waiting_queue[i + 1];
                }
            }
        }
    }

    return result;
}

void backtracking(int now) {
    if (now == n - 1) {
        int result = compute();
        if (first_result == 0) {
            first_result = 1;
            max_result = result;
            min_result = result;
        }
        else {
            if (max_result < result) max_result = result;
            if (min_result > result) min_result = result;
        }
        return;
    }

    for (int o = 0; o < 4; o++) {
        if (ope[o] > 0) {
            ope_order[now] = o; 
            ope[o] -= 1;
            backtracking(now + 1);
            ope[o] += 1;
            ope_order[now] = 0;
        }
    }
}

int main(void) {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    for (int i = 0; i < 4; i++) scanf("%d", &ope[i]);

    backtracking(0);
    printf("%d\n%d", max_result, min_result);
    return 0;
}