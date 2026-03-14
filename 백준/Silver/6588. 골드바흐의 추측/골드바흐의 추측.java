import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static final int MAX = 1_000_001;
    public static void main(String[] args) throws IOException {
        // Preprocessing
        boolean[] prime = new boolean[MAX];
        prime[1] = true;
        for (int i = 2; i < MAX; i++) {
            for (int j = 2; i * j < MAX; j++) {
                prime[i * j] = true;
            }
        }

        // Input Output Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;

            for (int i = 3; i <= n / 2; i += 2) {
                if (!prime[i] && !prime[n - i]) {
                    bw.write(n + " = " + i + " + " + (n - i) + "\n");
                    break;
                }
            }
        }

        bw.flush();

        // Input Output End
        br.close();
        bw.close();
    }
}
