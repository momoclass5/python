# 자판기에 물품을 초기화
items = ['오징어칩', '포키', '포테이토칩', '초코파이']
prices = [2100, 1300, 1800, 1200]

# 인덱스 값을 꺼내오기 위해서 enumerate함수를 이용
for index, item in enumerate(items) :
    print(f'{index} : {item}')


# 판매할 물건의 금액 
# 100원 단위로 입력 받아요
# 문자, 실수가 입력된 경우 오류
menu = int(input('구매하실 물품을 선택 해주세요'))

price = prices[menu]

print(f'선택하신 물품의 금액은 {price} 입니다.')

# 사용자로 부터 받은 금액
money = int(input('입금 : '))
# 거스름돈
change = money-price
# 문자타입 + 숫자타입 = 오류
print('거스름돈 : ' , change )
print(f'거스름돈 : {change}')
# 500원의 갯수
# / 실수가 반환될수 있다
# // 정수타입으로 반환
coin500_cnt=change//500

# 500원 거슬러주고 남은돈
change = change % 500

# 100원의 갯수
coin100_cnt=change//100

print(f'500원 : {coin500_cnt}개, 100원 : {coin100_cnt}개')
