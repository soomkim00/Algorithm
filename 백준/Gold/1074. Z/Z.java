import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		int s_r = 0;
		int s_c = 0;
		int count = 0;

		while (true) {
			if (s_r == r && s_c == c) {
				System.out.println(count);
				return;
			}

			int m_r = s_r + (1 << (n - 1));
			int m_c = s_c + (1 << (n - 1));
			int z = 0;

			if (r < m_r && c >= m_c) {
				z = 1;
				s_c = m_c;
			} else if (r >= m_r && c < m_c) {
				z = 2;
				s_r = m_r;
			} else if (r >= m_r && c >= m_c) {
				z = 3;
				s_r = m_r;
				s_c = m_c;
			}

			count += z * (int) Math.pow(4, n-1);
			n--;
		}
	}
}