import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();

        int[] result = new int[26];
        Arrays.fill(result, -1);

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int idx = c - 'a';
            if (result[idx] == -1) {
                result[idx] = i;
            }
        }

        StringBuilder sb = new StringBuilder(60);
        for (int i = 0; i < 26; i++) {
            sb.append(result[i] + " ");
        }
        System.out.println(sb);
    }
}