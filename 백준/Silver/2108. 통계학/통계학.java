import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		int[] count = new int[8001];  // -4,000 ~ 4,000
		// 인덱스 == 숫자 + 4,000, 숫자 == 인덱스 - 4000
		int sum = 0;  // 산술평균 계산용

		for (int i = 0; i < n; i++) {
			int input = Integer.parseInt(br.readLine());
			sum += input;
			count[input + 4000]++;
		}

		System.out.println(Math.round((double)sum / n));  // 산술평균 출력

		// 중앙값
		int midCount = n / 2 + 1;
		// 최빈값
		int oftenVal = 0;  // 최빈수인지 확인
		int oftenCount = 0;  // 두 번째 작은 값 확인
		int oftenIndex = 0;  // 최빈값 저장
		// 최소, 최대값
		int minVal = 8000;
		int maxVal = 0;

		for (int i = 0; i <= 8000; i++) {
			if (count[i] > 0) {
				// 1. 최소값 확인
				if (i < minVal) {
					minVal = i;
				}

				// 2. 중앙값 확인
				if (midCount > 0) {
					midCount -= count[i];
					if (midCount <= 0) {
						System.out.println(i - 4000);  // 중앙값 출력
					}
				}

				// 3. 최빈값 확인
				if (count[i] > oftenVal) {
					oftenVal = count[i];
					oftenCount = 1;
					oftenIndex = i - 4000;
				} else if (count[i] == oftenVal && oftenCount < 2) {
					oftenIndex = i - 4000;
					oftenCount++;
				}
			}
		}

		// 최대값 구하기
		for (int i = 8000; i >= 0; i--) {
			if (count[i] > 0) {
				maxVal = i;
				break;
			}
		}

		System.out.println(oftenIndex);  // 최빈값
		System.out.println(maxVal - minVal);  // 범위
	}
}