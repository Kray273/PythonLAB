# 04_super

class A :
    def __init__(self):
        print('A.__inif__()')
        self.message = 'SUPER!!'

class B(A) :
    def __init__(self):
        # A.__init__(self) # 부모의 생성자를 초기화하는 명시적 표현
        # Java에서는 생성자는 자바만 호출 가능, 따라서 다음과 같이 기능이 제공됨
        super().__init__() # Java와 동일한 컨셉으로 제공이 되니 이 방법을 권고함.
        print('B.__inif__()')

        print("self.message is "+ self.message) # 부모의 인스턴스를 자식이 출력하는 것은 상속의 개념에서 너무 당연하다.


if __name__ == '__main__' :
    obj = B()

    print(obj.message)
    # 0. 자식을 통해 부모의 생성자가 호출되면!
    # A.__inif__()  1. 부모의 생성자를 호출
    # B.__inif__()  2. 자식의 생성자를 호출
    # self.message is SUPER!! 2-2. 자식의 생성자 안에서 부모의 인스턴스 출력
    # SUPER!! 3. 부모의 생성자 호출!

#######################################

class Base :
    def __init__(self):
        print("Base") #호출 확인용 메세지지

class Derived(Base) : # 상속의 관계에서는 자식의 생성자에서 부모의 생성자의 초기화 해줘야 하는데 내부에서 알아서 해준다.
    pass  # 이름만 가진 클래스 정의
    # 내부에서 이루어 지는 행위
        # def __init__(self):
        #   super().__init__()

print('============================') # 구별을 위한 라인

d = Derived() # 참조변수 선언.