# 10_decorator_@

# 사용자 정의 데코레이터.
# @Java에서는 어노테이션!

class MyDecorator :
    def __init__(self, f):
        print("Initializing MyDecorator....")
        self.func = f

    def __call__(self):
        print("Begin:{}".format(self.func.__name__))

        self.func()

        print("End:{}".format(self.func.__name__))

@MyDecorator # 원하는 클래스의 연결자료형을 매서드와 연결
def print_Hi():
    print("Hi_!")
    # 원하는 기능에 AOP기능과 비슷하게 적용할 수 있다. 즉 전후에 원하는 기능을 수행가능. 

if __name__ == '__main__':
    # Hi = MyDecorator(print_Hi) 데코레이션으로 불필요
    print_Hi()