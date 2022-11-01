# 03 instanceVar

class InstanceVar :
    def __init__(self):
        self.text_list = []  # 멤버변수(field)

    def add(self, text):  # 맴버 매서드
         self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == '__main__' :
    # InstanceVar.text_list.append('a')  error 클래스 변수는 바로 접근하는 것을 허용하지 않는다.

    x = InstanceVar() # 인스턴스 변수는 참조 변수로만 접근이 가능하다.
    x.add('a')
    x.print_list()         # ['a']
    print(x.text_list)     # ['a']

    y = InstanceVar()      # 클래스 변수와 다르게 개별적인 값이 출력된다.
    y.add('b')
    y.print_list()         # ['b']
    print(y.text_list)     # ['b']