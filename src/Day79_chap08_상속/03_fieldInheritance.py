# 03_FieldInheritance

# 데이터 속성(field) 상속

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

