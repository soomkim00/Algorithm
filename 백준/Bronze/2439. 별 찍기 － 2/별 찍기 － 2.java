import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int N = Integer.parseInt(br.readLine());


        for (int i = 1; i <= N; i++) {
            StringBuilder sb = new StringBuilder(N);
            for (int j = 0; j < N - i; j++) {
                sb.append(' ');
            }
            for (int k = 0; k < i; k++) {
                sb.append('*');
            }
            bw.write(String.valueOf(sb) + "\n");
        }
        bw.flush();
    }
}