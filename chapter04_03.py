# 200316 15:13
# Chapter04-03
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable): key에 value를 저장하는 구조입니다.
# -> 적은 리소스로 많은 데이터를 효율적으로 관리
# 파이썬 자체가 강력한 해시테이블 엔진으로 만들어져 있다.
# 파이썬에서 Dictionary가 해시테이블의 예라고 볼 수 있겠죠
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조입니다.
# 파이썬에서는 해쉬를 별도로 구현할 필요가 없어요. 딕셔너리를 그냥 사용하면 되기 때문에

# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인/해쉬 값을 확인할 수 있다는 것은 고유하다는 거죠
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50]) # 리스트는 해쉬값을 뽑아낼 수가 없어요. 리스트는 mutable

print( hash(t1))
# print(hash(t2)) # 예외

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# setdefault를 사용하지 않을 경우
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# setdefault를 사용할 경우
for k, v in source:
    new_dict2.setdefault(k, []).append(v) # 디폴트로 키값은 k를 사용할 거야, 나머지는 리스트로 담을거야

print(new_dict2)

# 주의: 이렇게 만들면 안되요/나중값으로 덮어 써버려요
new_dict3 = {k : v for k , v in source}

print(new_dict3)

print()
print()