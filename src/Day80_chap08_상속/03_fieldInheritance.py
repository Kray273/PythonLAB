# 03_FieldInheritance

# 데이터 속성(field) 상속

'''
class A :
    def __init__(self):
        print("A.__init()__()") #생성자가 생성된 것을 확인하기 위해서 출력
        self.message = "Hi" # field(맴버변수)지정, 접근제어지시자 public

class B(A) :
    def __init__(self):
        print("B.__init()__()")

if __name__ == '__main__' :
    obj = B() # B를 통해 인스턴스 생성 요청 후 참조변수에 담음. B의 B.__init()__()는 출력이 됨.

    print(obj.message) # error를 발생 시킴. AttributeError: 'B' object has no attribute 'message'
    # message에 접근을 못해서 생긴 오류가 아닌.
    # 상속의 조건하에서 자식의 생성자에서 반드시 부모의 정의되어 있는 필드를 초기화할 의무를 가진다.
    #  따라서, A class의 생성자에서 print를 통해 초기화 하고 있다. 그래서 에러를 낸다.
    # 생성자는 필드(맴버변수)를 초기화할 목적이다.
'''


class A :
    def __init__(self):
        print("A.__init()__()")
        self.message = "Hi"

class B(A) :
    def __init__(self):
        A.__init__(self) #부모의 정의되어 있는 필드를 초기화할 목적으로 작성 필요! 명시적으로 표현
        # 자바와 다르게 내가 생성자를 호출해도 에러를 내지 않는다.
        print("B.__init()__()")

if __name__ == '__main__' :
    obj = B()

    print(obj.message)