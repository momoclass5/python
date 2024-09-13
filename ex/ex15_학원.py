# 학원 
class Teacher : 
    # 생성자
    def __init__(self, name, subject) -> None:
        # 인스턴스 변수 생성 = 초기화
        self.name = name
        self.subject = subject
    
    def __str__(self) -> str:
        return f'teacher(name:{self.name}, subject : {self.subject})'

class Student : 
    def __init__(self, name, student_id) -> None:
        self.name = name
        self.student_id = student_id
        
    def __str__(self) -> str:
        return f'student(name:{self.name}, student_id : {self.student_id})'


class Academy :
    name = '휴먼컴퓨터 학원'
    def __init__(self) -> None:
        self.teacher = None
        self.students= []

    # 파라메터로 전달된 강사를 인스턴스변수에 설정
    def add_teacher(self, teacher) :
        self.teacher = teacher
    
    def add_student(self, student) :
        # 학생 리스트에 요소를 추가
        self.students.append(student)
    
    # 학생 목록을 받아와서 학생 목록에 추가
    def add_students(self, students) :
        self.students += students
    
    # 교사정보를 문자열로 반환    
    def get_teacher_info(self) : 
        return self.teacher.__str__()
    
    # 학생정보를 문자열로 반환
    def get_students_info(self) : 
        s_str = ''
        for s in self.students :
            s_str += s.__str__() + '\n'
        return s_str
    
    def __str__(self) -> str :
        
        # 클래스 내부의 인스턴스(멤버변수)를 호출 할때에도 self를 붙여 주어야 합니다!!!!!
        # 내부함수를 호출할때 self를 넣지 않아요!!
        s = self.name + '\n' + self.get_teacher_info() + '\n'+  self.get_students_info()
        #print('================',s)
        return s
     
    
        
# 다른모듈에서 실행할경우 실행되지 않음
if __name__ == '__main__' : 
    t = Teacher('오미선', '웹프로그래밍')   
    print(t)
    s1 = Student('김윤상', 1)
    s2 = Student('김건'  , 2)
    s3 = Student('김재헌', 3)
    s4 = Student('박근민', 4)
    s5 = Student('백지연', 5)
    s6 = Student('김태형', 6)
    s7 = Student('김주희', 7)
    students = [s1, s2, s3, s4, s5, s6, s7]
    #print(students)
    for s in students :
        print(s)
        
    academy = Academy()
    academy.add_teacher(t)
    academy.add_student(s1)
    academy.add_student(s2)
    academy.add_student(s3)
    academy.add_student(s4)
    academy.add_student(s5)
    academy.add_student(s6)
    academy.add_student(s7)
    print('-'*20)
    print(academy.get_teacher_info())
    print('-'*20)
    print(academy.get_students_info())
    print('-'*20)
    print(academy)
'''
Teacher: 오미선, Subject: 웹프로그래밍

Students
Student: 김윤상, ID: 1
Student: 김건  , ID: 2
Student: 김재헌, ID: 3
Student: 박근민, ID: 4
Student: 백지연, ID: 5
Student: 김태형, ID: 6
Student: 김주희, ID: 7

json
배열 : []
객체 : {}
{
    "키" : "값"
    , "강사":{"이름":"오미선", "과목":"웹프로그래밍"}
    , "학생":[
        {"이름":"김윤상", "id":"1"}
         ,{"이름":"김건", "id":"2"}
         ,{"이름":"김재헌", "id":"3"}
         ,{"이름":"백지연", "id":"4"}
         ,{"이름":"김태형", "id":"5"}
         ,{"이름":"박근민", "id":"6"}
    ]
}

{
    "list":[]
    , "pageNavi":{}
    , "totalCnt" : 20
}


'''