# 05_multiInheritance
# 다중 상속

class A :
    def method(self):
        print("A")

class B(A) :
    def method(self):
        print("B")

class C(A) :
    def method(self):
        print("C")

class multi(B, C): # 두개 이상의 클래스를 상속
    # Java는 다중 상속을 지원하지 않음(C, C++은 지원)
    # Java에서 지원하지 않는 이유는 오히려 복잡성을 야기하고 그로인해 문제를 일으키기 때문이다.
    # Interfece에서 다중 상속의 개념을 충분히 커버 가능하다.

    # 다중상속은 최대한 쓰지 말자!

    pass

if __name__ == "__main__":
    obj = multi()

    obj.method() # 선행되어 있는 상속을 호출한다.
    # C++은 C를 호출할 것이다. 이러는 이유는 기준이 없어 개발자의 재량.이기 때문이다.#모호성 증가!