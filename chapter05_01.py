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

