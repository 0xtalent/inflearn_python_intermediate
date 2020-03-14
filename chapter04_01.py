# 200314 19:24
# Chapter04-01
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque]
# Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])

# 가변-언제든지 수정하능해: list, bytearray, array.array, memoryview, deque
# 불변-수정 못해요: tuple, str, bytes

# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '+_)(*&^%$#@!~)' # 플랫형이면서 불변형
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

# Comprehending Lists
code_list2 = [ord(s) for s in chars]

