import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int arr[] = new int[n+1];
        for (int idx = 1; idx <= n; idx++) arr[idx] = idx;

        int i, j;
        for (int t = 0; t < m; t++) {
            i = sc.nextInt();
            j = sc.nextInt();

            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }

        for (int idx = 1; idx <= n; idx++) System.out.print(arr[idx] + " ");
    }
}