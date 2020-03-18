# 200318 13:01
# Chapter05-03
# 파이썬 심화
# 클로저 심화
# 클로저: 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능하도록 도와주는 거

# 클로저(Closure) 사용
def closure_ex1():
    # Free variable 자유 변수라고 합니다./함수 바깥에서 선언
    # 클로저 영역
    series = []
    def averager(v):
        # series = [] # 주석 해제 후 확인
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    return averager # 함수 결과 반환 가능


avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()

# function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()

"""
# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1 # cnt = cnt + 1
        total += v
        return total / cnt
    
    return averager

avg_closure2 = closure_ex2()

# print(avg_closure2(15)) # 예외
"""

# Nonlocal -> Free variable
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    
    def averager(v):
        nonlocal cnt, total # 프리변수가 된거에요
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()