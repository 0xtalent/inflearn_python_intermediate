# 200316 13:53
# Chapter04-02
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9)) # 몫과 나머지를 반환해주는 함수죠
print(divmod(*(100, 9))) # 튜플로 넣을 거다 하면 아스타를 붙여줘서
print(*(divmod(100, 9))) # 결과값을 풀어버린거(패킹)

print()

x, y, *rest = range(10) # 나머지 것들이 패킹됨
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25) # 튜플은 불변형이죠 Immutable
m = [15, 20, 25] # 리스트는 가변형이죠 Mutable

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(id(l))
print(id(m))

l *= 2
m *= 2

print(id(l)) # 내부적으로 재할당이 되었음
print(id(m)) # 이때 리스트는 ID값이 가변형이기 때문에 자기 아이덴티티 값에 할당함

print()
print()

# sort vs sorted 
# reverse, key=len(키에 길이 옵션이 있습니다), key=str.lower(소문자 순서로 정렬을 하겠다), key=func..

# sorted : 정렬 후 새로운 객체 반환/원본은 수정 안됩니다
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True)) # 역순으로
print('sorted -', sorted(f_list, key=len)) # 길이순으로
print('sorted -', sorted(f_list, key=lambda x: x[-1])) # 키에는 내가 만든 함수도 사용할 수 있어요/끝에 글자를 기준으로
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True)) # 이거 쓰는 방법 이해 안가요
print()

print('sorted -', f_list)

print()

# sort : 정렬 후 객체 직접 변경/원본이 수정됩니다

# 반환 값 확인(None)/반환값이 없어요
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성(컨테이너, 다양한 형태를 담을 수 있어요), 다양한 자료형, 범용적 사용
# 숫자 기반일때는 array를 사용하는 것이 좋아요 : 배열(리스트와 거의 호환)