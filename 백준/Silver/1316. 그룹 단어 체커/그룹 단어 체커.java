import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (isGroupWord(br.readLine())) {
                count++;
            }
        }
        System.out.println(count);
    }

    public static boolean isGroupWord(String str) {
        boolean[] visited = new boolean[26];
        char prev = 0;

        for (int i = 0; i < str.length(); i++) {
            char curr = str.charAt(i);

            if (prev != curr) {
                if (visited[curr - 'a']) {
                    return false;
                }
                visited[curr - 'a'] = true;
                prev = curr;
            }
        }
        return true;
    }
}