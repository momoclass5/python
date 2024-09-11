f = open('새파일1.txt', 'r', encoding='utf-8')

line = f.readline()
print(line)

# 모든줄을 읽어 화면에 출력 하는 코드
while True :
    # readline() : 한줄씩 읽어옴
    # 더이상 읽을 줄이 없으면 빈 문자열을 반환
    line = f.readline()
    print(line)
    # 비어있으면 반복문을 탈출
    if not line : break

f.close()

# 파일을 닫고 새로 열어준다
f= open('새파일1.txt', 'r', encoding='utf-8')
# 파일의 모든줄을 읽어서 리스트로 반환
# 한줄 = 요소
lines = f.readlines()
#print(lines)
for line in lines :
    print(line, end='')

f.close()

# 파일을 닫고 새로 열어준다
f= open('새파일1.txt', 'r', encoding='utf-8')
# 파일의 전체 내용을 문자열로 반환
print(f.read())

f.close()

print('파일객체와 for문장을 함께 이용하기')
# 파일을 닫고 새로 열어준다
f= open('새파일1.txt', 'r', encoding='utf-8')
for line in f :
    print(line)
f.close()

# with 문은 파일을 열고 닫는것을 자동으로 처리 해줌
# with문을 벗어나는 순간 파일객체 f는 자동으로 닫힘
with open('새파일1.txt', 'w', encoding='utf-8') as f : 
    f.write('새로운 시작')