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
        long b = Long.parseLong(st.nextToken());

        ArrayList<ArrayList<Long>> matrix = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            matrix.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                matrix.get(i).add(Long.parseLong(st.nextToken()) % 1000L);
            }
        }

        // Input End
        br.close();

        // Solve : Divide and Conquer
        matrix = power(matrix, n, b);

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bw.write(matrix.get(i).get(j) + " ");
            }
            bw.write("\n");
        }
        bw.flush();

        // Output End
        bw.close();
    }

    public static ArrayList<ArrayList<Long>> power(ArrayList<ArrayList<Long>> m, int n, long b) {
        if (b == 1) return m;

        ArrayList<ArrayList<Long>> tmp = power(m, n, b / 2);
        tmp = mul(n, tmp, tmp);
        if (b % 2 == 1) tmp = mul(n, tmp, m);
        return tmp;
    }

    public static ArrayList<ArrayList<Long>> mul(int n, ArrayList<ArrayList<Long>> a, ArrayList<ArrayList<Long>> b) {
        ArrayList<ArrayList<Long>> c = new ArrayList<>();
        long mod = 1000L;

        for (int i = 0; i < n; i++) {
            c.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                long now = 0L;
                for (int k = 0; k < n; k++) {
                    now = (now + (a.get(i).get(k) * b.get(k).get(j))) % mod;
                }

                c.get(i).add(now);
            }
        }

        return c;
    }
}