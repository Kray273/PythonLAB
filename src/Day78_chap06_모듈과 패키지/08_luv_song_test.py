# 08_luv_song_test
import luv__song.module01 as mod01
import luv__song.module02 as mod02


if __name__ == '__main__' :
    print(" ===  main === ")
    mod01.test() # 모듈안에서 패키지의 이름을 담고 있음.
    mod02.test() # 같은 이름의 함수여도 호출해서 사용시에는 문제가 없다.
