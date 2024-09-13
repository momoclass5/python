# 반복이 가능한 객체 vs 반복 객체
# 이터레이터(iterator) = 반복객체
# next() 함수 호출시 다음 요소를 반환 하는 객체

# 반복 가능(iterable) 객체 - 내부적으로 반복객체를 가지고 있다
# 반복문을 통해 반복처리가 가능한 객체
# 리스트, 튜플, 딕셔너리

# 반복 가능객체로 부터 반복객체를 반환 하는 함수
# 반복객체 = iter(반복가능객체)
# next(반복객체) : 반복객체로부터 다음 요소의 값을 반환
#                   요소가 더이상 존재 하지 않는경우 오류가 발생
list_a = [1,2,3]
list_iter = iter(list_a)
print(type(list_a))
print(type(list_iter)) # XXX_iterator 

next(list_iter)
next(list_iter)
next(list_iter)
# 더이상 꺼내올 요소가 없는경우 StopIteration오류가 발생
# 반복객체의 경우 next, for문을 이용해서 값을 꺼내오면 다시 꺼내올수 없다
#next(list_iter) # 오류
list_iter = iter(list_a)
for i in list_iter :
    print(i)
# 반복객체는 요소를 모두 꺼내고 나면 더이상 사용할수 없다
# 다시 값을 반복가능 객체로 부터 받아와야 함
#next(list_iter)

# 반복가능객체 만들기
#   __inter__   : iter() 실행  
#   __next__    : next(객체) 실행

class 반복가능객체:
    def __init__(self, data) -> None:
        self.data = data
        self.position = 0
    
    
    # 메서드를 구현하면 해당 클래스의 객체는 반복 가능 객체가 된다
    # 반복 가능 객체는 보통 클래스의 객체(인스턴스)를 반환 
    def __iter__(self) : 
        return self
    
    # 반복객체의 요소를 차례대로 반환
    def __next__(self) : 
        if self.position >= len(self.data) :
            raise StopIteration
        res = self.data[self.position]
        self.position += 1
        return res
    
반복가능객체1 = 반복가능객체([1,2,3])    
반복객체 = iter(반복가능객체1)
next(반복객체)
next(반복객체)
next(반복객체)
next(반복객체)