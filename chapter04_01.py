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

# 200316 12:52

# Comprehending Lists + Map, Filter
# 속도 약간 우세
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
# 필터함수는 두개의 인자를 받죠. 첫번째는 임명함수?!나 함수를 받고 두번째는 어떤 리스트나 자료구조 형태를 받죠
# x 하나를 받아서 40보다 큰지를 트루 폴스로 리턴해주고/map함수

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()


# Generator 생성 
import array

# Generator: 한 번에 한 개의 항목을 생성(메모리 유지X)/하나의 파워풀한 이터레이터
tuple_g = (ord(s) for s in chars)

# Array: 한개의 자료형만 저장할 수 있고, 가변형입니다.
array_g = array.array('I',  (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist()) # 어레이를 바로 리스트로 반환하는 함수 tolist()

print()
print()

# 제네레이터 예제
# 제너레이터니까 소괄호로 묶어주고
# %s 문자열이다 알려주고

print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

# 한번에 만들고 출력한 것이 아니라 하나하나 계속 하나 출력하고 하나 생성하고...
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)


print()
print()

# 리스트 주의
# 깊은 복사와 얇은 복사
marks1 = [['~'] * 3 for _ in range(4)] # 4개를 만들고 3개를 곱할게요
marks2 = [['~'] * 3] * 4 # 정말 critical한 문제가 있습니다

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'# 모든 리스트들의 1번째 인덱스가 다 바뀝니다

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1]) # 서로 4개가 다름
print([id(i) for i in marks2]) # 하나 갖다가 복사가 이루어졌음