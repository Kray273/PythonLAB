# 07_overriding2

class Car :
    def ride(self):
        print("Run")

class FlyingCar(Car) :
    def ride(self) : # 오버라이딩을 통해 매서드 설정
        super().ride() #함수의 형태로 부모의 매서드 호출. 상속의 조건하에서 부모의 생성자를 호출할 때와 동일.
        print("Fly")

def who(whatever) :
    whatever.ride()

if __name__ == '__main__':
    car = Car()
    car.ride() #Run
    #외부에서 호출 X, 정의된 매서드 안에서만 호출 가능!
    my_car = FlyingCar()
    my_car.ride() # Run Fly 둘다 뜸.

