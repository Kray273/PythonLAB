# 11_iterator

# iterator 와 순회 가능한 객체

for i in range(3) : # 0,1,2 까지 반복.
    print(i)

print("===============================")

iterator = range(3).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) # error 반복수 이상을 반복!

class MyRange : # range() 함수와 동일한 클래스를 정의
    def __init__(self, start, end): # range(5) = range(0,5)
        self.start = start
        self.end = end

    def __iter__(self): #참조자료형을 정의시에 __iter__()를 한번 호출한다. (누가? for문이!)
        print('iter') # 호출시 확인용
        return self  # 받아온 값을 리턴

    def __next__(self):
        print('next')
        if self.start < self.end :
            current = self.start # current에 시작 값을 넣고
            self.start += 1 # 시작값을 하나 증가 시킴
            return current # 증가되지 않은 값을 리턴
        else:
            raise StopIteration() #Java의 throw

if __name__ == '__main__' :
    print("===============================")
    for i in MyRange(0,3) : # range(0,3) / range(0,10,2) 3번째는 2씩 증가라는 뜻!
        print(i)
