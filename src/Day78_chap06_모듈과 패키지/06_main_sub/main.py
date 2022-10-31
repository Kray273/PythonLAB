# main
import sub

print("beginning of main.py....")
print('name : {0}'.format(__name__)) # __main__
print("end of main.py....")

# outputs
# beginning of sub.py....
# name : sub  _ 해당 위치에서 실행 시킨 것이 아니면 모듈의 이름을 보여줌.
# end of sub.py....
# beginning of main.py....
# name : __main__
# end of main.py....

