# 02_Polymorphism

# 다형성(polymorphism)이란 하나의 객체가 여러 가지 타입을 가질 수 있는 것을 의미한다.
# Java에서는 이러한 다형성을 부모 클래스 타입의 참조 변수로 자식 클래스 타입의 인스턴스를 참조할 수 있도록 하여 구현하고 있다.

# 다형성이란! "상속의 조건하"에서 중요! 상속의 조건하에서!!!
# 자식 클래스의 인스턴스를 생성할 때, 자신의 자료형 뿐만이 아니라 부모의 자료형으로도 바라볼 수 있는 것!
# 즉 Computer nb = new NoteBook()이 가능하다.
# 위가 가능한 이유는 computer의 기능에 더해지는 notebook의 +a 기능을 생각하지 않기 때문이다.
# 그래서 !(NoteBook cm = new Computer()) 이다!
# 자식이 부모를 바라볼 수는 없다!  노트북은 이미 컴퓨터로 부터 추가된 +a기능이 고려 되어 있다.

class ArmorSuit :
    def armor(self):
        print('armored')

class IronMan(ArmorSuit) :
    pass

def get_armored(suit):
    suit.armor()

if __name__ == '__main__':
    suit = ArmorSuit()
    get_armored(suit) # 호출 가능.

    Tony = IronMan()
    # 문법적인 구조로 인해 다형성을 적용할 수가 없다.
    # 그래서 객체지향의 꽃인 다형성을 적용하기 위해 다시 컴파일 언어로 회귀하는 경우가 많다.
    get_armored(Tony) # 상속의 관계임으로 작동은 되지만 Tony가 어떤 자료형인지 판단하는 것은 어렵다.
                      # 이와 반대로 Java는 명확하게 구별해서 이를 통해 매서드 오버 라이딩을 사용할 수 있다.

    suit = suit()
    get_armored(suit) # error TypeError: 'ArmorSuit' object is not callable
    # suit()안에는 ArmorSuit의 기능이 작성되어 있지 않기 때문에 error를 일으킨다.