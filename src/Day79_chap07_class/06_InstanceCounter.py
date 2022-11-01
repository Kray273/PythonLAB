# 06_InstanceCounter

class InstanceCounter :
    count = 0 # 클래스 변수 선언

    def __init__(self):
        InstanceCounter.count += 1 # 같은 필드안에 변수라도 클래스 변수이니 클래스명으로 접근

    @classmethod #정적메서드와 다른게 classmethod라는 데코를 사용
    def print_instance_count(cls): # 범용적 기능이다 보니. self가 아닌 cls라는 매개변수를 전달 받아야한다.
        #cls는 내 자신의 클래스 이름.
        print(cls.count)

if __name__ == '__main__' :
    x = InstanceCounter() # 전통적인 인스턴스 생성방식.
    x.print_instance_count() # 참조변수로 접근 가능

    InstanceCounter.print_instance_count() # 클래스 변수처럼 참조변수 없이 호출 가능.

    y = InstanceCounter() #클래스를 호출할 때, 값을 하나 증가시키도록 생성자에서 구현
    y.print_instance_count()                    # 2
    InstanceCounter.print_instance_count()      # 2

    InstanceCounter.count = 10 #클래스로 접근해 바로 값을 변경 가능.
    InstanceCounter.print_instance_count()  # 10

