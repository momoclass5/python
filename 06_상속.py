class ParentClass : 
    def parent_method(self) : 
        return "부모클래스의 메서드"
    
# 자식클래스에서 부모를 지정
class ChildClass(ParentClass) : 
    def child_method(self) : 
        return "자식 클래스의 메서드"
    
    # 부모메서드를 재정의
    def parent_method(self) : 
        return "자식 클래스에서 재정의한 메서드"
    
cc = ChildClass()

print(cc.child_method())
print(cc.parent_method())