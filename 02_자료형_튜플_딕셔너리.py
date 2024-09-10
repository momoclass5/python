# 튜플 - 리스트와 유사하지만 요소값이 변경이 불가능 하다
# list = [] 요소값 생성/수정/삭제/삽입
# tuple = () 요소값 변경이 불가능, 요소값이 하나인 경우 ,를 붙여야함
t1 = ()
t2 = (1,) # 요소값이 하나인 경우 반드시 ,를 붙여야 함
t3 = 1,2,3 # 소괄호 생략 가능
t4 = (1,2,3, ('a','b')) # 소괄호 생략 가능

print(t1)
print(t2)
print(t3)
print(t4)

# 튜플을 값을 수정, 삭제시 오류가 발생
#del t1[0]
#t1[0] = 1

# 튜플에 접근
print(t2[0])    # 요소값을 튜플 타입으로 반환
print(t3[0:1])  # 슬라이싱된 요소를 튜플 타입으로 반환
print(t2+t3)    # 두 튜플을 연결하여 튜플 타입으로 반환
print(t3*3)     # 튜플의 요소를 3번 튜플 타입으로 반환

# 딕셔너리
# 키:값 형태로 저장되는 자료형
# { 키:값 , 키:값 ....}

dic = {'name':'박서현', 'age':14, 'phone':'010-1111-2222', 'birth':'20111129'}

dic['gender']='여' # 요소 추가
print(dic)
print(dic['name']) # 키를 이용해서 값을 반환
dic['gender']='남' # 중복불가 - 덮어쓰기됨

print(dic.keys()) # 키의 목록
print(dic.values()) # 값의 목록

# 딕셔너리의 키를 이용해서 값을 모두 출력 하는 방법
for k in dic.keys() : 
    print(k)
    print(dic[k])

# key, value 쌍 얻기 
# key, value를 튜플로 묶어 dict_items객체를 반환
print(dic.items())

# 없는 키값인 경우, get메서드를 이용하면 오류없이 사용 할 수 있다
print(dic.get('a'))

# 값이 없는경우 초기값 설정
# 키값이 존재하지 않는경우 None을 반환
# None : 변수에 값이 할당되지 않았을때
#       함수가 값을 반환 하지 않았을때
#       값이 없음/정의되지 않음을 나타내는 값
# print(dic.get('a'))   # 키값이 없는 경우 오류가 발생 
print(dic.get('a', '초기값'))

# bool()함수
# 자료형의 참/거짓을 식별하는 내장함수
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
# 1:true, 0:false
print(bool(0))

print(id(dic)) # id()메모리 주소를 반환
d = dic
# 메모리 주소가 같다는것은 같은 주소를 참조 하고 있다는 의미
print(dic is d) # A is B : A와 B의 메모리 주소가 같은지 확인

# 전개형문법
# 리스트에 들어있는 값을 변수에 저장
name, age = ['박서현', 15]
print(name)
print(age)