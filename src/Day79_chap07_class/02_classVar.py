# 02_classVar

class ClassVar :
    text_list = []  # 클래스 변수!
    #변수를 선언하고, 리스트의 자료형으로 초기화만 시켜준 상태. 리스트형 자료형 선언
    # python은 생성자 안에 필드를 선언하는데, 여기서는 밖에서 선언했다.
    # 여기서 선언된 변수는 자바의 static(클래스 변수)과 동일한 뜻이다.(클래스 변수, 클래스 매서드 둘다 있다!
    # 클래스 변수란 글로벌 변수처럼 사용하려고(공유) class내에 선언하는 변수.
    # 일반적으로 PI값처럼 수학에서 고정으로 사용하는 값과 같은 고정된 값들을 클래스 변수로 설정
    # 특징은 참조자료형 선언시에 static이 붙어 있으면, 사용시에 new를 사용하지 않아도 된다.
    # new를 사용하지 않아도 되는 이유는 Math math = math()라고 선언시에 Math를 만나는 순간
    # Math라는 클래스를 찾고, 그 안으로 들어가 static을 찾으면 new를 자동으로 한다(매서드 영역에 할당!).

    # Java는 3가지의 메모리 영역을 가지는데
    # 1. mathod 메모리 영역은 프로그램이 시작되고 종료되기 전까지 유지하는 영역_함수를 뜻하는 것이 아니라 이름만!
        # 그래서 누구든지 static변수를 사용할 수 있는 것이다.
    # 2. stack 메모리 영역은 매개 변수나 지역변수 처럼 호출되는 순간에 할당하고 실행이 종료되면 삭제되는 영역
        #  (ex. if문이 끝나면 안에 사용된 변수 사용 불가. 타 클래스에 사용된 지역변수는 사용이 되고 삭제됨. )
   # 3. heap 메모리 영역은 new했을 때 할당되는 영역으로, 언제 소멸 되는지 모른다(Java가 소멸시키는 정확한 시점을 모른다).

    def add(self, text) : #문자열을 추가하는 매서드
        self.text_list.append(text)

    def print_list (self) : # 문자열을 출력하는 매서드
        print(self.text_list)

if __name__ == '__main__' :
    ClassVar.text_list.append('a') # 'a'라는 문자열을 삽입
    print(ClassVar.text_list)

    x = ClassVar()   # 참조변수에 클래스를 할당
    x.add('b')     # 'b'를 추가
    x.print_list() # 추가된 문자열을 출력

    print(ClassVar.text_list)

    y = ClassVar()
    y.add('c')
    y.print_list()

    print(ClassVar.text_list)