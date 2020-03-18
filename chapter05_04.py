# 200318 14:06
# Chapter05-04
# 파이썬 심화
# 데코레이터

"""
데코레이터는 작성하는 코드의 긍정적인 영향을 엄청나게 증폭시킬 수 있습니다.
파이썬 데코레이터는 사용하기가 아주 쉽습니다. 
하지만 데코레이터를 작성하는 것은 완전히 다른 기술입니다.
다음과 같은 내용을 이해해야 합니다.

클로저
일급함수: 1)인자로 넘길 수 있고 2)함수를 함수의 결과값으로 받을 수 있고 3)변수로 할당할 수 있고, 런타임 시 초기화된다.
가변인자
인자 풀기(언패킹)
"""

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크..... -> 공통 기능 
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성 감소?(코딩하는 거에 따라 다름)
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
import time

def perf_clock(func):
    def perf_clocked(*args): # 패킹을 해서 받을거구요 아규먼트를 뭐 튜플로 넘어올 수도 있구요
        # 함수 시작 시간 
        st = time.perf_counter()
        result = func(*args) # 어렵다...ㅠㅠ
        # 함수 종료 시간 계산
        et = time.perf_counter() - st 
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수 
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result)) 
        return result 
    return perf_clocked # 전형적인 클로저의 패턴이네요~
    # 난이도가 있는 예제기 때문에 한번에 못따라해도 괜찮아요. 
    # 작동되는 것만 확인하고, 나중에 숙련도가 쌓이면 이해가 됩니다~

@perf_clock
def time_func(seconds):
    time.sleep(seconds) # 세컨드가 넘어오면 잠깐 슬립됩니다.

@perf_clock
def sum_func(*numbers): # 튜플로 받는건가?
    return sum(numbers)


# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars) # func가 들어간게 자유변수가 맞죠
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
print()
none_deco2(100, 150, 250, 300, 350)

print()
print()


# 데코레이터 사용
print('*' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('*' * 40, 'Called Decorator -> sum_func')
print()
sum_func(100, 150, 250, 300, 350)
print()