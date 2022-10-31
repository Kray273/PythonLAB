# main
import sub

if __name__ == '__main__' : #프로그램의 시작 포인트처럼 구석
    print("beginning of main.py....")
    print('name : {0}'.format(__name__)) # __main__
    print("end of main.py....")

# outPuts
# beginning of sub.py....
# name : sub
# end of sub.py....
# beginning of main.py....
# name : __main__
# end of main.py....