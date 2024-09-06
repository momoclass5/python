# 리스트 
# 자료형의 집합을 표현할 수 있는 자료형
# [](대괄호)로 감싸고 요소값은 ,(쉼표)로 구분
list = [1,2,3,4,5]
# 모든 타입을 담을수 있다
list = [1, 'a문자열' , [1,2,3,4,5]] 
print(list)

# range : 숫자 리스트를 자동으로 만들어주는 함수
# range(끝값)
# range(시작값, 끝값)
# 💦 주의 끝값은 포함되지 않는다
# for 문과 함께 자주 사용되는 range() 함수
a = range(1,10)
print(a)
dan = 2
for i in a :
    #print('i : ' , i)
    print('%d * %d = %d' %(dan, i, dan *i))
    # 앞에 f 문자를 주고 변수는 {}안에 출력
    print(f'{dan}*{i}={dan*i}')
    
# 리스트를 출력시 인덱스를 사용하는 방법
items = ['포테이토칩', '계란과자', '땅콩스낵', '빼빼로']
prices = [2000, 3000, 4000, 5000]
for item in items :
    print(item)
    
for index, item in enumerate(items) : 
    print(f'{index} : {item}')