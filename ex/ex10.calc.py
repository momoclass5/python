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
    if not ssn.isnumeric :
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
    age = getAge(ssn)
    print(age)
    
    info = [name, age]
    return info
    
getInfo('박서현', '1111113333333')

# 이름과, 주민등록번호를 입력받아서 이름, 성별, 나이를 반환하는 함수
# getGender()
print("=" *20)




# 함수를 만들어 봅시다
# 함수명 : calc(operator, *args)
#   operator : 연산자
#   args : 숫자가 저장된 튜플
def calc(*args) :
    res = 0
    # *을 사용하면 튜플로 값을 받아온다
    # 매개변수를 넣지 않으면 빈 튜플로 처리된다
    print(args)
    # args의 요수의 갯수는 2개 이상이여야 한다 
    print('len(args) : ', len(args))
    if len(args) < 2 :
        print('수를 2개 이상 입력 해주세요')
        return res
    
    # 튜플에 있는 요소들의 합계를 구하는 반복문
    for num in args : 
        res += num
    # operator : +-*/%
    return res

# 매개변수를 넣지 않아도 오류가 발생 되지 않는다
print('calc() : ', calc())
print('calc() : ', calc(1,2))