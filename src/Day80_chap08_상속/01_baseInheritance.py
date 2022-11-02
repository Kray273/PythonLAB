# 01_baseInheritance

# 상속의 문법적인 개념
    # 특정 참조자료형 간에 공통이 되어지는 속성이나 기능등이 존재한다고 한다면,
    # 특정 참조자료형 마다 속성이나 기능들을 반복하는것이 아니라.
    # 공통의 속석과 매서드를 뽑아 별도의 참조자료형(부모)을 선언하고
    # 나머 참조 자료형(자식)은 공통의 기능을 가진 참조 자료형을 부여 받음으로써
    # 코드의 중복을 줄이고, 관리의 효율성을 높인다.

class Base : #부모/상위 클래스
    def __init__(self):
        print(self)
        self.message = 'Hello, Kray.'

    def print_message(self):
        print(self.message)

# class Derived extends Base{} Java의 상속 방법

class Derived(Base) : # 자식/하위 클래스
    pass


if __name__ == '__main__' :
    base = Base() #부모클래스는 언제든 인스턴스 생성 가능 (주소값 : 0x0000021EF0D74408)
    base.print_message() #

    derived = Derived()
    # 동작원리
        # 0. 참조변수가 선언되면!
        # 1. 같은 이름의 참조 자료형(class)을 찾아간다.
        # 2. 같은 이름이 참조 자료형에 상속된(Base) 상위 클래스가 있다면 상위 클래스를 찾아간다.
        # 3. Heap메모리 영역에 상위클래스의 필드와 메서드 만큼의 메모리를 할당한다.
        # 4. 자식의 정의되어 있는 필드와 매서드 만큼 heap메모리 영역에 할당한다.
        # 5. heap에 할당된 메모리의 시작 주소 값을 리턴한다.
        # 6. stack 메모리에 메모리가 할당되고 시작 주소 값이 담긴다.(stack에 할당된 메모리가 heap을 바라본다.)
        # 7. stack 메모리에 시작 주소 값을 0.에 선언된 참조 변수에 리턴한다.

    derived.print_message() # 해당 클래스에 정의 되지 않은 매서드를 사용가능. (주소 값 : 0x000001EA94C74488)
    # 부모와 자식 클래스 주소값이 다르다. 그 이유는 위에 동작원리를 알면 된다.