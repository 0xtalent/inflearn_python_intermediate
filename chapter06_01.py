# 200318 15:58
# Chapter06-01
# 파이썬 심화
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text, List, Dict, Set, Tuple, unpacking, *args: iterable

# 반복 가능한 이유가 뭐에요? -> 내부적으로 iter(x)라는 함수가 호출이 되었다.
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for 반복
for c in t:
    print(c)

print()

# while 반복

w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

from collections import abc # 콜렉션즈에 있는거는 전부다 반복 가능하다고 했죠/abstractmethod

# 반복형을 확인할 수 있는 방법이 또 있어요/이게 정말 반복 가능한거야?
print(dir(t))
print(hasattr(t, '__iter__')) # True가 나오면 iterable한 거에요
print(isinstance(t, abc.Iterable)) # 상속을 받았는지 확인해볼 수 있어요
# 세가지 방법이 있네요

print()
print()

# next 사용
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tomorrow')

print(wi)
print(next(wi)) # 클래스지만 iterable해졌네요
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()

# 위에랑 똑같은 예제를 Generator 패턴으로 바꿔볼게요
# 1.지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2.단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3.작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        # print('Called __iter__')
        for word in self._text:
           yield word # 제네레이터
        return
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)

print(wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

print()
print()