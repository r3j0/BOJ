import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static int[] stack;
    public static int top = 0;

    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // Input End
        br.close();

        // Solve
        ArrayList<Character> ans = new ArrayList<>();
        stack = new int[n+1];
        int cnt = 1;
        boolean done = true;
        for (int i = 0; i < n; i++) {
            // Push
            while (empty() || stack[top - 1] < arr[i]) {
                push(cnt++);
                ans.add('+');
            }

            // Pop
            int now = 0;
            while (!empty() && stack[top - 1] >= arr[i]) {
                now = pop();
                ans.add('-');
            }

            if (now != arr[i]) {
                done = false;
                break;
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        if (!done) bw.write("NO");
        else {
            for (char c : ans) {
                bw.write(c + "\n");
            }
        }
        bw.flush();

        // Output ENd
        bw.close();
    }

    public static void push(int x) {
        stack[top++] = x;
    }

    public static int pop() {
        if (empty()) return -1;
        return stack[--top];
    }

    public static boolean empty() {
        if (top == 0) return true;
        return false;
    }
}