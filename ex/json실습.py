import json

file = open('ex/json실습.json', 'r', encoding='utf-8')
# json 파일을 읽어 오브젝트로 반환
data = json.load(file)
print(data)
# 키의 이름으로 값을 꺼내옵니다
print(data['키'])
print(data['숫자'])
print(data['리스트'])
print(data['객체'])
print(data['객체']['이름'])

person = data['객체']
print(person['이름'])
print('='*20)
print(data['강사'])
print(data['강사']['이름'])
print(data['학생'][0]['이름'])


