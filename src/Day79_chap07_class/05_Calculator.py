# 05_ Calculator

class Calculator :

    @staticmethod  # 데코레이션으로 수식(어노테이션과 비슷)
    def plus(x1, x2) : # 클래스 매서드로 self를 제외.
        # 클래스 매서드는 클래스 변수와 동일하게 공유 가능!
        # 정적 매서드 라는 용어를 사용
        return x1 + x2

    @staticmethod
    def minus(x1, x2):
        return x1 - x2

    @staticmethod
    def multiply(x1, x2):
        return x1 * x2

    @staticmethod
    def divide(x1, x2):
        return x1 / x2

if __name__ == '__main__' :
    print('{0} + {1} = {2}'.format(7, 4, Calculator.plus(7,4))) # 참조변수 없이 범용적으로 사용.
    print('{0} + {1} = {2}'.format(7, 4, Calculator.minus(7,4)))
    print('{0} + {1} = {2}'.format(7, 4, Calculator.multiply(7,4)))
    print('{0} + {1} = {2}'.format(7, 4, Calculator.divide(7,4)))