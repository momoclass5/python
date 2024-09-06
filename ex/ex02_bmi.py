# 사용자로 부터 키와 몸무계를 입력 받아 BMI를 구하는 프로그램을 작성
# BMI = 뭄무계/(키*키)
# 몸무계의 단위는 kg, 키의 단위는 m

# 사용자로 부터 키와 몸무게를 입력 받아 실수 타입으로 형변환 하여 변수에 저장
# input()의 반환타입은 문자타입이므로 형변환 해야 숫자의 연산 결과를 받을수 있다
while True : 
    msg = '''
BMI 계산기
    '''
    print(msg)
    height = float(input('키(m) : '))
    weight = float(input('몸무게(kg) : '))

    bmi = weight / (height*height)

    print('bmi는', bmi, '입니다')

    # BMI의 값에 따라 문자를 출력
    # 25이상 비만, 23이상 과체중, 18.5이상 정상, 나머지는 저체중
    if bmi >= 25 :
        print('비만')
    elif bmi >= 23 : 
        print('과체중')
    elif bmi >= 18.5 : 
        print('정상')
    else :
        print('저체중')
        
    next = ''
    
    # y또는 n을 입력 할때까지 계속 물어보기
    while next.lower() not in ['y', 'n']:          
        next = input('계속 하시겠습니까?(y/n)')
        
    print('next', next)
    #print('next lower', next.lower() != 'y')
    print('next ', next == 'y' or next == 'Y')
    
    # 소문자로 변환후 비교 
    if next.lower() != 'y' :
        print('lower', next.lower())
        break
    
    # or를 이용하는 방법
    # 조건1 or 조건2
    # 조건1 and 조건2
    if next == 'y' or next == 'Y' :
        print('y')
        continue # 다음반복으로 넘어감
    else :
        print('n')
        break   # 반복문을 탈출함
    
    # continue를 만나면 이후 블럭은 실행하지 않고 다음반복으로 넘어가므로
    # 아래 출력문장은 실행 되지 않는다
    print('=' * 30) 
    
   
    
