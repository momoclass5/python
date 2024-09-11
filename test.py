# 리스트 생성
a = [1,2,3]
# 주소값이 들어감
b = a
a.append(4)
# a,b는 같은 주소를 바라보고 있으므로 
# 리스트가 변경되면 같이 변경
print('a : ', a)
print('b : ', b)

a = '안녕'
b = a
a = '변경'
print(a)
print(b)


print("=" * 20)


# 전역변수
var1 = '함수밖 변수'
var2 = '함수밖 변수'


# 변수명 = 값
def verTest(var1=var1) :
    # 전역변수를 함수에서 사용
    global var2
    print(var1)
    # 그냥 외부에있는 변수에 접근하는것은 가능함
    # 하지만 외부에 있는 변수를 접근후 값 변경은 불가능함.
    # 지역변수로 정의
    var2 = '함수안에서 변경'
    var1 = '함수안에서 변경'
    print(var2)
    print(var1)
    
verTest() 
print(var1)
print(var2)

