f = open('새파일.txt', 'w')
f.close()

# open(파일명, 모드)
# w : 쓰기모드
# a : 이어쓰기모드 
#f = open('새파일1.txt', 'w', encoding='utf-8')
f = open('새파일1.txt', 'a', encoding='utf-8')
f.write('안녕하세요\n') # 파일출력 = 파일객체가 닫혀진 이후에는 접근 안됨
f.write('반가워요\n')

for i in range(1,20) : 
    f.write(f"{i}번째 줄입니다.\n")

f.close()

# 읽기보드
#open('새파일2.txt', 'r') # 파일이 존재하지 않는경우 오류 발생