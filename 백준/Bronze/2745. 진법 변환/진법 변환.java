import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String n = st.nextToken();
        int b = Integer.parseInt(st.nextToken());

        int result = 0;
        for (int i = 0; i < n.length(); i++) {
            char c = n.charAt(i);
            int value = 0;

            if (c >= 'A' && c <= 'Z') {
                value = c - 'A' + 10;
            } else {
                value = c - '0';
            }

            result = result * b + value;
        }

        System.out.println(result);
    }
}