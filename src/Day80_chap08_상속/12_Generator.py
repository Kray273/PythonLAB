# 12_Generator

def generator() :
    yield 0 # 값을 가지고 있다가 순차적으로 꺼내주는 키워드
    yield 1
    yield 2

iterator = generator()  # range와 유사하게 작동
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

###################################
def yourRange(start, end):
    current = start

    while current < end :
        yield current #현재 값을 가지고 대기!
        current += 1

if __name__ == "__main__" :
    print('=============================')
    for i in yourRange(0,3) :
        print(i)