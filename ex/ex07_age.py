# 주민번호를 반복해서 입력 받으세요

# break문을 사용해서 반복문을 탈출 하게 만들어 준다
while True : 
    ssn = input('주민등록 번호 : ')
    
    # 데이터 전처리
    # 사용자의 입력값에 있는 공백과 - 는 제거
    ssn = ssn.strip() # 공백을 제거후 변수에 저장
    ssn = ssn.replace('-', '') # '-' 를 제거
    
    # 유효성검증 1. 13자리, 2. 숫자변환가능, 3. 7번째 자리가 1,2,3,4중 하나인지
    # 유효성검증 실패시 더이상 코드를 실행 하지 않고 (남아있는 코드는 무시)
    # 다음 반복문으로 넘어감
    if len(ssn) != 13 :
        # 오류코드와 메세지를 지정 하여 사용하기도 함
        print('주민등록 번호 입력 오류1[13자리 숫자]')
        continue
    
    if not ssn.isnumeric :
        print('주민등록 번호 입력 오류2[13자리 숫자]')
        continue
    
    if ssn[6] not in ['1', '2', '3', '4'] :
        print('주민등록번호 뒷 1자리는 1,2,3,4 이여야 합니다.')
    
    print('성별출력','='*20)
    if ssn[6] in ['1', '3'] :
        print('남자')
    if ssn[6] in ['2', '4'] :
        print('여자')        
    
    print('나이출력','='*20)
    yy = ssn[0:2] # 앞의 2자리를 변수에 저장 
    if ssn[6] in ['1', '2'] :
        # yy를 숫자로 형변환 하여 연산을 진행 하면 두수의 합이 되므로 문자로 연결 해줘야 한다
        yy= '19' + yy # 숫자와 문자의 연산은 오류가 발생 하므로 타입을 맞춰주어야 한다
    if ssn[6] in ['3', '4'] :
        yy= '20' + yy
    
    print('나이 : ', 2024 - int(yy))
    
    res = input('종료 하시겠습니까?(Y)')
    # 대문자로 변경후 비교
    if res.upper() == 'Y' :
        break # 반복문을 탈출해서 프로그램을 종료
        exit() # 프로그램 종료
    
    
    