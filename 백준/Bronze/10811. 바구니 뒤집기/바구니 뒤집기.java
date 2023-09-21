import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int arr[] = new int[101];
        int tmp[] = new int[101];

        for (int i = 1; i <= n; i++) arr[i] = i;

        for (int i = 0; i < m; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();

            for (int k = start; k <= end; k++) tmp[end-(k-start)] = arr[k];
            for (int k = start; k <= end; k++) arr[k] = tmp[k];
        }

        for (int i = 1; i <= n; i++) System.out.print(arr[i] + " ");
    }
}