f = open('ex/2. 게티즈버그.txt', 'r', encoding='utf-8')
#print(f.read())

dic = {}
while True : 
    line = f.readline()
    if not line : 
        break
    line = line.replace('\n', '').replace('.', '').replace(',', '')
    word_list = line.split(' ')
    
    for word in word_list : 
        if word in dic : 
            # 카운팅 = 기존의 값 + 1
            dic[word] += 1
        else :
            # 추가
            dic[word] = 1

# 딕셔너리를 값으로 내림차순 정렬
dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)
print(dic)
print(f'총 단어수 : {len(dic)}')
for i in range(0,5) :
    print(dic[i])
    #print(f'{dic[i][0]}, {dic[i][1]}')
    
'''
# ,(콤마), ., \n(줄바꿈) 문자 제거
# 모두 대문자로 변경

# 딕셔너리에 데이터 추가
dic['키'] = 1
# 키는 중복될수 없으므로 값이 수정됨
dic['키'] += 1
print(dic)
if '핸드폰' in dic : 
    print('====')
    # 키값이 존재하면 값을 증가(카운팅)
    dic['핸드폰'] += 1
else :
    # 키값을 딕셔너리에 등록
    dic['핸드폰'] = 1
    
print(dic)
print(len(dic))
'''