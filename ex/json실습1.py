import json
#import ex15_학원
from ex15_학원 import Academy, Teacher, Student

# 파일열기
with open('ex/json실습.json', 'r', encoding='utf-8') as f :
    
    # json형식의 파일을 읽어 오브젝트로 변환 해서 반환
    obj = json.load(f)
    
    # 강사정보
    강사 = obj['강사']
    # print(f'이름 : {강사["이름"]}, 과목 : {강사["과목"]}')
    # 강사 객체
    t = Teacher(강사["이름"], 강사["과목"])
    print(t)
    
    # 학생정보 - 리스트
    studentList = obj["학생"]
    students = []
    #print(studentList) # 리스트는 반복문을 이용하여 요소를 하나씩 읽어와서 처리
    # 학생 객체 - 리스트를 돌면서 등록된 학생의 갯수만큼 생성
    for s in studentList :
        print(s["이름"])
        print(s["학번"])
        student = Student(s["이름"], s["학번"])
        students.append(student)
    
    a = Academy()
    a.add_teacher(t)
    a.add_students(students)
    print(a)
     
        


