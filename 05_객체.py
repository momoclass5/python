# 클래스 정의
class MyClass : 
    pass # 아무작업도 수행하지 않는 빈 코드블럭

# 클래스의 인스턴스를 생성
myClass = MyClass()
myClass2 = MyClass()

# 인스턴스마다 각각 다른 정보를 저장 할 수 있다
print(myClass is myClass2)

class MyClass :
    # 생성자 : 객체가 생성될때 자동으로 호출 되며, 보통 초기화를 진행한다
    # 생성자의 이름은 __init__이고, 첫번째 매개변수로 self를 받아 옵니다
    #   self매개변수 : 생성된 객체를 참조(this)
    #                   인스턴스변수, 메서드에 접근 할 수있다
    def __init__(self) :
        print('MyClass 생성자 호출')
      
myClass = MyClass()

class MyClass :
    # 클래스 변수 : 인스턴스가 공유하는 변수
    var = '파이썬 클래스'
    
    #  -> None : 반환타입을 명시
    # None : 반환없음
    # 타입힌트는 필수는 아니지만 코드의 가독성을 높이고 오류를 발견하는데 도움을 줄수 있다
    def __init__(self, name) -> None:
        self.instance_var = '인스턴스 변수'
        self.name = name

    #클래스 자체를 수정 하거나 클래스에 관련된 정보를 반환
    # classmethod : 첫번째 매개변수의 값으로 클래스를 넣어줌
    # @ : 데코레이터
    @classmethod
    def set_class_var(cls, value) :
        cls.var = value
        
        
    # 생성하지 않고 사용가능
    @staticmethod
    def static_method() : 
        return "정적메서드"
        
    
print(MyClass.static_method())
# 생성자의 매개변수가 있다면 매개변수를 넣어서 호출     
# 인스턴스 변수는 생성자를 통해 초기화 되며 인스턴스마다 다른값을 가질수 있다!!!!!!
# myClass = MyClass() # ERROR : 생성자의 매개변수를 넣지 않아서 오류가 발생
myClass = MyClass('2교육장')
myClass1 = MyClass('1교육장')
print('인스턴스변수 : ', myClass.instance_var)
print('name : ', myClass.name)

print('인스턴스변수 : ', myClass1.instance_var)
print('name : ', myClass1.name)
# 각각의 인스턴스는 서로 다른 메모리에 저장되며 다른값을 가진다!!
myClass.instance_var='값을 변경'
print('myClass 인스턴스변수 : ', myClass.instance_var)
print('myClass1 인스턴스변수 : ', myClass1.instance_var)

# 인스턴스 변수를 생성
#myClass.var = 'test'
# 클래스 변수의 값을 변경 - 모든 인스턴스가 공유해서 사용
myClass.set_class_var('test')

# 클래스 변수
print(f'var : {myClass.var}')
print(f'var : {myClass1.var}')


# 객체 실습
class 사람 :
    pass
# 사람 클래스로부터 인스턴스를 생성 하여 human 변수에 바인딩
human = 사람()

class 사람 :
    # 매서드의 첫번째 매개변수로 self를 넣는다!!!!
    # 만약 self를 넣지 않으면 TypeError가 발생
    #   TypeError: 사람.cry() takes 0 positional arguments but 1 was given
    def cry(self, 소리) :
        #print('응애응애')
        #print(소리*2)
        for 변수 in 소리 :
            print(변수)
    
    def call(self, name, phone) :
        print(f'{name}에게 {phone} 발신중')

    def 구구단(self, num1, num2) :
        print(num1*num2)

    def 개인정보(self, name) : 
        # 입력받은 이름의 첫글자와 끝글자는 보여주고 나머지는 x문자로 대체
        center = 'x' * (len(name)-2)
        print(name[0] + center +  name[-1])
        
        
human = 사람()
human.cry('엉엉')
사람().cry('흑흑')

human.call('김철수', '010-2222-2222')
human.구구단(3,7)
human.개인정보('박서현')

# 생성자 연습
class 사람 :
    def __init__(self, name, year) -> None:
        # 인스턴스 변수
        self.name = name
        self.year = year
        print(f'{name}님 환영합니다.')
        pass

    # 객체 출력시 실행 되는 메서드
    def __str__(self) -> str:
        # 인스턴스 변수로 등록 되어 있어야 출력이 가능
        # 문자열을 반환 하는 메서드
        # 출력시 실행되는 메서드
        return f'이름 : {self.name}, 년도 : {self.year}'

사람1 = 사람('박서현', 2011)
print(사람1) # __str__ 함수 실행 결과가 반환 되어 져서 출력
print(f'{사람1.name}, {사람1.year}')

사람2 = 사람('박소현', 2010)
print(사람2)


class 사람 :
    # cnt : 성의 갯수
    def __init__(self, name, cnt=1) -> None:
        self.성 = name[0:cnt]
        self.이름 = name[cnt:]
    
사람1 = 사람('강호동님', 2)
# 인스턴스 변수는 변수명으로 접근한다!!!
print(사람1.성)
print(사람1.이름)

# 성이 2개인 사람도 있죠..

class 사람 :
    # cnt : 성의 갯수
    def __init__(self, 친구1, 친구2) -> None:
        self.친구1 = 친구1
        self.친구2 = 친구2
        self.친구 = [친구1, 친구2]
    

박서현 = 사람('강호동', '신동엽')
print('박서현.친구1 : ' + 박서현.친구1)
print('박서현.친구2 : ' + 박서현.친구2)
print(박서현.친구)

# 친구를 추가 할때마다 친구들목록에 친구가 추가 되어야 한다
class 사람 :
    
    def __init__(self) -> None:
        # 인스턴스변수 초기화
        self.친구들 = []
    
    def 친구추가(self, name) :
        self.친구들.append(name)
print('='*20)
박서현 = 사람()
박서현.친구추가('강호동')
박서현.친구추가('양효섭')
print(박서현.친구들)


class 사람 :
    def __init__(self, 이름, 친구들) -> None:
        self.이름 = 이름
        self.친구들 = 친구들
        
    def 친구추가(self, 친구) : 
        self.친구들.append(친구)

    def 친구목록(self) : 
        print(f'{self.이름} 친구목록')
        for 친구 in self.친구들 :
            print(f'- {친구}')
            
변수명 = 사람('유종훈', ['김철수', '김영희'])
print(변수명.이름)
print(변수명.친구들)
변수명.친구목록()