# 함수 정의
# 단을 입력 받아서 값을 출력 하는 함수
def gugu(dan) : 
    res = []

    res.append(f'{dan}단')
    print(f'{dan}단', end=' ')
    # 2*1 ~ 2*9
    # 범위를 통해서 반복문을 실행
    for i in range(1,10) : 
       res.append(dan * i)
       # 출력시 줄바꿈 하지 않음
       # end = ' ' 출력후 공백입력
       print(dan*i, end=' ')
    
    print()
    return res

# 함수 호출
res = gugu(2)
print(res)

# end값 미만의 수를 출력
# 범위를 입력 받아서 3의배수, 5의배수의 합계를 반환 하는 함수
def test(end) :
    #print(list(range(1,end)))
    res = 0
    for i in range(1,end) :
        # 3배수이거나 5의 배수이면 출력
        if i % 3 == 0 or i % 5 == 0 :
            #print(i)
            res += i
    
    return res

res = test(10)
print(res)

# 게시판 페이징
# 게시물의 총 갯수와 한페이지에 보여줄 게시물의 수를 입력 받아서 
# 총 페이지수를 반환 하는 함수
def get_total_page(total_cnt, amount) : 
    # total_cnt : 게시물의 총건수
    # amount :  한페이지에 보여질 게시물의 수 
    # // : 정수를 반환
    # 나머지가 있다는건 더 보여줄 게시물이 있다는 의미
    # 나머지가 없다는건 다음 페이지가 없다는거랑 같음
    if total_cnt % amount == 0 : 
        return total_cnt//amount
    else :
        return total_cnt//amount + 1
    
import math
def get_total_page1(total_cnt, amount) : 
    return math.ceil(total_cnt/amount)

print("="*20)    
print(get_total_page1(5, 10)) # 총 페이지수 : 1
print(get_total_page1(15, 10)) # 총 페이지수 : 2
print(get_total_page1(25, 10)) # 총 페이지수 : 3
print(get_total_page1(30, 10)) # 총 페이지수 : 3


