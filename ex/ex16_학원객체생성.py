import ex15_학원
# 파일의 모든 변수, 클래스, 메서드를 사용하겠다는 의미
# 이름.변수, 이름.클래스, 이름.메서드
a = ex15_학원.Academy()

from ex15_학원 import Academy, Teacher, Student as s;

# 강사
t = Teacher('오미선', '웹프로그래밍')   

# 학생
s1 = s('김윤상', 1)
s2 = s('김건'  , 2)
s3 = s('김재헌', 3)
s4 = s('박근민', 4)
s5 = s('백지연', 5)
s6 = s('김태형', 6)
s7 = s('김주희', 7)

# 학생 목록
students = [s1, s2, s3, s4, s5, s6, s7]

academy = Academy()
academy.add_teacher(t)
academy.add_students(students)
print(academy)
