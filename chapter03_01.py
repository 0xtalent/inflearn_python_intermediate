# 200313 13:17
# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 스페셜 메도스(매직 메소드): 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드


# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))
print()
print()

n = 10

# 사용
print(n + 100)
print(n.__add__(100))

# print(n.__doc__)
print(n.__bool__(), bool(n))

print(n * 100, n.__mul__(100))

print()
print()
