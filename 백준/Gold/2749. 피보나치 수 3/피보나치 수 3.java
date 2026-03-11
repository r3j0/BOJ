import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static final long MOD = 1_000_000;

    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());

        // Input End
        br.close();

        // Solve : Divide and Conquer
        long result;
        if (n == 1) result = 1;
        else result = fibo(n - 1)[0][0];

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(result + "\n");
        bw.flush();
        // Output End
        bw.close();
    }

    public static long[][] fibo(long k) {
        if (k == 1) {
            return new long[][]{
                    {1, 1},
                    {1, 0}};
        }

        long[][] tmp = fibo(k / 2).clone();
        long[][] tmp2 = tmp.clone();
        if (k % 2 == 1) tmp2 = mul(tmp2.clone(), fibo(1));

        return mul(tmp, tmp2);
    }

    public static long[][] mul(long[][] a, long[][] b) {
        long[][] c = new long[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    c[i][j] = (c[i][j] + (a[i][k] * b[k][j])) % MOD;
                }
            }
        }

        return c;
    }
}
