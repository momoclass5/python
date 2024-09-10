from datetime import datetime

# 현재 날자와 시간을 가지고 오기
now = datetime.now()
# 모듈이름에 .을 붙이면
# 모듈이 가지고 있는 함수, 변수를 사용 할 수 있다
print(now)   # 현재 시간날자
print(now.date())   # 현재 시간날자
print(now.year)   # 현재 년
print(now.month)   # 현재 월
print(now.day)   # 현재 일
print(now.hour)   # 현재 시간
print(now.minute)   # 현재 분
print(now.second)   # 현재 초
print("-" * 20)
print(now.strftime("%Y-%m-%d(%a) %H:%M:%S"))

# 2024-12-25 일이 무슨 요일인지 출력 해봅시다
day = datetime(2024, 12, 24)
print(day.strftime("%a"))

# 한글설정
import locale
locale.setlocale(locale.LC_TIME, 'ko_KR.UTF-8')
print(day.strftime("%a"))
print(day.strftime("%A"))

# 날자연산
from datetime import datetime, timedelta
# timedelta
#   datetime 모듈에서 제공하는 클래스
#   날짜와 시간의 연산을 간편하게 처리

# 함수를 호출 할때 매개변수의 이름을 지정 하면 
# 매개변수의 순서에 상관없이 값을 넣어줄 수 있다
nextDay = now + timedelta(days=1) # 다음날
print(f'내일 : {nextDay}')

# 사용자의 입력일로 부터 7일 후 날자를 출력
input_day = input('대여일(yyyy-mm-dd) : ')
# datetime(년,월,일)
list_day = input_day.split('-')
day = datetime(int(list_day[0]), int(list_day[1]), int(list_day[2]))
returnDay = day + timedelta(days=7)
print(returnDay)
print(returnDay.strftime("%Y-%m-%d(%a)"))