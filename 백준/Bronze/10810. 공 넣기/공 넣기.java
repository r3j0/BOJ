import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int arr[] = new int[n+1];

        int i, j, k;
        for (int t = 0; t < m; t++) {
            i = sc.nextInt();
            j = sc.nextInt();
            k = sc.nextInt();

            for (int idx = i; idx <= j; idx++) arr[idx] = k;
        }

        for (int idx = 1; idx <= n; idx++) System.out.print(arr[idx] + " ");
    }
}