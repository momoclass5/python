# hello() : '어서오세요'를 출력 하는 함수 
def hello() :
    print('어서오세요')

hello()
print(hello()) # 반환이 없는 함수는 None을 반환

# hello(name) : 'ㅇㅇ님 환영합니다.'를 출력 하는 함수
def hello(name, age) : 
    print(f'{name}님({age}) 환영 합니다.')

# hello() 오류
hello('박서현', 13)
# 매개변수의 이름으로 값을 넣는 방법
hello(age = 13, name="박서현")

# gugudan(dan) : 단에 해당하는 구구만을 출력
def gugudan(dan) : 
    for i in range(1, 10) : 
        print(f'{dan} * {i} = {dan * i}')
        
gugudan(2)

def add(a, b) : 
    return a + b

# add(a,b) : 두수의 합을 반환 하는 함수
print(f'add(10, 10) : {add(10, 10)}')

def test() :
    # 함수종료 -> None가 반환
    return


# 함수 만들기
# 주민등록번호를 입력받아서 성별을 반환하는 함수
name, age = ['박서현', 13]
def getGender(ssn) : 
    # 유효성검증
    ssn = str(ssn)
    ssn = ssn.replace('-', '')
    if not ssn.isnumeric() :
        print('숫자만 입력 가능 합니다.')
        return
    if len(ssn) != 13 :
        print('주민등록 번호는 13자리로 입력 해주세요')
        return 
    # 1111114444444 : 13자리 숫자
    # 오류가 발생하지 않도록 문자로 형변환
    if ssn[6] not in ['1','2','3','4'] :
        print('주민번호 형식에 일치 하지 않습니다.')
        return 
    if ssn[6] in ['1','3'] :
        return '남'
    if ssn[6] in ['2','4'] :
        return '여'

print('성별 : ', getGender('1111113222222'))
print('성별 : ', getGender(1111113222222))
print('성별 : ', getGender(1111))

print("=" *20, 'getAge()')
# 주민등록번호를 입력받아서 나이를 반환하는 함수
from datetime import datetime
def getAge(ssn) : 
    # now() : 현재 날자와 시간을 반환
    res = 0
    yyyy = datetime.now().year
    yy = ssn[:2]
    if ssn[6] in ['1','2'] : 
        yy = '19' + yy
    elif ssn[6] in ['3','4'] :
        yy = '20' + yy
    else :
        print('주민등록 번호 형식에 맞지 않습니다.')
        return res
    print('올해년도 : ', yyyy)
    print('태어난 년도 : ', yy )
    res = yyyy - int(yy)
    print('나이 : ', age)
    return res

getAge('1111114444444')
print('='*20, 'getInfo()')

def getInfo(name, ssn) : 
    # 이름, 나이, 주민번호를 반환
    name = name
    # 함수를 호출 하여 나이와 성별을 반환 받아 변수에 저장
    age = getAge(ssn)
    gender = getGender(ssn)
    
    info = [name, age, gender]
    return info
    
a, b, c = getInfo('박서현', '1111113333333')
print(f'이름 : {a}, 나이 : {b}, 성별 : {c}')

# 이름과, 주민등록번호를 입력받아서 이름, 성별, 나이를 반환하는 함수
# getGender()
print("=" *20)


# 계산기 - 입력이 잘못된경우 0을 반환
def cacl(operator, num1, num2) :
    # operator : +-*/%
    if operator not in ['+', '-', '*', '/', '%'] :
        return 0
    # .isnumeric() : 문자열이 가지고 있는 함수
    # 문자열인 경우에만 사용이 가능 
    # 타입이 다른 경우 사용 할 수 없음
    #   AttributeError: 'int' object has no attribute 'isnumeric'
    # 함수에 괄호를 붙이지 않았을 때
    #   <built-in method isnumeric of str object at 0x0000026C06345050>
    print('================', str(num1).isnumeric() )
    if operator == '+' : 
        return num1 + num2
    elif operator == '-' : 
        return num1 - num2
    elif operator == '*' : 
        return num1 * num2
    elif operator == '/' : 
        return num1 / num2
    elif operator == '%' : 
        return num1 % num2
    
print('calc(+,10,100)', cacl('+', 10, 100))

# 평균을 구해 봅시다
def avg(*numbers) :
    print('numbers', numbers)
    #return sum(numbers)/len(numbers)
    sum = 0
    for num in numbers : 
        sum +=num
    return sum/len(numbers)
print('avg : ', avg(1,2,3,4,5,6,7,8,9,10))


# 리스트, 튜플, 딕셔너리, set
# bool()
# datetime
# random
# 함수(def, 매개변수, 반환)


# pip 환경변수 
# : 어느경로에서든지 명령어를 실행 할수 있도록 하는 작업
pip install matplotlib
pip list