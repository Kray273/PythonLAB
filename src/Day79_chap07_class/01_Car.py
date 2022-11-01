# 01_Car 일부러 첫 글자를 대문자로 작성(가독성을 위해서)

# VO의 필드(변수)는 DB의 column이다. 따라서 web 객체는 DB의 레코드를 의미한다.

# DB와 연결되어 관리할 목적으로 만들 것을 VO(JavaBean)이라고 한다.
class Car :
    # Java에서는 생성자(변수 초기화)를 클래스의 이름과 동일하게 만들었다.
    # 하지만 Python에서는 더 직관적으로 __init__()라는 함수로 선언한다.
    def __init__(self):
        # Java에서는 매개변수와 필드의 이름이 같으면 매개변수를 관찰하게 되므로 우리는 this를 지정해서 시작 주소값을 보관함.
        # 이와 같은 기능을 Python에서는 self로 지정한다. (this가 갑자기 나타나니 직관적으로 self라고 지정)
        self.color =  0xFF0000 # 차량의 색상
        self.wheel_size = 16 # 바퀴 사이즈
        self.displacement = 2000 # 배기량

    # 기능 또한 함수로 만들어 진다.
    def forward(self):             # 전진
        pass # 기능을 나중에!

    def backward(self):            # 후진
        pass

    def turn_left(self):           # 좌회전
        pass

    def turn_right(self):          # 우회전
        print("차가 도네요? 오른쪽으로?")


if __name__ == '__main__' :
    # 위의 코드는 자료형을 선언한 것이여서 의미는 없다. Java의 경우 new를 하면 해당 객체 만큼의 메모리가 할당되면 의미를 가진다.
    # 이와 다르게 Python에서 메모리 할당에 대한 요청을 함수를 호출 하듯이 한다.
    my_car = Car() # Car class의 객체를 생성
    # 객체를 호출하면 Python이 하는 4가지 행동.
    # 1. 앞에 참조변수를 찾아가 해당 객체만큼의 메모리를 할당한다.
    # 2. self를 찾아가 주소값을 저장한다.
    # 3. 생성자를 찾아가 데이터를 호출하면 필드 값을 초기화 한다.
    # 4. self(시작 주소값)를 반환한다.

    # Java의 경우 데이터에 접근하기 위해 참조변수.data명으로 접근하면 된다.
    # 이와 동일하게 Python도 '.'을 통해 접근 가능하다.
    print('0x{:02X} : '.format(my_car.color))
    # 핵사코드로 작성된 color를 정수의 값 2자리를 16진수로 출력하고, 2자리가 안되면 0을 출력하라는 의미
    print(my_car.wheel_size)
    print(my_car.displacement)

    my_car.forward() # my_car 맴버 매서드 접근
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()