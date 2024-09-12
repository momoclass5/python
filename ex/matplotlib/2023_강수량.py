# 강수량 파일을 읽어서 모두 출력 해봅시다

x=[]
y=[]
# 파일이 없는경우 오류 발생
f = open('ex/2023_강수량.csv', 'r', encoding='utf=8')

title = f.readline()  
while True :
    # 더이상 읽을것이 없으면 빈문자열을 반환
    line = f.readline()  
    print('line=====', line)
    
    # 빈값은 false를 반환
    if not line : break
    
    # 전개문법을 사용 할 경우 
    # 값의 갯수가 맞지 않으면 오류가 발생 할수 있다
    # 빈 값이 반환되면 반복문을 종료 하도록 처리 
    a, b, c = line.split(',')
    
    x.append(a.replace('2023-',''))
    # 줄바꿈 제거, 숫자(실수)로 변환
    y.append(float(c.replace('\n', '')))
    
print(x)
print(y)

# 그래프로 출력하기
import matplotlib.pyplot as plt

# 한글깨짐 해결
# 맷플롭에서 사용하는 폰트를 한글폰트로 변경
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 데이터 설정, 점모양, 선모양, 선색
plt.plot(x, y)

# 제목
plt.title('2023년 월별 강수량')
# 축제목
plt.xlabel('월')
plt.ylabel('강수량(mm)')
# 범례
plt.legend('2023')

# 차트 보여줘
plt.show()

