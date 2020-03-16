# 200316 17:10
# Chapter04-04
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict 수정이 불가능한 딕셔너리 만들기/읽기 전용의 딕셔너리
from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key1'] = 'value2'

d['key2'] = 'value2'

print(d)

print()
print()

# Set
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi']) # 안에 리스트를 넣어서 선언
s3 = {3} # 단일원소 일때
s4 = set() # Not {} / 원소가 하나도 없을 때는 딕셔너리로 인식
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 파이썬은 실행될 때 바이트 코드를 실행합니다.
# 파이썬 인터프리터가 바이트 코드를 실행하는 겁니다.
# dis를 사용하면 바이트 코드가 어떻게 생성되는지 순서를 볼 수 있어요
from dis import dis

print('------')
print(dis('{10}'))

print('------')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

print('------')

print({name(chr(i), '') for i in range(0,256)})