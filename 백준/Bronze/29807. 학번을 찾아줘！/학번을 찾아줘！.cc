#include <stdio.h>

int main(void) {
    //국어 > 영어 국어 -영어) * 508  x = *108
    //수학 ? 탐구 수학 - 탐구 * 212   x =  *305
    //외국어 응시 외국어 * 707
    //세 값 * 4763
    int t;
    int arr[10];
 
    scanf("%d", &t);
    for (int i = 0; i < 10; i++) {
        arr[i] = 0;
    }
 
    for (int i = 0; i < t; i++) {
        scanf("%d", &arr[i]);
    }
    int a, b, c;
    if (arr[0] > arr[2]) {
        a = (arr[0] - arr[2]) * 508;
    }
    else a = (arr[2] - arr[0]) * 108;
    
    if (arr[1] > arr[3]) {
        b = (arr[1] - arr[3]) * 212;
    }
    else b = (arr[3] - arr[1]) * 305;

    if (arr[4] != 0)  c = arr[4] * 707;
    else c = 0;

    int result;
    result = (a + b + c) * 4763;

    printf("%d", result);
    return 0;
}