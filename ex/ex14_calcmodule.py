# 모든 클래스, 변수를 사용할수 있다
# 코드가 실행되어짐

# 파일의 이름만 작성
# from 파일이름 import 사용할클래스이름
'''
from ex13_calc import 계산기
print('='*20)
# from을 사용하면 이름을 사용하지 않고 접근이 가능
calc = 계산기(1,2)
print(calc.더하기())
'''

# import를 이용할 경우 이름을 붙여서 호출
import ex13_calc
calc = ex13_calc.계산기(1,2)

