// 1600 : 말이 되고픈 원숭이
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Node {
    int y, x, cnt;
    public Node (int y, int x, int cnt) {
        this.y = y;
        this.x = x;
        this.cnt = cnt;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int[][] board = new int[h][w];
        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // Input End
        br.close();

        // Solve
        int answer = -1;

        boolean[][][] vis = new boolean[h][w][k+1];
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0, 0, 0));

        int[] dy = new int[]{-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1};
        int[] dx = new int[]{0, 0, -1, 1, -2, -1, 1, 2, 2, 1, -1, -2};

        int result = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                Node now = q.poll();
                if (now.y == h - 1 && now.x == w - 1) {
                    answer = result;
                    break;
                }

                for (int d = 0; d < 12; d++) {
                    if (d >= 4 && now.cnt == k) break;
                    int ny = now.y + dy[d];
                    int nx = now.x + dx[d];
                    int nc = now.cnt + ((d >= 4) ? 1 : 0);
                    if (0 <= ny && ny < h && 0 <= nx && nx < w && !vis[ny][nx][nc] && board[ny][nx] == 0) {
                        vis[ny][nx][nc] = true;
                        q.add(new Node(ny, nx, nc));
                    }
                }
            }
            if (answer != -1) break;
            result += 1;
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();

    }
}