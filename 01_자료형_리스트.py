# 리스트를 만들고 1부터 10까지 입력 해보세요
a = []
for i in range(10) :
    #a.append(i) # 리스트에 맨 뒤에 항목을 추가
    #a.insert(0, i) # 리스트의 맨 앞에 항목을 추가
    a.insert(len(a), i)

# i = 0 ~ 9
for i in range(10) :
    # end='' : 줄바꿈없이 출력
    print(a[i], end='') # 리스트의 방번호에 입력된 값을 출력
        
# 5개의 음식을 입력받고 리스트에 추가 해보세요
# 리스트에 담겨있는 음식목록을 출력 해봅시다 - for

# 중복된 경우 입력되지 않도록 처리 - while-break
f_list = []
while True :
    f = input('좋아하는 과일?')
    
    # 중복된 값은 입력하지 않고 다음 반복으로 넘어감
    if f in f_list : 
        continue
        
    f_list.append(f)
    
    # len(문자열, 리스트, 튜플, 딕셔너리) = 요소의 갯수를 반환
    if len(f_list) == 5 :
        break

print(f_list) # 리스트를 출력 하면 리스트에 담긴 요소를 확인 할 수 있다
# 정렬 후 출력 
f_list.sort()
print(f_list)
# 오름차순 정렬 : sort(), 내림차순 정렬 : sort(reverse=True)
# 리스트에 오렌지가 없으면 3번 인덱스 오렌지를 리스트에 추가
if '오렌지' not in f_list : 
    # f_list.append('오렌지') # 맨마지막
    f_list.insert(3, '오렌지')
    
print(f_list)
