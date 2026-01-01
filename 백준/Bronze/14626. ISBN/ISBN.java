import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();

		int starIdx = -1; // '*'의 위치 저장
		int currentSum = 0; // '*'를 제외한 나머지 숫자들의 가중치 합

		for (int i = 0; i < 13; i++) {
			char c = input.charAt(i);

			if (c == '*') {
				starIdx = i; // 위치 기억
				// '*'는 합계에 더하지 않고 넘어감
			} else {
				int num = c - '0'; // [중요] ASCII 값을 실제 정수로 변환
				if (i % 2 == 0) {
					currentSum += num * 1; // 가중치 1
				} else {
					currentSum += num * 3; // 가중치 3
				}
			}
		}

		// 0부터 9까지 넣어보면서 ISBN 조건(합이 10의 배수)을 만족하는지 확인
		for (int i = 0; i <= 9; i++) {
			int weight = (starIdx % 2 == 0) ? 1 : 3; // '*' 위치의 가중치 결정
			int totalSum = currentSum + (i * weight);

			if (totalSum % 10 == 0) {
				System.out.println(i);
				break; // 정답을 찾으면 출력 후 종료
			}
		}
	}
}