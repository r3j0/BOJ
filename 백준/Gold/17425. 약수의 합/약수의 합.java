// 17425 : 약수의 합
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static final int MAX = 1_000_001;
    public static void main(String[] args) throws IOException {
        // Solve
        long[] arr = new long[MAX];
        for (int i = 1; i < MAX; i++) {
            for (int j = 1; i * j < MAX; j++) {
                arr[i * j] += (long)i;
            }
        }

        long[] sarr = new long[MAX];
        for (int i = 1; i < MAX; i++) {
            sarr[i] = sarr[i-1] + arr[i];
        }

        // Input - Output Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            bw.write(sarr[n] + "\n");
        }

        bw.flush();

        // Input - Output End
        br.close();
        bw.close();
    }
}