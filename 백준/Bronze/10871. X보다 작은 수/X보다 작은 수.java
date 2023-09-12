import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();

        int tmp;
        for (int i = 0; i < n; i++) {
            tmp = sc.nextInt();
            if (tmp < x) System.out.print(tmp + " ");
        }
    }
}