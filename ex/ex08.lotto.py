# random 모듈을 이용하여 무작위수를 추출 해봅시다
import random

# 리스트의 항목을 무작위로 섞은후 원하는 갯수만큼 중복되지 않은 값을 추출
lotto = random.sample(range(1,47), 6)
print(lotto)

# 빈 리스트를 만들고 6개의 숫자를 담아 봅시다
# 무작위수를 추출 하여 중복을 제거 하고 담아 봅시다
lotto = []
while len(lotto) < 6 :
    num = random.randint(1,47)
    
    # 중복되지 않은 값만 저장
    if num not in lotto : 
        lotto.insert(0, num)

# 정렬
lotto.sort(reverse=True)
print(lotto) 
    
# 중복되지 않는 값을 저장
# set() 을 이용 하는 방법
lotto = set()

while len(lotto) < 6 :
    num = random.randint(1,47)
    lotto.add(num)

# sorted() 함수를 이용해서 정렬
#   요소를 정렬후 리스트로 반환
lotto_list = sorted(lotto)
print(lotto)
print(lotto_list)
# 역순 정렬
lotto_list = sorted(lotto, reverse=True)
print(lotto_list)
