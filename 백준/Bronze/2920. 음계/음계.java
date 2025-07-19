import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int check = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int first = Integer.parseInt(st.nextToken());
        for (int i = 1; i < 8; i++) {
            int second = Integer.parseInt(st.nextToken());
            if (second - first == 1 && check != -1) {
                check = 1;
            } else if (second - first == -1 && check != 1) {
                check = -1;
            } else {
                check = 0;
                break;
            }
            first = second;
        }

        switch (check) {
            case 1:
                System.out.println("ascending");
                break;
            case -1:
                System.out.println("descending");
                break;
            default:
                System.out.println("mixed");
                break;
        }

    }
}