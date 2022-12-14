# 06_overriding

# 개념
    # 오버라이딩(overriding)이란 상속 관계에 있는 부모 클래스에서 이미 정의된 메소드를 자식 클래스에서
    # 같은 시그니쳐를 갖는 메소드로 다시 정의하는 것이라고 할 수 있습니다.
    # 자바에서 자식 클래스는 부모 클래스의 private 멤버를 제외한 모든 메소드를 상속받습니다.

# 오버라이딩 설명
    # 모든 인스턴스는 속성과 기능으로 정의할 수 있고.
    # 속성은 맴버변수(field)로 제공하고, 기능은 method로 제공한다.

    # 매서드 오버라이딩이랑 부모 클래스에서 기능과 속석을 정의해두면
    # 자식 클래스에서 동일한 이름으로 기능과 속성을 재정의 할 수 있는 것이다.
    # 예로 들어 에어컨의 신모델을 구매했는데, 고장이 났다고 가정하자.
    # 해당 모델의 부품은 단종 되어서 없는데 구 모델의 제품이 호환이 가능하면
    # 구 버전의 부품으로 교체해서 수리할 수 있다.
    # 이는 신모델을 개발할 때, 구모델을 가지고 신 모델을 만들었기 때문이다.
    # 즉 자바에서는 Aircon aircon = new Aircon() 을 Aircon aircon = new New_Aircon()으로만 바꿔주면
    # 다른 코드들을 수정할 필요가 없어짐으로 유지보수가 편하며, 업그레이드된 기능을 쉽게 사용 가능하다.

# 원래의 의도는 프로그램이 끝나는 시점에 적용을 하는 개념인데
# 자바에서는 '인터페이스'라는 기능을 통해 프로그램이 시작하면서 구현할 수 있도록 제공된다.


class A :
    def method(self): # 부모의 정의되어 있는 매서드.
        print("A")

class B(A) :
    def method(self): # 자식 클래스에서 기능을 재정의 해서 기능 업그레이드
        print("B")

class C(A) :
    def method(self): # 즉, 오버라이딩.
        print("C")

def overried(overiding) : #매서드를 정의하고 매개변수를 받는다. 즉 어떤 자료형이든 받는다.
    overiding.method() #매개변수를 통해

if __name__ == '__main__':
    a = A()
    #a.method() # A 출력

    b = B()
    #b.method() # B 출력

    c = C()
    #c.method() # C 출력

    # 상속을 하던, 바로 호출하던 동일함으로 오버라이딩의 이점이 없다.
    # 이점이 없는 문법을 제공하는 이유는 매서드를 통해 하나의 매서드를 통해 상속관계에 있는 다른 매서드들을 수행
    overried(a) # #a.method() 와 동일
    overried(b)
    overried(c)
    # 의미적인 부분은 제공하지만 이점이 크지 않다.

    overried("over") # error 전달은 되지만 전달 받은 매서드가 실행되는 과정에서 에러를 낸다. 자료형이 맞지 않아서
    # 이와 다르게 자바는 전달되는 순간에 자바는 에러를 낸다. 전달 받는 매개변수와 자료형이 맞지 않아서.

# 비슷해보이지만 다른 개념!
# 오버로딩(Overloading) : 같은 이름의 메서드 여러개를 가지면서 매개변수의 유형과 개수가 다르도록 하는 기술 (상속 아님!)
