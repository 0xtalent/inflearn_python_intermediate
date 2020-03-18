# 200318 11:00
# Chapter05-02
# 파이썬 심화
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(10)


# Ex2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)


# Ex3

c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40
    
print('>>',c)
func_v3(10)
print('>>>',c)

from dis import dis

print()
print(dis(func_v3))

print()
print()


# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍이랑 연결 되겠죠?
# 클로저는 불변자료구조 및 atom(원자성), STM /이를 통해서 -> 멀티스레드(Coroutine) 프로그래밍에 강점
a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))

print()
print()

# 클래스 이용
class Averager(): 
    """평균을 누적해서 구해주는 클래스입니다."""
    def __init__(self): # 스페셜 메소드 써야죠 기본에 초기화 메소드 들어갑니다
        self._series = []

    def __call__(self, v):
        # 콜러블 메소드를 구현하고 있으면 클래스를 함수처럼 호출할 수 있다.
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager() # 생성자 초기화 파라미터 없습니다~

# 계속 누적되고 있습니다잉~
print(averager_cls(15))
print(averager_cls(35))
print(averager_cls(40))

print()
print()

# 클로저: 자유영역, 그 스코프에 있는 변수의 값 상태를 함수는 종료되었지만 기억하고 있다는거~