# 200313 15:58
# Chapter03-03
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt # 루트

l_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print(l_leng1)


# 네임드 튜플 사용
# 튜플인데 딕셔너리의 성질을 가지고 있음
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

# 두 점 선언
# 클래스 형식으로 튜플을 추상화하고 있죠
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# 계산
l_leng2 = sqrt((pt4.x - pt3.x) ** 2 + (pt4.y - pt3.y) ** 2)

# 출력
print(l_leng2)
print(l_leng1 == l_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y']) # 리스트로 선언하기
Point2 = namedtuple('Point', 'x, y') # 콤마찍는 방법 좋아하는 사람 많음. 실수 줄일 수 있으니까
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False

# 출력
print(Point1, Point2, Point3, Point4)

print()
print()

# Dict to Unpacking
# 누가 딕셔너리로 값을 줬는데, 네임드 튜플에 할당 해 볼게요
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

# 출력
print(p1, p2, p3, p4, p5)

print()
print()

# 사용
print(p1[0] + p2[1]) # Index Error 주의
print(p1.x + p2.y) # 클래스 변수 접근 방식

# Unpacking
x, y = p3

print(x+y)

# Rename 테스트
print(p4)

print()
print()


# 네임드 튜플 메소드
temp = [52, 38] 

# _make() : 새로운 객체 생성
# 리스트를 네임드 튜플로 변환하는게 _make() 함수입니다
p4 = Point1._make(temp)

print(p4)

# _fields : 필드 네임 확인/매직 메소드 성의 메소드
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
# 네임드 튜플을 딕셔너리로 변환하는 거라고 보시면 됩니다
print(p1._asdict(), p4._asdict())


# 실 사용 실습
# 반20명 , 4개의 반-> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
# 리스트 컴프리헨션으로 할까요, 문자열로 해야죠? 번호~, 
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split() # 공백을 기준으로 4개를 리스트로 만들어주겠죠
# 괄호열고 A, B, C, D 해도 되는게 그냥 해봤습니다

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
# 와 어렵다
# 근데 공식같이 쉽네
# 아름답다
# 반복으로 암기해야 할 듯
# 응용할 수 있도록
students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in [str(n) 
                            for n in range(1,21)]]


print()
print()

print(len(students2))
print(students2)

print()
print()

# 출력
for s in students:
    print(s)
