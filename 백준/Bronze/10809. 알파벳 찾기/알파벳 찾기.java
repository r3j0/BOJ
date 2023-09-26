import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int alpha[] = new int[26];
        for (int i = 0; i < s.length(); i++) {
            if (alpha[s.charAt(i) - 'a'] == 0) alpha[s.charAt(i) - 'a'] = i + 1;
        }

        for (int i = 0; i < 26; i++) {
            System.out.print((alpha[i] - 1) + " ");
        }
    }
}