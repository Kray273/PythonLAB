# 01_ Exception

def my_power(y):
    x = int(input("숫자를 입력하세요 : "))  # R은 scan(), Java는 scanner(), Python과 JS는 input()
    return x ** y


if __name__ == '__main__' :
    print(my_power(2)) # 입력받은 값을 자승하겠다 .

    # 문자를 입력하면 error를 낸다. 이런 경우를 예외를 발생했다고 한다.

    # 예외가 발생되면 프로그램을 자동으로 종료시키지 말고 프로그래머가 정의한 방식으로 작동되게 하는 것이 예외처리이다.