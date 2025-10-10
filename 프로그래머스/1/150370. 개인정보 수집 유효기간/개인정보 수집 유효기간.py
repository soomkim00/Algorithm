def solution(today, terms, privacies):
    answer = []
    
    # 날짜 문자열을 숫자 리스트로 변환하는 함수
    def day_to_number(day):
        return list(map(int, day.split('.')))
    
    # n개월을 더하거나 빼는 함수 (여러 해 이동 가능)
    def cal_month(day_list, diff_month):
        result = day_list[:]
        total_month = result[0] * 12 + result[1]  # 전체 달 수로 변환
        total_month -= diff_month
        result[0] = total_month // 12
        result[1] = total_month % 12
        if result[1] == 0:  # 12월 처리
            result[0] -= 1
            result[1] = 12
        return result

    # 날짜를 숫자 단위(총 일 수)로 변환해 비교하기 쉽게
    def to_days(y, m, d):
        return (y * 12 * 28) + (m * 28) + d  # 모든 달을 28일로 가정 (문제 조건)
    
    today_num = day_to_number(today)
    today_total = to_days(*today_num)
    
    limit_days = dict()
    
    # 각 약관별로 유효기간(개월 단위) 저장
    for term in terms:
        name, month = term.split()
        limit_days[name] = int(month)
    
    # 개인정보별 유효기간 확인
    for i in range(len(privacies)):
        day, name = privacies[i].split()
        day_num = day_to_number(day)
        add_month = limit_days[name]
        
        # 수집일 + 약관개월 → 하루 빼야 함
        total = to_days(*day_num) + (add_month * 28) - 1
        if total < today_total:
            answer.append(i + 1)
    
    return answer
