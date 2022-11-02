# 09_decorator_constructor

# 데코레이션 사용 용도 (생성자)

class MyDecorator :
    def __init__(self, f):
        print("Initializing MyDecorator....")
        self.func = f

    def __call__(self):
        print("Begin:{}".format(self.func.__name__)) #  값이 1개 이기에 {0}이 아니여도 사용가능

        self.func() # __call__() 매서드가 호출되면,
                    # 생성자에서 저장해두고 있었던 함수(데이터 속성)를 호출.

        print("End:{}".format(self.func.__name__))

def print_Hi():
    print("Hi_!")

if __name__ == '__main__':
    Hi = MyDecorator(print_Hi) #클래스 생성시 매개변수를 하나 전달하기로 정의되어 있음.
                               # func = print_Hi의 주소값이 저장.
        # MyDecorator 인스턴스가 만들어지며,
        # __init__(self, f) 매서드가 호출_(생성자 매서드)
        # ptint_Hi 식별자는 앞에서 정의한 함수가 아닌 MyDecorator의 객체.

    Hi() # 인스턴스가 __call__(self)을 함수를 호출하는 방식으로 호출

    # 참조자료형을 만나면
    # Initializing  MyDecorator....  1. 참조 자료형 안에 생성자가 있는지 확인한다.
    #                                2. 생성자에 매개변수를 저장한다.
    #                                3. __Call__()을 호출한다.
    # Begin: print_Hi                4. 호출된 매서드를 순차적으로 수행된다. __name__에 전달받은 매개변수를 저장.
    # Hi_!                           * 생성자에서 저장해두고 있었던 함수(데이터 속성)를 호출.
    # End: print_Hi