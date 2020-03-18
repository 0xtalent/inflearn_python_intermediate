# 200317 19:20
# Chapter05-01
# 파이썬 심화
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화: 실행시점에 초기화가 됩니다.
# 2.변수 할당 가능해야 합니다.
# 3.함수를 다른 함수의 인수로 전달 가능해야 합니다.
# 4.함수 결과 반환 가능해야 합니다(return)

# 함수 객체
def factorial(n):
    '''팩토리얼 함수에요 -> n : int 이것은 n 인트를 받아요'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1) # 재귀함수!!

class A:
    pass

print(factorial(6))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A)))) # 함수만 갖고 있는 속성(클래스 속성 제거)
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(10)) # 변수에 할당한 상태로 함수를 실행가능 합니다.
print(map(var_func, range(1,11)))
print(list(map(var_func, range(1,6))))


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce 등
print([var_func(i) for i in range(1,6) if i % 2]) # 지능형 리스트죠, 1 3 5만 나왔습니다. 0으로 나눠떨어지면 False가 되니까
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
# 가독성 면에서는 이게 좀 더 낫죠. 1부터 5까지의 숫자 중에서 홀수의 팩토리얼을 구하는데, 필터함수의 인자로 전달

print()
print()

# reduce()
from functools import reduce # 파이썬 버전이 업되면서 따로 빠졌거든요
from operator import add # 명시적으로 엄격하게 문법을 짤려고

print(reduce(add, range(1,11))) # 누적
print(sum(range(1,11)))


# 익명함수(lambda)
# 가급적 주석을 꼭 작성해라
# 가급적 익명함수보다는 함수를 사용해라
# 이름이 있는 일반 함수 형태로 리팩토링을 권장합니다
print(reduce(lambda x, t: x + t, range(1,11))) # 두개의 인자를 받아서, x + t를 반환합니다. 
# 두개씩 받아서 앞에거랑 뒤에거를 계속 누적시키면서, 출력을 해 준다는 것
print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))
# str('a') 호출 가능하잖아요. / 3.14는 상수잖아요 3.14() 이렇게 못하잖아요.
# from inspect import signature

# sg = signature(var_func)

# print(sg)
# print(sg.parameters)

# print()
# print()

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용합니다.
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5) # 함수가 인자로 들어가죠. 일급객체니까 5 * ?

# 고정 추가
six = partial(five, 6) # 함수를 변수에 할당했습니다.

print(five(10))
# print(six())
print([five(i) for i in range(1,11)]) # 마지막으로 리스트 컴프리헨션 해볼까요?
print(list(map(five, range(1,11))))