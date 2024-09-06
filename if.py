# if문장
# 조건문
# 주어진 조건이 참인 경우에 실행
print('if')

# 조건에는 비교연산자
# >=, <=, ==
# 참 True / 거짓 False
if True :
    print('True')
    
# 자바와는 다르게 코드블럭대신 :과 탭(들여쓰기)이 이용 됩니다.
res = False
if res :
    print('참인 경우에만 실행 됩니다!')
# 부정연산자 not(! 대신 not을 사용)
elif not True : 
    print('조건이 여러개인 경우')
else :
    print('거짓인 경우에만 실행 됩니다!')
    

# 조건부표현식 (삼항연산자)
message = '참인경우' if True else '거짓인경우'
print(message)

# 반복문 
# while 조건문 :
#   코드작성
# 조건문이 참인 동안 코드를 반복해서 실행 

while True :
    print('무한반복')
    if True :
        # 조건문을 이용하여 반복문을 탈출 할 수 있다
        # 반복문을 탈출
        break # 반복문을 탈출하는 키워드

i=0
# 조건이 참이면 코드블럭을 반복해서 실행
while i<10 :
    i += 1
    print('i : %d' %i)


msg = """
도서관에 오신걸 환영합니다.

1. 도서대여
2. 도서반납
3. 도서등록
4. 도서삭제
5. 종료

"""

while True :
    print(msg)
    menu = input("메뉴를 선택 해주세요")
    if menu == '1' :
        print("도서대여")
    elif menu == '2' :
        print("도서반납")
    elif menu == '3' : 
        print("도서등록")
    elif menu == '4' : 
        print("도서삭제")
    elif menu == '5' : 
        print("프로그램 종료")
        #exit() # 프로그램을 종료하는 함수
        break # 반복문 탈출
    else :
        print(menu + "번은 없는 메뉴 입니다.")

index=0

while index < 100 :
    index += 1
    if index%2 != 0 :
        # 홀수인 경우 다음 반복문으로 넘어감
        continue # 남은 코드블럭을 실행하지 않고 다음 반복문으로 넘어감
    print(index)
    

        