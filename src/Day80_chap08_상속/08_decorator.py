# 08_decorator

#데코레이터

class Callable :
    def __init__(self): #생성자
        pass

    def __call__(self): # 자동완성 후 기본 매개변수 제거.
        # def __call__(self, *args, **kwargs):
        print("I am called.")

if __name__ == '__main__' :
    obj = Callable() #클래스를 호출하기 위해서는 객체를 호출하고 참조변수에 담아둔다.
    # 범용적으로 참조변수가 객채의 주소 값을 가지고 있음으로 객체라고도 말함.

    obj() #객체를 함수를 호출 방식으로 사용
    # 인스턴스 뒤에 괄호()를 붙여 호출하면(함수호출 방식),
    # 내부적으로 __call__(self) 매서드가 호출된다.
