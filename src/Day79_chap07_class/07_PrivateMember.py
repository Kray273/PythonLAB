# 07_PrivateMember

# 접근 제어지시자
    # 1. private : 해당 필드내에서만 접근 가능
    # 2. default : 같은 패키지 내에 존재하면 접근 가능(기본값)_Python에서는 제공하지 않음.
    # 3. protected : 상속의 조건하에서만 의미를 가짐_서로 다른 패키지에서도 상속 가능_Python에서는 제공하지 않음.
    # 4. public : 같은 프로젝트 내에서는 어떤 위치에서라도 접근을 허용.

class HasPrivate :
    def __init__(self):
        self.public1 = "public1" #기본 값은  public이다.
        self.__private1 = "private1" # 변수 이름 앞에 '__'로 private을 지정할 수 있음.
        self.__private2_ = "private2" # 변수 이름 앞에 '__', 이름 뒤에 '_'로 private을 지정할 수 있음.
        self.__public2__ = "public2" # 변수 이름 앞, 뒤에 '__"를 붙으면 public이다.

    def print_from_internal(self):
        print(self.public1)
        print(self.__private1)
        print(self.__private2_)
        print(self.__public2__)


if __name__ == '__main__' :
    obj = HasPrivate()
    obj.print_from_internal() # 같은 필드여서 모두 출력
                                # public1
                                # private1
                                # private2
                                # public2

    print("=======================")
    print(obj.public1) # 자료형 밖에서도 얼마든지 접근 가능
    #print(obj.__private1)  # error  AttributeError: 'HasPrivate' object has no attribute '__private1'  --private 속성이여서.
                            # 외부에서는 접근을 할 수가 없다.
    #print(obj.__private1_)  # error 동일한 문제
    print(obj.__public2__)