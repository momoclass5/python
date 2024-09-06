# 1~100까지 수의 합 출력
index = 1
sum=0
while index <= 100 :
    #print(index)
    index += 1
    sum += index # sum = sum + index

print("sum : %d"%sum)
print("=" * 50)

# 1~100까지 수중 홀수의 합만 출력
index = 0
sum = 0
while index < 100 :
    index += 1
    # 짝수이면 다음 반복문으로 넘어감
    if index % 2 == 0 :
        continue
    sum += index

print('sum : %d'%sum)
     