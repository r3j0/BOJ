#include <stdio.h>
#include <string.h>

char original[100001];
char string[51];
char string_dictionary[51][100];
int string_dictionary_size = 0;
long long dp[51][100001] = {0,};
long long result = 0;

int max(int a, int b) {
    if (a > b) return a;
    else return b;
}

int main(void) {
    gets(original);
    gets(string);
    for (int cnt = 0; cnt < strlen(string); cnt++) {
        char now = string[strlen(string) - 1];
        for (int k = strlen(string) - 1; k > 0; k--) string[k] = string[k-1];
        string[0] = now;

        int can = 1;
        for (int i = 0; i < string_dictionary_size; i++) {
            if (strcmp(string_dictionary[i], string) == 0) {
                can = 0;
                break;
            }
        }

        if (can == 0) continue;

        strcpy(string_dictionary[string_dictionary_size++], string);

        for (int i = 1; i <= strlen(string); i++) {
            for (int j = 1; j <= strlen(original); j++) {
                if (string[i-1] == original[j-1]) {
                    if (i == 1 || dp[i-1][j-1] != 0) dp[i][j] = (max(1, dp[i-1][j-1]) + dp[i][j-1]) % 1000000007;
                    else dp[i][j] = 0;
                }
                else dp[i][j] = dp[i][j-1] % 1000000007;
            }
        }
        result = (result + dp[strlen(string)][strlen(original)]) % 1000000007;
    }

    printf("%lld", result);

    return 0;
}