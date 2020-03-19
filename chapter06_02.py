# 200319 14:00
# Chapter06-02
# 파이썬 심화
# 병행성(Concurrency): 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러일을 쉽게 해결
# 병렬성(Parallelism): 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
# 파이썬에서 병행성도 지원하고, 병렬성도 지원합니다.

# Generator Ex1

def generator_ex1():
    print('Start')
    yield 'A Point.'
    print('continue')
    yield 'B Point.'
    print('End')

temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

print()

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

print()
print()

for i in temp3:
    print(i)

print()
print()


# Generator Ex3(중요 함수)
# filterfalse, takewhile, accumulate, chain, product, groupby...

# 무한대로 숫자를 만들어보고 싶다.
import itertools

gen1 = itertools.count(1, 2.5) # 시작과 증가단위

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

print()

# 조건/takewhile: 첫번째 매개변수로 함수를 받습니다.
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
# n은 n이 1000미만 일때까지 itertools.count(1, 2.5)

for v in gen2:
    print(v)
# 순회를 한번 해 볼께요

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)


print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

print()

# 연결1 chain: 서로 다른 iterable한게 있을 때 묶어서 하나로 뽑아내고 싶을 때
gen5 = itertools.chain('ABCDE', range(1,11,2))

print(list(gen5))

# 연결2

gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')

print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)

print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group)) # 이거 쫌 어렵네요

print()