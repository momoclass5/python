# 포맷 함수 사용하기
input_str1 = '안녕하세요'
input_str2 = '반갑습니다'

# format함수를 이용하여 문자를 대입하는 방법
# 중괄호 안에 인덱스, 이름을 넣어주고 포맷함수에 입력할 값을 넣어준다
# 인덱스로 넣기
print('문자1 : {0}'.format(input_str1))
# 여러개 넣기
print('문자1 : {0}, 문자2 : {1}'.format(input_str1, input_str2))
# 이름으로 넣기
print('문자1 : {str1}, 문자2 : {str2}'.format(str1=input_str1, str2=input_str2))
print('숫자 : {0}'.format(20))

# 정렬
# :<자릿수 왼쪽 정렬
# :>자릿수 오른쪽 정렬
# :^자릿수 가운데 정렬
print('{0:<10}'.format('안녕'))
print('{0:>10}'.format('안녕'))
print('{0:^10}'.format('안녕'))

print('문자열의 길이 : ' , len('안녕'))
# len() 함수의 매개값을로 숫자 타입을 넣으면 오류 발생
# print('문자열의 길이 : ' , len(123)) # 오류

# f 문자열 포매팅
print(f'{"안녕하세요":^10}')
print(f'{input_str1:^10}')
# 비어있는 공간을 채우기
print(f'{input_str1:=^20}')
print(f'{input_str1:0^20}')

# 문자열 관련 함수
# 문자 갯수 세기    문자열.count()
input_str1 = '안녕하하하하하하' 
print(input_str1.count('하')) # 하가 몇개 나왔는지 카운팅
# 문자열 삽입   삽입문자.join(문자열)
print(','.join(input_str1)) # 문자 사이에 ,를 입력
# 위치를 찾는 함수  문자열.find(찾을문자), 문자열.index(찾을문자)
# 문자열에서 찾는 문자의 위치를 반환
print(input_str1.find('하')) # 하가 처음 나오는 위치를 반환 (0부터 시작)
print(input_str1.find('오')) # 찾는 문자가 없다면 -1을 반환
print(input_str1.index('하')) # 하가 처음 나오는 위치를 반환 (0부터 시작)
# 오류발생 으로 주석처리
#print(input_str1.index('오')) # 찾는 문자가 없으면 오류 발생

# 대소문자 변환 = 비교시 사용
# 모두 대문자로 변경 문자열.upper()
# 모두 소문자로 변경 문자열.lower()
str1 = 'hi'
print(str1.upper()) # 반환값이 있는 함수는 값 자체를 변경하지 않음
print(str1)         
str1 = 'HI'
print(str1.lower()) # 반환값이 있는 함수는 값 자체를 변경하지 않음
print('lower(), upper() 함수를 이용해도 기존 변수의 값은 변경되지 않음 str1 : ' + str1)         
# 공백을 제거 하는 함수
# 문자열.strip() : 양쪽 공백을 제거
# 문자열.lstrip() : 왼쪽 공백을 제거
# 문자열.rstrip() : 오른쪽 공백을 제거
str1 = '        안녕        '
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

# 문자열 바꾸기
# 문자열.replace(바꿀문자열, 바뀔문자열)
print(str1.replace("안녕", "정말"))

# 문자열 나누기
# 문자열.split("나눌문자")
# 리스트를 반환
print(str1.split(" "))
str1 = 'a,b,c,d'
# 문자열을 원하는 문자로 끊어서 리스트로 반환
print(str1.split(","))

# 실습 
# 0000001111111
# 13자리인지 체크, 숫자로 변환 가능 한지 체크
# 주민등록 번호를 입력 받아서 성별을 출력하는 프로그램 작성
# 주민등록 번호를 입력 받아서 나이를 출력하는 프로그램 작성
print(str1.isnumeric())
print('주민번호를 13자리 숫자로 입력')
ssn = input('주민등록 번호 : ')
if ssn.isnumeric :
    if len(ssn) == 13 :
        # 추출 로직
        # 1111112222222
        # 주민등록 번호 뒷자리의 첫번째 자리가 1,2,3,4 인지 판단
        print('주민등록번호 뒷자리 첫번째 값 : ' + ssn[6])
        print(type(ssn[6]))
        if int(ssn[6]) in [1,2,3,4] :
            # 성별구하기
            if int(ssn[6]) in [1,3] :
                print('남자')
            elif int(ssn[6]) in [2,4] :
                print('여자')
            
            print("="*20)
            # 나이구하기
            yyyy = 2024
            # 주민등록 번호 앞2자리
            yy = ssn[0:2]
            if ssn[6] in ['1','2'] :
                # 주민번호 앞1자리가 1,2 이면 '19' + yy
                # 시작번호는 포함, 끝번호는 불포함
                # 시작값(0), 종료값(문자열의 길이에 따라 다름) 생략이 가능
                yy = '19' + yy
                #print(ssn[:2]) # 처음부터 2-1인덱스 까지
                #print(ssn[6:]) # 6 인덱스 부터 끝까지
                #print(ssn[:2]) # 0 인덱스 부터 2-1 인덱스 까지
            elif ssn[6] in ['3','4'] :
                # 주민번호 앞1자리가 3,4 이면 '20' + yy
                yy = '20' + yy
                
            # 나이구하기 (yyyy-int(19+yy))
            print('나이 : ' ,yyyy - int(yy))
        else :
            print('주민등록 형식에 일치 하지 않습니다.')
    else :
        print(f'13자리({ssn})로 입력 해주세요')
        # pass : 코드블럭이 없는경우 입력
else : print(f'숫자({ssn})만 입력 가능 합니다.')

# not 부정연산자
if not ssn.isnumeric :
    pass
    # exit()
    #return
    #continue
    #break

exit()



# 환경변수 설정 - 위치에 상관없이 파이썬을 실행 시킬수 있도록 환경변수를 설정
#   내컴퓨터 마우스 우클릭 설정 -> 고급시스템설정 -> 환경변수
#   path에 파이썬설치 경로를 추가
# 파이썬 설치시 환경변수 추가를 클릭하면 환경변수가 등록됨
# 환경변수가 등록되었는지 확인하는 방법
#   터미널에서 python명령어를 실행 
#   등록된 경우 python이 실행되고 명령어를 입력할 수 있는 프롬프트가 출력됨

# 두 수를 입력 받고 사칙연산의 결과를 출력 해봅시다
# 사용자의 입력을 대기 하다가 
# 사용자가 엔터를 누르면 입력된 값을 가지고 오는 함수
# 문자열을 반환 - 타입을 확인하는 함수 type()

num1 = input('숫자1을 입력 해주세요 : ')
num2 = input('숫자2을 입력 해주세요 : ')

print(num1)
print(type(num1))
# 문자열의 더하기 연산은 두 문자열을 연결 
# 숫자로 연산 하기 위해 형 변환이 필요
# int(문자열) : 문자를 숫자로 형변환
print(f'{num1} + {num2} = {int(num1) + int(num2)}')
print(f'{num1} * {num2} = {int(num1) * int(num2)}')
print(f'{num1} - {num2} = {int(num1) - int(num2)}')
print(f'{num1} / {num2} = {int(num1) / int(num2)}')
# 최대값, 최소값을 구하는 함수는 문자열도 처리가 가능!
print(f'최대값 : {max(num1, num2)}')
print(f'최소값 : {min(num1, num2)}')

# a + b = c
# 최대값 mix(a,b)
# 최소값 min(a,b)
print('두 수의 연산결과')

exit()


# 자판기에 물품을 초기화
items = ['오징어칩', '포키', '포테이토칩', '초코파이']
prices = [2100, 1300, 1800, 1200]

# 인덱스 값을 꺼내오기 위해서 enumerate함수를 이용
for index, item in enumerate(items) :
    print(f'{index} : {item}')


# 판매할 물건의 금액 
# 100원 단위로 입력 받아요
# 문자, 실수가 입력된 경우 오류
menu = int(input('구매하실 물품을 선택 해주세요'))

price = prices[menu]

print(f'선택하신 물품의 금액은 {price} 입니다.')

# 사용자로 부터 받은 금액
money = int(input('입금 : '))
# 거스름돈
change = money-price
# 문자타입 + 숫자타입 = 오류
print('거스름돈 : ' , change )
print(f'거스름돈 : {change}')
# 500원의 갯수
# 실수가 반환될수 있다
# 정수타입으로 반환
coin500_cnt=change//500

# 500원 거슬러주고 남은돈
change = change % 500

# 100원의 갯수
coin100_cnt=change//100

print(f'500원 : {coin500_cnt}개, 100원 : {coin100_cnt}개')
