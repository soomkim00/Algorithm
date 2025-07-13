import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 주어지는 수가 1,000 이하의 자연수
        // 1~1,000 까지 소수 여부를 모두 구해놓기

        // 소수 판별용 배열, 0: 소수, 1:합성수
        int[] prime_number = new int[1001];  // index를 1,000까지 사용하기 위해 0 버림

        prime_number[1] = 1;  // 1은 소수가 아니다 (정의)
        for (int i = 2; i < 1001; i++) {
            if (prime_number[i] == 1) {
                continue;
            }

            int mul = 2;
            while (i * mul <= 1000) {
                prime_number[i * mul] = 1;
                mul++;
            }
        }

        // 입력되는 수에 대해서 소수 판별
        StringTokenizer st = new StringTokenizer(br.readLine());

        int count = 0;
        for (int i = 0; i < N; i++) {
            int temp = Integer.parseInt(st.nextToken());
            if (prime_number[temp] == 0) {
                count++;
            }
        }

        System.out.println(count);
    }
}