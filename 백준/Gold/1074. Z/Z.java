import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        // Input End
        br.close();

        // Solve : Recursion
        int answer = solve(n, 0, 0, r, c) - 1;

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static int solve(int n, int xpos, int ypos, int xend, int yend) {
        // Z
        if (n == 0) return 1;
        int cnt = 0;
        int half = (1 << (n - 1));

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                if (xpos + (half * i) <= xend && xend < xpos + (half * (i + 1)) &&
                    ypos + (half * j) <= yend && yend < ypos + (half * (j + 1))) {
                    cnt += solve(n - 1, xpos + (half * i), ypos + (half * j), xend, yend);
                    return cnt;
                }
                else {
                    cnt += half * half;
                }
            }
        }

        return cnt;
    }
}