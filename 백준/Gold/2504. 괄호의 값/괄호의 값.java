// 2504 : 괄호의 값
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        // Input End
        br.close();

        // Solve : Stack
        int answer = 0;
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') st.push(-4);
            else if (s.charAt(i) == '[') st.push(-9);
            else { // ')', ']'
                // 스택에 있는 A+B 꼴들 더하기
                int now_num = 0;
                while (!st.isEmpty() && st.peek() > 0) {
                    now_num += st.pop();
                }

                // 1. 스택이 비어있거나
                // 2. 동일한 종류의 괄호가 매치되지 않는다면
                // 올바르지 않은 괄호 문자열
                if (st.isEmpty() ||
                    (int)s.charAt(i) / 10 != -st.peek()) {
                    break;
                }

                // 여는 괄호 빼기
                st.pop();

                // now_num이 0이라면 () [] 괄호 문자열 값 스택 추가
                // now_num이 >0 이라면 괄호 문자열 값 곱해서 스택 추가
                st.push((s.charAt(i) == ')' ? 2 : 3) * (now_num > 0 ? now_num : 1));
            }

            // 괄호 문자열을 전부 순회했다면 정답 생성
            if (i == s.length() - 1) {
                while (!st.isEmpty() && st.peek() > 0) {
                    answer += st.pop();
                }

                // 만약 스택이 비어있지 않는다면 여는 괄호가 더 남아있는 것.
                if (!st.isEmpty()) {
                    answer = 0;
                }
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}