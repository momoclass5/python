# 계산기 클래스를 정의
# 생성자 의해 두개의 인스턴스 변수 num1, num2를 생성
# 더하기 메서드
# 빼기 메서드
# 곱하기 메서드
# 나누기 메서드
class 계산기 :
    # 두수를 입력 받아 객체를 초기화
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def 더하기(self) :
        return self.num2 + self.num1
    
    def 빼기(self) :
        return self.num2 - self.num1
    
    def 곱하기(self) :
        return self.num2 * self.num1
    
    def 나누기(self) :
        return self.num2 / self.num1

print('모듈이 직접 실행 되었는지 확인하는 변수')
print('__name__ : ', __name__)
# 모듈이 직접 실행 되었는지 다른 모듈에 의해서 실행 되었는지
# 구분하는데 사용되는 특별한 변수 
# 모듈이 직접 실행 되었다면 __name__은  __main__으로 지정
if __name__ == '__main__' :

    try :
        calc = 계산기()
    except TypeError as te:
        print(te)
        calc = 계산기(0,0)

    # 인스턴스의 변수이름으로 접근하여 메서드, 변수를 사용 할 수 있다
    print('인스턴스변수 calc.num1 : ', calc.num1 )
    print('메서드 calc.더하기() : ', calc.더하기() )


    try :
        num = 10/0
    except ZeroDivisionError :
        print('0으로 나눌수 없습니다')

    try :
        num = 10/2
        # input의 반환타입은 문자 이므로 숫자로 변환 하는 처리
        num = int(input('숫자를 입력 해주세요'))
    except ZeroDivisionError as err:
        print(f'err : {err}')
    except ValueError as ve :
        print(f'err : {ve}')   
    except :
        print('error')
    else : 
        print('정상적으로 실행 되었을때만 실행')

# 사용자 정의 예외만들기
# Exception 클래스를 상속 하여 사용자 정의 예외클래스를 정의 할 수 있다
class MyError(Exception) : 
    def __str__(self) -> str:
        return '에러 메세지'
    pass

def say_nick(nick) : 
    if nick == '에러' :
        # 에러를 발생 시키는 코드
        # raise :  오류를 강제로 발생 시키는 코드
        raise MyError()


    print(f'nick : {nick}') 

say_nick('실행')
try : 
    say_nick('에러')
except MyError as me:
    print(f'say_nick 에러 : {me}')


# 계산기를 상속받아서 공학용계산기를 정의
class 공학용계산기(계산기) :
    def __init__(self, num1, num2, num3) -> None:
        # 부모 생성자를 호출 하여 인스턴스 변수를 세팅
        super().__init__(num1, num2)
        self.num3 = num3
        
    def add(self) : 
        return '공학용 계산기 더하기'


a = 공학용계산기(1,2,3)
print(a.add())

print('프로그램 종료')


